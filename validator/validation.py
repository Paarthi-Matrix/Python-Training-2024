import re

from helper.constant import (
    REGEX_VALIDATE_WASTAGE_TYPE,
    REGEX_VALIDATE_STATUS, REGEX_VALIDATE_DOOR_N0,
    REGEX_VALID_COMPLAINT,
)


def is_valid_name(name):
    return bool(re.match(r'^[A-Za-z ]+$', name))


def is_valid_email(email):
    return bool(re.match(r'^[a-z0-9_.]+@(ideas2it|gmail|yahoo)\.com$', email))


def is_valid_password(password):
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\s]{8,}$', password))


def is_valid_mobile(mobile):
    return bool(re.match(r'^[6-9]\d{9}$', mobile))


def is_valid_load(load):
    if re.match(r'^(low|Heavy)$', load, re.IGNORECASE):
        return True
    return False


def is_valid_cycle_period(cycle_period):
    if re.match(r'^(daily)$', cycle_period, re.IGNORECASE):
        return True
    return False


def is_valid_wastage_type(wastage_type):
    return bool(re.match(REGEX_VALIDATE_WASTAGE_TYPE, wastage_type, re.IGNORECASE))


def is_valid_city(city):
    return bool(re.match(r'^chennai$', city, re.IGNORECASE))


def is_valid_status(status):
    if re.match(REGEX_VALIDATE_STATUS, status, re.IGNORECASE):
        return True
    return False


def is_valid_door_no(door_no):
    if re.match(REGEX_VALIDATE_DOOR_N0, door_no):
        return True
    return False


def is_complaint_valid(complaint):
    if re.match(REGEX_VALID_COMPLAINT, complaint):
        return True
    return False


def check_valid_input(value, validation_func):
    """Helper function to get and validate input."""
    return validation_func(value)
