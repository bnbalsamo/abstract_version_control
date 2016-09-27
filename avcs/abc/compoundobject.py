from abc import ABCMeta

class CompoundObject(metaclass=ABCMeta):

    _arrangement = None

    def get_arrangement(self):
        return self._arrangement

    def set_arrangement(self, x):
        if self.validate_arrangement(x):
            self._arrangement = x
        else:
            raise AttributeError("validate_arrangement() failed!")

    def del_arrangement(self):
        self._arrangement = None

    def validate_arrangement(self, arrangement):
        return True

    arrangement = property(get_arrangement, set_arrangement, del_arrangement)
