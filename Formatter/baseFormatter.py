from abc import ABC, abstractmethod

class baseFormatter(ABC):
    
    def __init__(self):
        pass
    
    #@abstractmethod - abstractmethod decorator를 위에 쓰면, @staticmethod decorator를 쓰지 못함. 
    # 따라서 @abstractmethod를 쓰고 싶으면, @staticmethod 아래에 써야 함.
    @staticmethod
    def format(data):
        pass