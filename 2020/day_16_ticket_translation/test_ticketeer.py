from ticketeer import calculate_ticket_scanning_error_rate


def test_calculate_ticket_scanning_error_rate():
    assert calculate_ticket_scanning_error_rate('test_input.raw') == 71
