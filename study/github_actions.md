## Github Actions
깃허브 내에서 지원하는 자동화 도구(CI/CD 플랫폼)이다.  
개발자가 코드를 Repository에 올리면 그 코드를 자동으로 빌드, 테스트, 배포까지 해준다.  
위 기능을 수행하기 위한 핵심 요소는 다음의 5가지이다.   
<br/>  

1. Workflow(워크플로우)  
  * 자동화 프로세스의 최상위 단계로, Repository 내에 .github/workflow 디렉터리에 YAML 폴더로 저장된다.
<br/>
 
2. Event(이벤트)  
  * 워크플로우를 실행시키는 트리거이다. ex) 코드 push, Pull request 생성, 특정 시간대 생성 등
<br/>

3. Jobs(잡)  
  * 하나의 워크플로우 안에서 실행되는 독립적인 단계들의 집합이다. 기본적으로 여러 Job은 동시에 실행된다.

4. Steps(스텝)
  * Job 안에서 실행되는 개별 작업이다. 명령어를 실행하거나 미리 만들어진 'Action'을 호출한다.

5. Actions(액션)
  * 자주 사용하는 기능을 미리 만들어둔 재사용 가능한 코드 블록입니다. (예: 체크아웃, 노드 환경 설정 등)


### YAML 파일 예시
```yaml
name: My First Workflow
on: [push] # 이벤트: 푸시가 발생하면 실행

jobs:
  say-hello:
    runs-on: ubuntu-latest # 실행 환경
    steps:
      - name: Greet user
        run: echo "Hello, GitHub Actions!"
```
