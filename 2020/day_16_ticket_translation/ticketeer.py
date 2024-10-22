def calculate_ticket_scanning_error_rate(file_path):
    tickets_data = _get_tickets_data(file_path)
    incorrect_values = _get_incorrect_values(tickets_data)
    return sum(incorrect_values)


def get_fields_in_correct_order(file_path):
    tickets_data = _get_tickets_data(file_path)
    return _get_fields_in_correct_order(tickets_data)


def calculate_your_ticket_hash(file_path):
    tickets_data = _get_tickets_data(file_path)
    fields_in_correct_order = _get_fields_in_correct_order(tickets_data)
    return _calculate_your_ticket_hash(fields_in_correct_order, tickets_data['your_ticket'])


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


def _get_fields_in_correct_order(tickets_data):
    tickets_data = _remove_incorrect_nearby_tickets(tickets_data)
    impossible_field_positions = _get_impossible_field_positions(tickets_data)
    possible_field_positions = _get_possible_field_positions(tickets_data, impossible_field_positions)
    correct_field_positions = _get_correct_field_positions(tickets_data, possible_field_positions)
    return correct_field_positions


def _remove_incorrect_nearby_tickets(tickets_data):
    incorrect_tickets = []

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
                incorrect_tickets.append(ticket)
                break

    for incorrect_ticket in incorrect_tickets:
        tickets_data['nearby_tickets'].remove(incorrect_ticket)

    return tickets_data


def _get_impossible_field_positions(tickets_data):
    cant_be_at = {}

    for ticket_id, ticket in enumerate(tickets_data['nearby_tickets'], start=1):
        for position, value in enumerate(ticket, start=1):
            for field in tickets_data['fields']:

                ranges = field["ranges"]
                if int(value) not in range(int(ranges[0][0]), int(ranges[0][1]) + 1) and \
                        int(value) not in range(int(ranges[1][0]), int(ranges[1][1]) + 1):

                    if position not in cant_be_at:
                        cant_be_at[position] = {field['name']}
                    else:
                        cant_be_at[position].add(field['name'])

    from pprint import pprint
    print('\nImpossible:')
    pprint(cant_be_at)

    return cant_be_at


def _get_possible_field_positions(tickets_data, impossible_field_positions):
    # this can be done as roznica zbiorow all_fields - cant_be:

    can_be_at = {}

    for field in tickets_data['fields']:
        for position in range(1, len(tickets_data['fields']) + 1):
            if position not in impossible_field_positions:
                if position not in can_be_at:
                    can_be_at[position] = [field['name']]
                else:
                    can_be_at[position].append(field['name'])
                continue

            if field['name'] not in impossible_field_positions[position]:
                if position not in can_be_at:
                    can_be_at[position] = [field['name']]
                else:
                    can_be_at[position].append(field['name'])

    from pprint import pprint
    print('\nPossible:')
    pprint(can_be_at)

    return can_be_at


def _get_correct_field_positions(tickets_data, possible_field_positions):
    max_ids = {}
    ids = {}  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 15, 3, 3, 1, 1, 3, 0, 4, 8]

    for position, fields in possible_field_positions.items():
        max_ids[position] = len(fields) - 1
        # ids[position] = 0

    min_position = 1
    max_position = max(ids)
    position = max_position

    expected_fields_permutation_count = len(tickets_data['fields'])

    while True:
        ids_permutation = [ids[i] for i in range(min_position, max_position + 1)]
        fields_permutation = [possible_field_positions[i][field_id] for i, field_id in enumerate(ids_permutation, start=1)]

        from pprint import pprint
        print('\nChecking permutation:')
        pprint(ids_permutation)
        pprint(fields_permutation)

        if len(set(fields_permutation)) == expected_fields_permutation_count:

            from pprint import pprint
            print('\nCorrect permutation:')
            pprint(fields_permutation)
            return fields_permutation

        if ids[position] < max_ids[position]:
            ids[position] += 1
        else:
            ids[position] = 0
            position -= 1

            if position < min_position:
                return None

            if ids[position] < max_ids[position]:
                ids[position] += 1
                position = max_position


def _calculate_your_ticket_hash(fields_in_correct_order, your_ticket):
    your_ticket_hash = 1

    for field_id, field_name in enumerate(fields_in_correct_order):
        if field_name.startswith('departure'):
            your_ticket_hash *= int(your_ticket[field_id])

    return your_ticket_hash
