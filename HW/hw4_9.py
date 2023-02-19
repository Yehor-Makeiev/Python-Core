def is_valid_pin_codes(pin_codes):

    if len(pin_codes) == 0:
        return False
    if len(pin_codes) != len(set(pin_codes)):
        return False

    for pink in pin_codes:

        if type(pink) != str:
            return False
        elif len(pink) != 4:
            return False
        elif str(pink).isnumeric() != True:
            return False

    return True


if __name__ == "__main__":
    is_valid_pin_codes(['1101', '9g34', '0011'])
