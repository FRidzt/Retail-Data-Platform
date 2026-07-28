import random

from datetime import datetime, timedelta


def random_date(start_date, end_date):

    start = datetime.strptime(
        start_date,
        "%Y-%m-%d"
    )

    end = datetime.strptime(
        end_date,
        "%Y-%m-%d"
    )

    delta = end - start

    random_days = random.randint(
        0,
        delta.days
    )

    return (
        start
        +
        timedelta(days=random_days)
    ).strftime("%Y-%m-%d")