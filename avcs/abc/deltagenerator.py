from abc import ABCMeta, abstractmethod

from .compoundobject import CompoundObject

class DeltaGenerator(metaclass=ABCMeta):
    @abstractmethod
    def generate_delta(src_obj, tar_obj):
        pass
