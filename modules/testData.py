import random
from datetime import datetime, timedelta

def positive_earth_get_test_data():
    """ Generate params for earth GET request

    :return: list of dict with earth get params
    :rtype: list
    """
    return [
            {"lon": 100.75, "lat": 1.5, "date": "2014-02-01", "dim": 1.025},#example
            {"lon": gen_lon(), "lat": gen_lat()},
            {"lon": 0, "lat": 0},
            {"lon": 0, "lat": 90},
            {"lon": 0, "lat": -90},
            {"lon": -180, "lat": 0},
            {"lon": 180, "lat": 0},
            {"lon": -180, "lat": 90},
            {"lon": -180, "lat": -90},
            {"lon": 180, "lat": 90},
            {"lon": 180, "lat": -90},
            {"lon":  gen_lon(), "lat": gen_lat(), "date": gen_date()},
            {"lon":  gen_lon(), "lat": gen_lat(), "dim": gen_dim()},
            {"lon":  gen_lon(), "lat": gen_lat(), "date": gen_date(), "dim": gen_dim()},
            {"lon": gen_lon(), "lat": gen_lat(), "date": gen_date(), "cloud_score": False},
            ]

def negative_earth_get_test_data():
    """ Generate negative params for earth GET request

    :return: list of dict with earth get params
    :rtype: list
    """
    return [{"lon": gen_lon()},
            {"lat": gen_lat()},
            {"lon": -181, "lat": gen_lat()},
            {"lon": 181, "lat": gen_lat()},
            {"lon": gen_lon(), "lat": 91},
            {"lon": gen_lon(), "lat": -91},
            {"lon": "badstr", "lat": gen_lat(), "date": gen_date()},
            {"lon": gen_lon(), "lat": "badstr", "date": gen_date()},
            {"lon": gen_lon(), "lat": gen_lat(), "date": "badstr"},
            {"lon": gen_lon(), "lat": gen_lat(), "date": gen_date(), "dim": "badstr"},
            {"lon": gen_lon(), "lat": gen_lat(), "date": gen_date(), "cloud_score": True},
            {"lon": 100.75, "lat": 1.5, "date": gen_date(), "dim": gen_dim(83, 100)},
            {"lon": 100.75, "lat": 1.5, "date": gen_date(), "dim": gen_dim(-10, 0)},
            {"lon": gen_lon(), "lat": gen_lat(), "date": "1970-01-01"},
            {"lon": gen_lon(), "lat": gen_lat(), "date": gen_date("more")},
            {"lon": gen_lon(), "lat": gen_lat(), "date": gen_date("less")},
            {"lon": 100.75, "lat": 1.5, "date": gen_date(dateformat="%Y-%d-%m"), "dim": 1.025}
            ]

def gen_lat(start=-90, stop=90):
    """ Generate Latitude

    :param start: min limit of possible range
    :type start: float
    :param stop: max limit of possible range
    :type stop: float
    :return: random value from range
    :rtype: float
    """
    return round(random.uniform(start, stop), 6)

def gen_lon(start=-180, stop=180):
    """ Generate Longitude

    :param start: min limit of possible range
    :type start: float
    :param stop: max limit of possible range
    :type stop: float
    :return: random value from range
    :rtype: float
    """
    return round(random.uniform(start, stop), 6)

def gen_dim(start=0.00000000001, stop=82):
    """ Generate width and height of image in degrees

    :param start: min limit of possible range
    :type start: float
    :param stop: max limit of possible range
    :type stop: float
    :return: random value from range
    :rtype: float
    """
    return random.uniform(start, stop)

def gen_date(mode="normal", dateformat="%Y-%m-%d"):
    """ Generate date string line "2014-01-01"

    :param mode: mode of generating random date
                 normal - between "2014-01-01" and current date
                 more - between tomorrow and next year
                 less - between "1900-01-01" and "2013-12-31"
    :type mode: str
    :param dateformat: output format date
    :type dateformat: str
    :return: str of date format like "%Y-%m-%d"
    :rtype: str
    """
    end_date = datetime.now()
    start_date = datetime(2014, 1, 1)
    if mode == "more":
        start_date = end_date + timedelta(days=1)
        end_date = end_date + timedelta(days=365)
    elif mode == "less":
        end_date = end_date - timedelta(days=1)
        start_date = datetime(1900, 1, 1)

    time_between_dates = end_date - start_date
    random_number_of_days = random.randrange(time_between_dates.days)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.strftime(dateformat)
