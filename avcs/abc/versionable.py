from abc import ABCMeta

from .version import Version

class Versionable(metaclass=ABCMeta):

    _identifier = None
    _identity = None
    _versions = []

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

    def get_identity(self):
        return self._identity

    def set_identity(self, x):
        if self.validate_identity(x):
            self._identity = x
        else:
            raise AttributeError("validate_identity() failed!")

    def del_identity(self):
        self._identity = None

    def validate_identity(self, identity):
        return True

    def get_versions(self):
        return self._versions

    def set_versions(self, versions):
        self.del_versions()
        for x in versions:
            self.add_version(x)

    def del_versions(self):
        self._versions = []

    def add_version(self, version):
        if not isinstance(version, Version):
            raise TypeError("{} isn't a version!".format(type(version)))
        self._versions.append(version)

    identifier = property(get_identifier, set_identifier, del_identifier)
    identity = property(get_identity, set_identity, del_identity)
    versions = property(get_versions, set_versions, del_versions)
