from typing import Tuple, List

Page = int
Rule = Tuple[Page, Page]
Rules = List[Rule]
Update = List[Page]
Updates = List[Update]


def add_up_middle_page_numbers_from_correct_updates(input_file_path: str) -> int:
    rules, updates = _get_rules_and_updates(input_file_path)
    correct_updates = _get_correct_updates(rules, updates)
    return _add_up_middle_pages(correct_updates)


def _get_rules_and_updates(input_file_path: str) -> Tuple[Rules, Updates]:
    rules = []
    updates = []
    section = 'rules'

    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if not line:
                section = 'updates'
            elif section == 'rules':
                before, after = line.split('|')
                rules.append((int(before), int(after)))
            elif section == 'updates':
                updates.append([int(page) for page in line.split(',')])

    return rules, updates


def _get_correct_updates(rules: Rules, updates: Updates) -> Updates:
    correct_updates = []

    for update in updates:
        update_correct = True

        for page_id in range(0, len(update)):
            page = update[page_id]
            pages_before = update[:page_id]
            pages_after = update[page_id + 1:]
            pages_that_must_be_before = _get_rules_before(page, rules)
            pages_that_must_be_after = _get_rules_after(page, rules)
            pages_before_are_correct = _check_if_pages_are_correct(pages_before, pages_that_must_be_after)
            pages_after_are_correct = _check_if_pages_are_correct(pages_after, pages_that_must_be_before)

            if not pages_before_are_correct or not pages_after_are_correct:
                update_correct = False
                break

        if update_correct:
            correct_updates.append(update)

    return correct_updates


def _get_rules_before(page: Page, rules: Rules) -> List[Page]:
    return [rule[0] for rule in rules if rule[1] == page]


def _get_rules_after(page: Page, rules: Rules) -> List[Page]:
    return [rule[1] for rule in rules if rule[0] == page]


def _check_if_pages_are_correct(pages: List[int], rules: List[int]) -> bool:
    incorrect_pages = [page for page in pages if page in rules]
    return True if not incorrect_pages else False


def _add_up_middle_pages(updates: Updates) -> int:
    middle_pages = [update[int(len(update) / 2)] for update in updates]
    return sum(middle_pages)
