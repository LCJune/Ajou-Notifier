from abc import ABC, abstractmethod

class baseFormatter(ABC):
    
    @abstractmethod
    def format(self, data):
        pass