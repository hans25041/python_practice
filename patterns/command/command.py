from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        raise NotImplementedError

    @abstractmethod
    def turn_off(self):
        raise NotImplementedError


class LightSwitch(Switchable):
    def turn_on(self):
        return "The light turned on."

    def turn_off(self):
        return "The light turned off."


class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError


class CloseSwitchCommand(Command):
    def __init__(self, switch):
        self._switch = switch

    def execute(self):
        return self._switch.turn_on()


class OpenSwitchCommand(Command):
    def __init__(self, switch):
        self._switch = switch

    def execute(self):
        return self._switch.turn_off()


class Client:
    def __init__(self, open_command, close_command):
        self._open_command = open_command
        self._close_command = close_command

    def open(self):
        return self._open_command.execute()

    def close(self):
        return self._close_command.execute()
