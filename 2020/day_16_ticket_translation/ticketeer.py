def calculate_ticket_scanning_error_rate(file_path):
    tickets_data = _get_tickets_data(file_path)
    incorrect_values = _get_incorrect_values(tickets_data)
    return sum(incorrect_values)


def _get_tickets_data(file_path):
    tickets_data = {'fields': [],
                    'your_ticket': None,
                    'nearby_tickets': []}

    with open(file_path, 'r') as file:
        section = 'fields'

        for line in file:
            line = line.strip()

            if line == '':
                continue

            if line == 'your ticket:':
                section = 'your_ticket'
                continue

            if line == 'nearby tickets:':
                section = 'nearby_tickets'
                continue

            if section == 'fields':
                tickets_data[section].append(_get_field(line))

            if section == 'your_ticket':
                tickets_data[section] = _get_your_ticket(line)

            if section == 'nearby_tickets':
                tickets_data[section].append(_get_nearby_ticket(line))

    return tickets_data


def _get_field(line):
    name, ranges = line.split(': ')
    return {'name': name, 'ranges': [range_min_max.split('-') for range_min_max in tuple(ranges.split(' or '))]}


def _get_your_ticket(line):
    return [number for number in line.split(',')]


def _get_nearby_ticket(line):
    return [number for number in line.split(',')]


def _get_incorrect_values(tickets_data):
    incorrect_values = []

    for ticket in tickets_data['nearby_tickets']:
        for value in ticket:
            value = int(value)
            value_correct = False

            for field in tickets_data['fields']:
                for field_range in field['ranges']:

                    if value in range(int(field_range[0]), int(field_range[1]) + 1):
                        value_correct = True
                        break

                if value_correct:
                    break

            if not value_correct:
                incorrect_values.append(value)

    return incorrect_values
