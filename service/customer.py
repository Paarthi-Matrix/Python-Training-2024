import uuid

from constants.constants import (
    CUSTOMER_QUOTATION_NUMBER, ITEM_CRITICAL_LEVEL,
    ITEM_QUANTITY, ITEM_STATUS, ITEM_STATUS_CRITICAL,
    ITEM_STATUS_NOT_AVAILABLE, STATUS, STATUS_SENT,
    WAREHOUSE_ITEM_ZERO_LOGGER
)
from custom_exceptions.warehouse_exception import WarehouseException
from resources.config import logger

warehouse = {}
vendor_quotations = {}
quotations = {}


def create_ware_house():
    """
    Creates a new warehouse with a unique ID and initializes it with an empty list.

    Returns:
        str: The unique ID of the created warehouse.
    """
    warehouse_id = str(uuid.uuid4())
    warehouse[warehouse_id] = []
    return warehouse_id


def add_item(warehouse_id, new_item):
    """
        This function adds new item to the existing warehouse id

    Parameters:
        warehouse_id (str) : Respective warehouse id
        new_item (dict) : Dictionary of new item
    """
    warehouse_list = warehouse[warehouse_id]
    warehouse_list.append(new_item)


def delete_item(warehouse_id, item_no):
    """
        Deletes an item from the warehouse based on the given warehouse ID and item number.

        Parameters:
            warehouse_id (str): The ID of the warehouse from which the item should be deleted.
            item_no (str): The number or ID of the item to be deleted from the warehouse.

        Returns:
            bool: True if the item is found and successfully deleted; False if the item is not found.
    """
    item_list = warehouse[warehouse_id]
    for item in item_list:
        if item_no in item:
            item_list.remove(item)
            return True
    return False


def change_item_quantity(warehouse_id, item_number, delta):
    """
        Adjusts the quantity of a specific item in a warehouse and updates its status accordingly.

        Parameters:
            warehouse_id (str): The ID of the warehouse containing the item.
            item_number (str): The number or ID of the item whose quantity needs to be changed.
            delta (int): The change in quantity (can be positive or negative).

        Returns:
            bool: True if the item's quantity is successfully updated; False if the warehouse is not found.

        Raises:
            WarehouseException: If the resulting quantity is negative, indicating insufficient stock.
    """
    item_list = warehouse.get(warehouse_id, None)
    if item_list is None:
        logger.error(f"Warehouse with ID {warehouse_id} not found.")
        return False

    for item in item_list:
        if item_number in item:
            item_data = item[item_number]
            if item_data[ITEM_QUANTITY] + delta < 0:
                logger.error(WAREHOUSE_ITEM_ZERO_LOGGER)
                raise WarehouseException(delta)
            item_data[ITEM_QUANTITY] += delta

            if item_data[ITEM_QUANTITY] == 0:
                item_data[ITEM_STATUS] = ITEM_STATUS_NOT_AVAILABLE
            elif item_data[ITEM_QUANTITY] <= item_data[ITEM_CRITICAL_LEVEL]:
                item_data[ITEM_STATUS] = ITEM_STATUS_CRITICAL
            logger.info(f"Updated item: {item_number}, new quantity: {item_data[ITEM_QUANTITY]}")
            return True


def get_warehouse(warehouse_id):
    """
    Retrieves the warehouse data for a given warehouse ID.

    Parameters:
        warehouse_id (str): The ID of the warehouse to retrieve.
    Returns:
        dict or None: The warehouse data dictionary if found; otherwise, None.
    """
    if warehouse_id in warehouse:
        return warehouse[warehouse_id]
    else:
        return None


# TODO Need to utilize the user_id parameter, so that the user can access only their warehouses
def is_warehouse_available(warehouse_id, user_id):
    """
    Checks if a warehouse exists for a given warehouse ID.

    Parameters:
        warehouse_id (str) : The ID of the warehouse to check.
        user_id (str) : user_id of the user.

    Returns:
        bool: True if the warehouse exists; False otherwise.
    """
    return warehouse_id in warehouse


def get_vendor_quotations_by_quotation_id(customer_quotation_id):
    """
    Retrieves all vendor quotations based on the customer quotation ID.

    Parameters:
        customer_quotation_id (str): The ID of the customer quotation.

    Returns:
        dict: A dictionary containing all matching vendor quotations.
    """
    matching_quotations = {}

    for vendor_id, quotation_form in vendor_quotations.items():
        if (quotation_form.get(CUSTOMER_QUOTATION_NUMBER) == customer_quotation_id
                and quotation_form.get(STATUS) == STATUS_SENT):
            matching_quotations[vendor_id] = quotation_form

    return matching_quotations if matching_quotations else None


def get_vendor_quotation_by_id(vendor_quotation_id, customer_quotation_id):
    """
    Retrieves a vendor quotation based on vendor ID, customer ID, and status.

    Parameters:
        vendor_quotation_id (str): The ID of the vendor quotation.
        customer_quotation_id (str): The ID of the customer quotation.

    Returns:
        dict or None: Returns the matching vendor quotation dictionary if found; otherwise, None.
    """
    quotation_form = vendor_quotations.get(vendor_quotation_id)
    if (quotation_form
            and quotation_form.get(CUSTOMER_QUOTATION_NUMBER) == customer_quotation_id
            and quotation_form.get(STATUS) == STATUS_SENT):

        return quotation_form
    else:
        return None


def set_vendor_quotations(vendor_quotation):
    """
        Adds a new vendor quotation to the vendor quotations dictionary with a unique ID.

        Parameters:
            vendor_quotation (dict): The vendor quotation details to be added.

        Returns:
            None
    """
    vendor_quotation_id = str(uuid.uuid4())
    vendor_quotations[vendor_quotation_id] = vendor_quotation
    logger.info(f"Vendor quotation was successfully sent to customer with vendor quotation id {vendor_quotation_id}")
