import string


def is_valid_password(password):
    dig = 0
    upp = 0
    low = 0
    symb = 0

    if len(password) != 8:
        return False

    for s in password:
        if s in string.digits:
            dig += 1
        if s in string.ascii_uppercase:
            upp += 1
        if s in string.ascii_lowercase:
            low += 1
        if s in string.punctuation:
            symb += 1
    if dig >= 1 and upp >= 1 and low >= 1 and symb >= 0:
        return True

    else:
        return False


if __name__ == "__main__":
    is_valid_password("NmlDl1V0")


# def is_valid_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#     if len(password) == 8 and has_upper and has_lower and has_num:
#         return True
#     return False
