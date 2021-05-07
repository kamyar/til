

from abc import ABC, abstractmethod


class BasePlugin(ABC):

    @abstractmethod
    def new_til(self, title, date, content):
        pass
