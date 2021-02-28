from pytest import raises

from patterns.command.command import LightSwitch, Switchable, \
    CloseSwitchCommand, Command, OpenSwitchCommand, Client


class TestLightSwitch:
    def test_initialization(self):
        switch = LightSwitch()
        assert isinstance(switch, LightSwitch)
        assert isinstance(switch, Switchable)

    def test_turn_on_light_switch(self):
        switch = LightSwitch()
        assert switch.turn_on() == "The light turned on."

    def test_turn_off_light_switch(self):
        switch = LightSwitch()
        assert switch.turn_off() == "The light turned off."


class TestCloseSwitchCommand:
    def test_initialization(self):
        command = CloseSwitchCommand(LightSwitch())
        assert isinstance(command, CloseSwitchCommand)
        assert isinstance(command, Command)

    def test_execute_close_switch_command_with_light_switch(self):
        command = CloseSwitchCommand(LightSwitch())
        assert command.execute() == "The light turned on."

    def test_execute_close_switch_command_with_invalid_switch(self):
        command = CloseSwitchCommand(None)
        with raises(AttributeError):
            command.execute()


class TestOpenSwitchCommand:
    def test_initialization(self):
        command = OpenSwitchCommand(LightSwitch())
        assert isinstance(command, OpenSwitchCommand)
        assert isinstance(command, Command)

    def test_execute_open_switch_command_with_light_switch(self):
        command = OpenSwitchCommand(LightSwitch())
        assert command.execute() == "The light turned off."

    def test_execute_open_switch_command_with_invalid_switch(self):
        command = OpenSwitchCommand(None)
        with raises(AttributeError):
            command.execute()


class TestClient:
    def test_initialization(self):
        client = Client(None, None)
        assert isinstance(client, Client)

    def test_client_open(self):
        client = self._construct_light_switch_client()
        assert client.open() == "The light turned off."

    def test_client_close(self):
        client = self._construct_light_switch_client()
        assert client.close() == "The light turned on."

    def test_cannot_open_with_none_command(self):
        client = Client(None, None)
        with raises(AttributeError):
            client.open()

    def test_cannot_close_with_none_command(self):
        client = Client(None, None)
        with raises(AttributeError):
            client.close()

    @staticmethod
    def _construct_light_switch_client():
        switch = LightSwitch()
        open_command = OpenSwitchCommand(switch)
        close_command = CloseSwitchCommand(switch)
        return Client(open_command, close_command)
