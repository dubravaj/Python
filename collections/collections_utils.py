import logging
from collections import namedtuple
from geopy.geocoders import Nominatim
from geopy.distance import geodesic, great_circle
# collections datatypes 
# geographic point holding latitude and longtitude values 
GeoPoint = namedtuple("GeoPoint", ['lat','long'])
# amino acid holding abbreviation of the amino acid and its full name 
AminoAcid = namedtuple("AminoAcid", ['abbr', 'full_name'])

logger = logging.getLogger()
logger.setLevel(logging.INFO)

locator = Nominatim(user_agent="geo_app")

def get_address(geo_point: GeoPoint) -> str:
    """Get address of geographical point"""

    point = f"{geo_point.lat}, {geo_point.long}"
    location = locator.reverse(point)
    logger.info(f"Address of point ({geo_point.lat},{geo_point.long}) is: {location.address}")

    return location.address 

def get_distance(point1: GeoPoint, point2: GeoPoint, units="km") -> float:
    """Get distance between two geographical points"""

    distance = geodesic(point1, point2)
    address1 = get_address(point1)
    address2 = get_address(point2)

    if units == "km":
        distance = distance.km
    else:
        distance = distance.miles
    
    print(f"Distance between {address1} and {address2} is {format(distance, '.2f')} {units}")

    return distance