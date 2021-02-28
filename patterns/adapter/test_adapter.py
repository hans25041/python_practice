from pytest import raises

from patterns.adapter.adapter import Target, Adapter, Client, Adaptee


class TestAdapter:
    def test_initialization(self):
        adapter = Adapter()
        assert isinstance(adapter, Adapter)
        assert isinstance(adapter, Target)


class TestAdaptee:
    def test_initialization(self):
        adaptee = Adaptee()
        assert isinstance(adaptee, Adaptee)
        assert not isinstance(adaptee, Target)

    def test_action(self):
        adaptee = Adaptee()
        assert adaptee.action() == "Adaptee ran its action."


class TestClient:
    def test_initialization(self):
        client = Client(None)
        assert isinstance(client, Client)

    def test_cannot_run_client_on_none(self):
        client = Client(None)
        with raises(AttributeError):
            client.run()

    def test_cannot_run_client_on_adaptee(self):
        client = Client(Adaptee())
        with raises(AttributeError):
            client.run()

    def test_can_run_adaptee_via_adapter(self):
        client = Client(Adapter())
        assert client.run() == "Adaptee ran its action."
