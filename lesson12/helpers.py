import re


class WrongDateFormat(Exception):
    pass


class WrongPhoneNumberFormat(Exception):
    pass


def check_birthday_date(date):
    BIRTH_REG = re.compile(r"(\d{2})\s(\d{2})\s(\d{4})")

    if BIRTH_REG.match(date):
        return True
    else:
        raise WrongDateFormat


def check_phone_number(number):
    PHONE_REGEX = re.compile(r"^380\d{2}\d{7}$")

    if PHONE_REGEX.match(str(number)):
        return True
    else:
        raise WrongPhoneNumberFormat


