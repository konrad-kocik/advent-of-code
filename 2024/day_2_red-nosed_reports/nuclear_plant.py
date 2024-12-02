from typing import List

Level = int
Report = List[Level]
Reports = List[Report]


def count_safe_reports(input_file_path: str) -> int:
    reports = _get_reports(input_file_path)
    reports_evaluations = _evaluate_reports(reports)
    return reports_evaluations.count('safe')


def _get_reports(input_file_path: str) -> Reports:
    reports = []

    with open(input_file_path, 'r') as file:
        for line in file:
            reports.append([int(level) for level in line.strip().split()])

    return reports


def _evaluate_reports(reports: Reports) -> List[str]:
    reports_evaluations = []

    for report in reports:
        report_evaluation = 'safe'

        for level_id, level in enumerate(report):
            if level_id < len(report) - 1:
                next_level = report[level_id + 1]
            else:
                break

            if level == next_level:
                report_evaluation = 'unsafe'
                break
            elif abs(level - next_level) >= 4:
                report_evaluation = 'unsafe'
                break
            elif level_id >= 1:
                previous_level = report[level_id - 1]
                trend_to_previous_level = 'increasing' if level - previous_level > 0 else 'decreasing'
                trend_to_next_level = 'increasing' if next_level - level > 0 else 'decreasing'
                if trend_to_next_level != trend_to_previous_level:
                    report_evaluation = 'unsafe'
                    break

        reports_evaluations.append(report_evaluation)

    return reports_evaluations
