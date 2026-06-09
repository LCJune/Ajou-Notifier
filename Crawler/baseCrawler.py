import requests
from bs4 import BeautifulSoup
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from abc import ABC, abstractmethod # Abstract Base Classes, ABC와 abstractmethod는 같이 쓰인다.

# baseCrawler를 추상 클래스로 설정, 객체 생성을 금지시킨다.
# baseCrawler는 Crawler 객체들의 설계도일뿐, 실제로 사용할 객체가 아니다.
class baseCrawler(ABC):

    def __init__(self):
        self.session = requests.Session()

        # session의 header를 설정하는 메서드
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 ..." # header가 없으면 사용자를 확인하는 특정 웹 사이트들은 접속이 불가능하다.
        })

        # HTTP 요청 실패 시 재시도 조건 설정을 담은 Retry 객체 생성
        retry = Retry(
            total=3, # 총 3번 재시도
            backoff_factor=0.3, # 재시도 간격
            status_forcelist=[ # 목록 안의 상태 코드에만 재시도 실행
                500,
                502,
                503,
                504
            ]
        )
        
        """
        Retry 객체를 Session 객체에 바로 적용할 수 없기에,
        HTTPAdapter를 이용해 Session 객체에 적용한다.
        이렇듯 HTTPAdapter는 requests 객체에 다른 추가 설정을 적용할 때 쓰인다.
        """
        adapter = HTTPAdapter( 
            max_retries = retry
        )

        # mount 메서드로 특정 URL 형식에 사용할 Adapter를 정한다.(미정 시 기본)
        self.session.mount(
            'https://',
            adapter
        )

        self.session.mount(
            'http://',
            adapter
        )

    # 아래 메서드들을 추상 메서드로 지정, 하위 클래스가 반드시 구현하도록 강제한다.
    @abstractmethod
    def _crawl(self, url):
        pass
    
    @abstractmethod
    def _parse(self, response):
        pass
    
    @abstractmethod
    def get_notices(self):
        pass
