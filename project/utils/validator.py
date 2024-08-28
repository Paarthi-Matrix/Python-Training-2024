import re

from common.common_constants import EMAIL_REGEX


def is_valid_email(email):
    regex = EMAIL_REGEX
    if re.match(regex, email):
        return True
    else:
        return False
