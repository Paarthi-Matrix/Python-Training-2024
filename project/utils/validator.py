import re

from common.common_constants import EMAIL_REGEX, MOBILE_NUMBER_REGEX, NAME_REGEX


def is_valid_email(email):
    email_regex = EMAIL_REGEX
    return re.match(email_regex, email) is not None


def is_valid_mobile(number):
    mobile_number_regex = MOBILE_NUMBER_REGEX
    return re.match(mobile_number_regex, number) is not None


def is_valid_name(name):
    name_regex = NAME_REGEX
    return re.match(name_regex, name) is not None
