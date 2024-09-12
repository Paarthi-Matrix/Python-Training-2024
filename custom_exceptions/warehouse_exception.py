from constants.constants import WAREHOUSE_ITEM_ZERO_LOGGER  # todo naming


class WarehouseException(Exception):
    """
       Exception raised for errors related to warehouse operations.

       Attributes:
           data (str): The data associated with the exception, typically providing additional context for the error.
           message (str): The message explaining the error. Defaults to a standard warehouse error message.
    """
    def __init__(self, data, message=WAREHOUSE_ITEM_ZERO_LOGGER):
        self.data = data
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return WAREHOUSE_ITEM_ZERO_LOGGER.format(data=self.data)
