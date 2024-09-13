import hashlib

import bcrypt

from resources.logger_configuration import logger

"""def hash_password(password):
    
       Hashes a password using the SHA-256 algorithm.

       Parameters:
           password (str): The plain text password to be hashed.

       Returns:
           str: The hexadecimal representation of the hashed password.
    
    password_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256(password_bytes)
    return hash_object.hexdigest()"""


def continue_operation(operative_func):
    continue_choice = input("Do you want to continue? (YES/NO): ").strip().upper()
    if continue_choice == "YES":
        operative_func()
    elif continue_choice == "NO":
        logger.info("Exiting customer actions.")


def hash_password(password: str) -> str:
    """Hash a password."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def check_password(stored_password: str, provided_password: str) -> bool:
    """Check a hashed password."""
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))
