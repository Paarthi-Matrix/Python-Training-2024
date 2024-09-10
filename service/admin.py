import uuid

admins = {}


def register_admin(name, email, password):
    """
    Registers a new admin with the provided details and generates a unique admin ID.

    Args:
        name (str): The name of the admin.
        email (str): The email address of the admin.
        password (str): The password for the admin's account.

    Returns:
        str: A unique identifier for the registered admin.
    """
    admin_id = str(uuid.uuid4())
    admin_details = {
        "admin_id": admin_id,
        "name": name,
        "email": email,
        "password": password
    }
    admins[admin_id] = admin_details
    return admin_id


def is_admin_registered():
    """
    Checks if at least one admin is registered.

    Returns:
        bool: True if more than one admin detail is present; False otherwise.
    """
    if len(admins) >= 1:
        return True
    return False
