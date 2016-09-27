from abc import ABCMeta

from .versionable import Versionable

class VersionControlSystem(metaclass=ABCMeta):

    _versionables = []

    def get_versionables(self):
        return self._versionables

    def set_versionables(self, versionables):
        self.del_versionables()
        for x in versionables:
            self.add_versionable(x)

    def del_versionables(self):
        self._versionables = []

    def add_versionable(self, versionable):
        if not isinstance(versionable, Versionable):
            raise TypeError("{} is not a Versionable!".format(
                type(versionable))
            )
        self._versionables.append(versionable)

    versionables = property(get_versionables,
                            set_versionables,
                            del_versionables)
