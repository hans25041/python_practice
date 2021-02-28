from abc import ABC, abstractmethod


class Target(ABC):
    @abstractmethod
    def operation(self):
        raise NotImplementedError


class Adapter(Target):
    def operation(self):
        return Adaptee().action()


class Adaptee:
    def action(self):
        return "Adaptee ran its action."


class Client:
    def __init__(self, dependency):
        self._dependency = dependency

    def run(self):
        return self._dependency.operation()
