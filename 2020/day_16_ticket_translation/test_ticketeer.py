from ticketeer import calculate_ticket_scanning_error_rate, get_fields_in_correct_order


def test_calculate_ticket_scanning_error_rate():
    assert calculate_ticket_scanning_error_rate('test_input.raw') == 71


def test_get_fields_in_correct_order():
    assert get_fields_in_correct_order('test_input_2.raw') == ['row', 'class', 'seat']
