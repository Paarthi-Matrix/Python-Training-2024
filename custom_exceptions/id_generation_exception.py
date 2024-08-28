from constants.biznex_constants import USER_ID_GENERATION_EXCEPTION_DETAIL_MESSAGE
from constants.biznex_constants import USER_ID_GENERATION_EXCEPTION_MESSAGE


class IdGenerationException(Exception):
    def __init__(self, data, message=USER_ID_GENERATION_EXCEPTION_MESSAGE):
        self.data = data
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return USER_ID_GENERATION_EXCEPTION_DETAIL_MESSAGE.format(data=self.data)
