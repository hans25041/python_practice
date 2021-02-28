from abc import abstractmethod, ABC


class Gadget(ABC):
    @abstractmethod
    def boom(self):
        raise NotImplementedError


class FooGadget(Gadget):
    def boom(self):
        return "Foo Boom"


class BarGadget(Gadget):
    def boom(self):
        return "Bar Boom"


class Gizmo(ABC):
    @abstractmethod
    def bang(self):
        raise NotImplementedError


class FooGizmo(Gizmo):
    def bang(self):
        return "Foo Bang"


class BarGizmo(Gizmo):
    def bang(self):
        return "Bar Bang"


class WidgetCreator(ABC):
    """WidgetCreator is an abstract factory."""
    @abstractmethod
    def create_gadget(self) -> Gadget:
        raise NotImplementedError

    @abstractmethod
    def create_gizmo(self) -> Gizmo:
        raise NotImplementedError


class FooCreator(WidgetCreator):
    """FooCreator is a concrete WidgetCreator."""
    def create_gadget(self) -> Gadget:
        return FooGadget()

    def create_gizmo(self) -> Gizmo:
        return FooGizmo()


class BarCreator(WidgetCreator):
    """BarCreator is a concrete WidgetCreator."""

    def create_gadget(self) -> Gadget:
        return BarGadget()

    def create_gizmo(self) -> Gizmo:
        return BarGizmo()


class Client:
    def __init__(self, creator: WidgetCreator):
        self._creator = creator

    def boom(self):
        return self._creator.create_gadget().boom()

    def bang(self):
        return self._creator.create_gizmo().bang()
