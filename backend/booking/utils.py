from datetime import datetime


def convert_to_iso_format(date_string):
    try:
        parsed_date = datetime.strptime(
                date_string, "%d.%m.%Y"
            ).strftime("%Y-%m-%d")
        return parsed_date
    except (ValueError, TypeError) as e:
        return None
