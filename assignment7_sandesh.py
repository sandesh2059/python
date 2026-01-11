from abc import ABC , abstractmethod

class EWallet(ABC):

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass


class esewa