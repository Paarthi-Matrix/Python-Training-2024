def is_valid_name(name):
    for char in name:
        if 65 <= ord(char) <= 90:
            continue
        elif 97 <= ord(char) <= 122:
            continue
        elif char == ' ':
            continue
        else:
            return False
    return True


def is_valid_email(email):
    if email.__contains__("@gmail.com"):
        if email[0] == '.' or email[-1] == '.':
            return False
        else:
            for index in range(len(email) - 10):
                if 97 <= ord(email[index]) <= 122:
                    continue
                elif 48 <= ord(email[index]) <= 57:
                    continue
                else:
                    return False
            return True
    return False


def is_valid_password(password):
    if len(password) < 8:
        return False
    else:
        lower = 0
        upper = 0
        digit = 0
        for index in range(len(password)):
            if 65 <= ord(password[index]) <= 90:
                lower += 1
            elif 97 <= ord(password[index]) <= 122:
                upper += 1
            elif 48 <= ord(password[index]) <= 57:
                digit += 1
            elif password[index] == ' ':
                return False
        if upper > 0 and lower > 0 and digit > 0:
            return True
        else:
            return False


def is_valid_mobile(mobile):
    if mobile[0] == '6' or mobile[0] == '7' or mobile[0] == '8' or mobile[0] == '9':
        if len(mobile) == 10:
            return True
        else:
            return False
    else:
        return False
