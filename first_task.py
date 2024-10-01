from datetime import datetime, timedelta

datetime_package = [(datetime(2020, 1, 1), datetime(2020, 1, 7)), (datetime(2020, 1, 15), datetime(2020, 2, 7))]


def generate_range_dates(start_date, end_date) -> list:
    first_date = min(start_date, end_date)
    second_date = max(start_date, end_date)

    dates = [first_date]

    while first_date < second_date:
        first_date += timedelta(days=1)
        dates.append(first_date)

    return dates


def datetime_unpackaging(dt_package) -> None:
    for datetime_elem in dt_package:
        start_date, end_date = datetime_elem
        dates = generate_range_dates(start_date, end_date)

        for date in dates:
            print(date)


datetime_unpackaging(datetime_package)
