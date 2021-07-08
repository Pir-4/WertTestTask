import random

def positive_test_data():
    """"""
    return [
            {"lon": 100.75, "lat": 1.5, "date": "2014-02-01", "dim": 1.025},
            {"lon": Longitude(), "lat": Latitude()},
            {"lon": 0, "lat": 0},
            {"lon": 0, "lat": 90},
            {"lon": 0, "lat": -90},
            {"lon": -180, "lat": 0},
            {"lon": 180, "lat": 0},
            {"lon": -180, "lat": 90},
            {"lon": -180, "lat": -90},
            {"lon": 180, "lat": 90},
            {"lon": 180, "lat": -90},
            {"lon":  Longitude(), "lat": Latitude(), "date": "2014-02-01"},
            {"lon":  Longitude(), "lat": Latitude(), "date": "2014-02-01", "dim": Dim()},
            {"lon":  Longitude(), "lat": Latitude(), "dim": Dim()},
            {"lon": Longitude(), "lat": Latitude(), "date": "2014-02-01", "cloud_score": False},
            ]

def negative_test_data():
    """"""
    return [{"lon": Longitude()},
            {"lat": Latitude()},
            {"lon": -181, "lat": Latitude()},
            {"lon": 181, "lat": Latitude()},
            {"lon": Longitude(), "lat": 91},
            {"lon": Longitude(), "lat": -91},
            {"lon": "badstr", "lat": Latitude(), "date": "2014-02-01"},
            {"lon": Longitude(), "lat": "badstr", "date": "2014-02-01"},
            {"lon": Longitude(), "lat": Latitude(), "date": "badstr"},
            {"lon": Longitude(), "lat": Latitude(), "date": "2014-02-01", "dim": "badstr"},
            {"lon": Longitude(), "lat": Latitude(), "date": "2014-02-01", "cloud_score": True},
            {"lon": 100.75, "lat": 1.5, "date": "2014-02-01", "dim": Dim(83, 100)},
            ]

def Latitude(start=-90, stop=90):
    return round(random.uniform(start, stop+1), 6)

def Longitude(start=-180, stop=180):
     return round(random.uniform(start, stop+1), 6)

def Dim(start=0.00000000001, stop=82):
        return random.uniform(start, stop+1)
