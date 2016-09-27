from abc import ABCMeta

from .compoundobject import CompoundObject
from .delta import Delta
from .lib import get_version

class Version(metaclass=ABCMeta):

    _identifier = None
    _reference = None
    _representation = None
    _delta = None

    def get_identifier(self):
        return self._identifier

    def set_identifier(self, x):
        if self.validate_identifier(x):
            self._identifier = x
        else:
            raise AttributeError("validate_identifier() failed!")

    def del_identifier(self):
        self._identifier = None

    def validate_identifier(self, identifier):
        return True

    def get_reference(self):
        return self._reference

    def set_reference(self, x):
        if self.validate_reference(x):
            self._reference = x
        else:
            raise AttributeError("validate_reference() failed!")

    def del_reference(self, x):
        self._reference = None

    def validate_reference(self, ref):
        return True

    def get_representation(self):
        return self._representation

    def set_representation(self, x):
        if not isinstance(x, CompoundObject) and x is not None:
            raise TypeError("{} isn't a CompoundObject or None!".format(
                type(x)
            ))
        if self.delta is not None:
            raise AttributeError("Can't set a representation and a delta " +
                                 "at the same time in the same Version!")
        self._representation = x

    def del_representation(self):
        self._representation = None

    def get_delta(self):
        return self._delta

    def set_delta(self, delta):
        if not isinstance(delta, Delta) and delta is not None:
            raise TypeError("{} isn't a Delta or None!".format(type(delta)))
        if self.representation is not None:
            raise AttributeError("Can't set a representation and a delta " +
                                 "at the same time in the same Version!")
        self._delta = delta

    def del_delta(self):
        self._delta = None

    def evaluate(self):
        if self.representation is not None:
            return self.representation
        else:
            referenced_version = get_version(self.reference)
            evaluated_referenced_version = referenced_version.evaluate()
            delta_applier = DeltaApplier()
            return delta_applier(evaluated_referenced_version, self.delta)

    identifier = property(get_identifier, set_identifier, del_identifier)
    reference = property(get_reference, set_reference, del_reference)
    representation = property(get_representation, set_representation,
                              del_representation)
    delta = property(get_delta, set_delta, del_delta)
