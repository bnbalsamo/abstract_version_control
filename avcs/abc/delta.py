from abc import ABCMeta

class Delta(metaclass=ABCMeta):

    _operations = []

    def get_operations(self):
        return self._operations

    def set_operations(self, operations):
        self.del_operations()
        for x in operations:
            self.add_operations(x)

    def del_operations(self):
        self.operations = []

    def add_operation(self, operation):
        if self.validate_operation(operation):
            self._operations.append(operation)

    def validate_operation(self, op):
        return True
