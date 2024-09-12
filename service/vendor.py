import uuid

customer_quotation_request = {}


def set_quotations(quotation):
    """
        Creates a new customer quotation and stores it in the system.

        Generates a unique quotation ID, associates it with the provided quotation,
        and stores it in the customer quotation request dictionary.

        Parameters:
            quotation (dict): A dictionary containing the details of the quotation.

        Returns:
            str: The unique ID assigned to the new quotation.
    """
    quotation_id = str(uuid.uuid4())
    customer_quotation_request[quotation_id] = quotation
    return quotation_id


def get_quotation(quotation_id):
    """
        Retrieves a specific customer quotation by its ID.

        Parameters:
            quotation_id (str): The unique ID of the quotation to retrieve.

        Returns:
            dict or None: The quotation data if found; otherwise, None.
    """
    return customer_quotation_request.get(quotation_id, None)


def get_all_quotations():
    """
       Retrieves all customer quotations stored in the system.

       Returns:
           dict: A dictionary containing all customer quotations.
    """
    return customer_quotation_request


def update_customer_quotation(quotation_id, edited_quotation):
    """
        Updates an existing customer quotation with new details.

        Replaces the existing quotation data associated with the given ID
        with the new, edited quotation details.

        Parameters:
            quotation_id (str): The unique ID of the quotation to update.
            edited_quotation (dict): The updated details of the quotation.

        Returns:
            None
    """
    customer_quotation_request[quotation_id] = edited_quotation

