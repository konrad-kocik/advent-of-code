def change_password(old_password: str) -> str:
    new_password = ''

    while not _meets_requirements(new_password):
        new_password = _increment(old_password)
        old_password = new_password

    return new_password


def _meets_requirements(password: str) -> bool:
    return _has_only_allowed_chars(password) and _has_increasing_straight(password) and _has_at_least_two_pairs(password)


def _has_only_allowed_chars(password: str) -> bool:
    for disallowed_char in 'iol':
        if disallowed_char in password:
            return False
    return True


def _has_increasing_straight(password: str) -> bool:
    for i in range(len(password) - 2):
        first_char_num = ord(password[i])
        second_char_num = ord(password[i + 1])
        third_char_num = ord(password[i + 2])

        if first_char_num + 2 == second_char_num +1 == third_char_num:
            return True

    return False


def _has_at_least_two_pairs(password: str) -> bool:
    for i in range(len(password) - 1):
        first_char = password[i]
        second_char = password[i + 1]

        if first_char == second_char:
            for j in range(i + 2, len(password) - 1):
                third_char = password[j]
                fourth_char = password[j + 1]

                if third_char == fourth_char:
                    return True

    return False


def _increment(password: str) -> str:
    incremented_password = ''

    for char in password[::-1]:
        char_num = ord(char)

        if char_num < 122:
            char_num += 1
            char = chr(char_num)
            incremented_password = f'{char}{incremented_password}'
            incremented_password = f'{password[:len(password) - len(incremented_password)]}{incremented_password}'
            break
        else:
            char = 'a'
            incremented_password = f'{char}{incremented_password}'

    return incremented_password
