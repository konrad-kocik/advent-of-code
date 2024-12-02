from typing import List

Level = int
Report = List[Level]
Reports = List[Report]


def count_safe_reports(input_file_path: str, problem_dampener: bool = False) -> int:
    reports = _get_reports(input_file_path)
    reports_evaluations = _evaluate_reports(reports, problem_dampener)
    return reports_evaluations.count('safe')


def _get_reports(input_file_path: str) -> Reports:
    reports = []

    with open(input_file_path, 'r') as file:
        for line in file:
            reports.append([int(level) for level in line.strip().split()])

    return reports


def _evaluate_reports(reports: Reports, problem_dampener: bool) -> List[str]:
    reports_evaluations = []

    for report in reports:
        report_evaluation = _evaluate_report(report)

        if report_evaluation == 'unsafe' and problem_dampener:
            for level in report:
                adjusted_report = report.copy()
                adjusted_report.remove(level)
                if _evaluate_report(adjusted_report) == 'safe':
                    report_evaluation = 'safe'
                    break

        reports_evaluations.append(report_evaluation)

    return reports_evaluations


def _evaluate_report(report: Report) -> str:
    for level_id, level in enumerate(report):
        if level_id >= 1:
            previous_level = report[level_id - 1]
        else:
            continue

        if level == previous_level:
            return 'unsafe'
        elif abs(level - previous_level) >= 4:
            return 'unsafe'
        elif level_id >= 2:
            trend = 'increasing' if level - previous_level > 0 else 'decreasing'
            previous_trend = 'increasing' if report[level_id - 1] - report[level_id - 2] > 0 else 'decreasing'
            if trend != previous_trend:
                return 'unsafe'

    return 'safe'
