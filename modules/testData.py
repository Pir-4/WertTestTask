import random
from datetime import datetime, timedelta

def positive_test_data():
    """"""
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

def negative_test_data():
    """"""
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
            ]

def gen_lat(start=-90, stop=90):
    """"""
    return round(random.uniform(start, stop), 6)

def gen_lon(start=-180, stop=180):
    """"""
    return round(random.uniform(start, stop), 6)

def gen_dim(start=0.00000000001, stop=82):
    """"""
    return random.uniform(start, stop)

def gen_date(mode="normal"):
    """"""
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
    return random_date.strftime("%Y-%m-%d")
