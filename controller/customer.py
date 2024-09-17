from constant.constant import (
    ENTER_PO_NUMBER,ITEM_DELETION_PROMPT, USER_DICT_USER_ID,
    NOT_FOUND_CODE, BAD_REQUEST_CODE, OK_STATUS, UN_PROCESSABLE_ENTITY
)
from custom_exceptions.warehouse_exception import WarehouseException
from controller.procure_to_payment import get_purchase_order_by_po_number
from resources.config import logger
from service.customer import (
    add_item, change_item_quantity, delete_item,
    get_vendor_quotations_by_quotation_id, get_warehouse,
    is_warehouse_available
)
from service.procure_to_payment import update_purchase_order
from service.vendor import set_quotations, update_customer_quotation
from util.common_utils import generate_random_string
from util.user_input_validation import is_valid_number


def view_warehouse(warehouse_id):
    """
        This function is used to view the warehouse of the user by wafe house id
    Parameters:
        warehouse_id (str) : warehouse id to be viewed

    Returns:
        vendor_quotation (dict) : Returns the requested vendor quotation by Id.
                                  If no ID present returns None
    """
    return get_warehouse(warehouse_id)


def add_item_to_warehouse(warehouse_id, item_details, user_id):
    """
        Adds a new item to a specified warehouse.

        The function adds the item to the specified warehouse if it exists.

        Parameters:
            warehouse_id (str) : warehouse id of the warehouse ot be added.
            item_details (dict) : Dictionary of items that are need to be added to the warehouse
            user_id (str) : user id of the logged-in user
    """
    new_item = {}
    if not is_warehouse_available(warehouse_id, user_id):
        logger.error(f"No such warehouse with id {warehouse_id} found ")
        return
    item_id = generate_random_string()
    new_item[item_id] = item_details
    add_item(warehouse_id, new_item)


def delete_item_from_warehouse(warehouse_id, item_number, user_id):
    """
        Deletes an item from a specified warehouse.

        The function prompts the user for the warehouse ID and item number,
        verifies the existence of the warehouse, and attempts to delete the specified item.
        If the warehouse or item does not exist, appropriate error messages are logged.

        Parameters:
            warehouse_id (str) : warehouse id of the warehouse from which the item need to be deleted
            item_number (str) : Item number of the item to be deleted
            user_id (str) : user id of logged-in user
    """
    if not is_warehouse_available(warehouse_id, user_id):
        logger.error(f"No such warehouse with the given id {warehouse_id} is present ")
        return
    if delete_item(warehouse_id, item_number):
        logger.info(ITEM_DELETION_PROMPT)
    else:
        logger.error(f"No such item with item number {item_number} is found in warehouse")


def update_quantity(warehouse_id, item_number, delta, user_id):
    """
        Updates the quantity of an item in a specified warehouse.

        This function allows the user to update the quantity of a particular item in a warehouse
        by specifying the warehouse ID, item number, and a delta value (which can be positive or negative).
        It performs input validation, checks for the existence of the warehouse and item, and handles errors
        gracefully, logging appropriate messages based on the outcome.
    """
    if not is_warehouse_available(warehouse_id, user_id):
        logger.error(f"No such warehouse with the given id {warehouse_id} is present ")
        return NOT_FOUND_CODE
    if not is_valid_number(delta):
        logger.error(f"User gave invalid number {delta}")
        return BAD_REQUEST_CODE
    delta = int(delta)
    try:
        if change_item_quantity(warehouse_id, item_number, delta):
            logger.info(f"Item quantity changed for item numer {item_number}")
            return OK_STATUS
        else:
            logger.error(f"No such item number {item_number} found in warehouse")
            return NOT_FOUND_CODE
    except WarehouseException as e:
        logger.exception(e.message, exc_info=True)
        return UN_PROCESSABLE_ENTITY


def request_quotation(quotation_form):
    """
    This function is responsible for requesting quotation from vendor
    """
    quotation_id = set_quotations(quotation_form)
    logger.info(f"Users quotation was successfully sent. Their quotation_id is {quotation_id}")


def View_vendor_quotation(customer_quotation_id):
    """
    This function used to view the vendor quotation given to the customer
    """
    return get_vendor_quotations_by_quotation_id(customer_quotation_id)


def view_purchase_order(user):
    """
    This is used to view the purchase order given by customer
    """
    purchase_order_number = input(ENTER_PO_NUMBER)
    purchase_order = get_purchase_order_by_po_number(purchase_order_number, user[USER_DICT_USER_ID])
    if purchase_order is None:
        logger.error(f"No such purchase order number present in db {purchase_order_number}")
    print(purchase_order)


def edit_purchase_order(edited_purchase_order, purchase_order_number):
    """
        This function is used to edit the quotation given by the customer

        Parameter:
            quotation_id (str) : Quotation id to be edited
            edited_quotation (dict) : Edited form of the customer quotation
    """
    update_purchase_order(edited_purchase_order, purchase_order_number)


def edit_quotation(quotation_id, edited_quotation):
    """
    This function is used to edit the quotation given by the customer

    Parameter:
        quotation_id (str) : Quotation id to be edited
        edited_quotation (dict) : Edited form of the customer quotation
    """
    update_customer_quotation(quotation_id, edited_quotation)


def view_all_vendor_quotations(customer_quotation_id):
    """
    Used to view all the quotations given by vendor
    """
    return get_vendor_quotations_by_quotation_id(customer_quotation_id)
