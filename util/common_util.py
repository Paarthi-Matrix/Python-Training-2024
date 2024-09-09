import hashlib


def hash_password(password):
    """
       Hashes a password using the SHA-256 algorithm.

       Parameters:
           password (str): The plain text password to be hashed.

       Returns:
           str: The hexadecimal representation of the hashed password.
    """
    password_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256(password_bytes)
    return hash_object.hexdigest()
