from random import randint


def get_random_password() -> str:
    password = ""
    while len(password) != 8:
        random_num = randint(40, 126)
        password += chr(random_num)

    return str(password)


if __name__ == "__main__":
    get_random_password()
