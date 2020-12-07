from re import match


def get_valid_passports_count():
    return len(_get_valid_passports(_get_passports()))


def _get_passports():
    passports = []

    with open('input.raw', 'r') as file:
        passport = {}

        for line in file:
            line = line.rstrip()

            if line == '':
                passports.append(passport)
                passport = {}
                continue

            for entry in line.split(' '):
                key, value = entry.split(':')
                passport[key] = value

        passports.append(passport)

    return passports


def _get_valid_passports(passports):
    return [p for p in passports if
            _is_byr_valid(p) and
            _is_iyr_valid(p) and
            _is_eyr_valid(p) and
            _is_hgt_valid(p) and
            _is_hcl_valid(p) and
            _is_ecl_valid(p) and
            _is_pid_valid(p)]


def _is_byr_valid(passport):
    return passport.get('byr', False) and 1920 <= int(passport['byr']) <= 2002


def _is_iyr_valid(passport):
    return passport.get('iyr', False) and 2010 <= int(passport['iyr']) <= 2020


def _is_eyr_valid(passport):
    return passport.get('eyr', False) and 2020 <= int(passport['eyr']) <= 2030


def _is_hgt_valid(passport):
    if not passport.get('hgt', False) or (not passport['hgt'].endswith('cm') and not passport['hgt'].endswith('in')):
        return False
    elif (passport['hgt'].endswith('cm') and 150 <= int(passport['hgt'][:-2]) <= 193) or \
            (passport['hgt'].endswith('in') and 59 <= int(passport['hgt'][:-2]) <= 76):
        return True
    else:
        return False


def _is_hcl_valid(passport):
    return passport.get('hcl', False) and match('^#[0-9a-f]{6}$', passport['hcl'])


def _is_ecl_valid(passport):
    return passport.get('ecl', False) and passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def _is_pid_valid(passport):
    return passport.get('pid', False) and match('^[0-9]{9}$', passport['pid'])


print(get_valid_passports_count())
