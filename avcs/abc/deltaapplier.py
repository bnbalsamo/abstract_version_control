from abc import ABCMeta, abstractmethod

class DeltaApplier(metaclass=ABCMeta):
    @abstractmethod
    def apply_delta(compound_object, delta):
        pass
