def get_data():
    data = []

    with open('input.raw', 'r') as file:
        for line in file:
            min_max, letter, password = line.split(' ')
            data.append((*min_max.split('-'), letter.replace(':', ''), password.rstrip()))

    return data


def get_correct_passwords(data):
    return [d[3] for d in data if bool(d[3][int(d[0]) - 1] == d[2]) != bool(d[3][int(d[1]) - 1] == d[2])]


print(len(get_correct_passwords(get_data())))
