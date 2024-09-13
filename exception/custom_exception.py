class ResourceNotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class UserAlreadyExistsError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class GarbageCollectorException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ResourceAlreadyExistsException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ExceedLimitException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InvalidCredentialException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)