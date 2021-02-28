from patterns.abstract_factory.abstract_factory import (
    WidgetCreator,
    BarCreator,
    FooCreator,

    Gadget,
    FooGadget,
    BarGadget,

    Gizmo,
    FooGizmo,
    BarGizmo,

    Client,
)


class TestWidgetCreator:

    def test_initialize_concrete_widget_creator(self):
        foo_creator = FooCreator()
        assert isinstance(foo_creator, WidgetCreator)
        assert isinstance(foo_creator, FooCreator)

        bar_creator = BarCreator()
        assert isinstance(bar_creator, WidgetCreator)
        assert isinstance(bar_creator, BarCreator)

    def test_foo_creator_produces_foo_widgets(self):
        foo_creator = FooCreator()
        foo_gadget = foo_creator.create_gadget()
        assert isinstance(foo_gadget, FooGadget)
        assert isinstance(foo_gadget, Gadget)
        foo_gizmo = foo_creator.create_gizmo()
        assert isinstance(foo_gizmo, FooGizmo)
        assert isinstance(foo_gizmo, Gizmo)

    def test_bar_creator_produces_bar_widgets(self):
        bar_creator = BarCreator()
        bar_gadget = bar_creator.create_gadget()
        assert isinstance(bar_gadget, BarGadget)
        assert isinstance(bar_gadget, Gadget)
        bar_gizmo = bar_creator.create_gizmo()
        assert isinstance(bar_gizmo, BarGizmo)
        assert isinstance(bar_gizmo, Gizmo)

    def test_client_with_foo_creator(self):
        client = Client(FooCreator())
        assert client.boom() == "Foo Boom"
        assert client.bang() == "Foo Bang"

    def test_client_with_bar_creator(self):
        client = Client(BarCreator())
        assert client.boom() == "Bar Boom"
        assert client.bang() == "Bar Bang"
