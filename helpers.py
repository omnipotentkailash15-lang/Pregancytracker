from datetime import date, timedelta


def calculate_week(lmp_date: date) -> int:
    """Calculate gestational week from LMP date."""
    days = (date.today() - lmp_date).days
    week = days // 7
    return max(1, min(week, 40))


def get_trimester(week: int) -> int:
    if week <= 13:
        return 1
    elif week <= 26:
        return 2
    else:
        return 3


def get_days_remaining(lmp_date: date) -> int:
    edd = lmp_date + timedelta(weeks=40)
    remaining = (edd - date.today()).days
    return max(0, remaining)
