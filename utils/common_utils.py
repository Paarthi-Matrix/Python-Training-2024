import random
import string


def generate_random_string(length=8):
    """
    Generates a random string of the specified length consisting of uppercase letters and digits.

    Parameters:
        length (int): The length of the random string to generate (default is 8).

    Returns:
        str: A random string of the specified length.
    """
    characters = string.ascii_uppercase + string.digits
    random_string = ''.join(random.choices(characters, k=length))
    return random_string
