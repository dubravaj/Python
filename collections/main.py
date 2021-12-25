import csv
import pathlib
from itertools import combinations
from collections_utils import GeoPoint,get_distance

if __name__ == "__main__":

    filepath = pathlib.Path(__file__).parent.joinpath("points.csv")
    # read geo points from csv file
    with open(filepath, 'r') as points_file:
        locations = map(GeoPoint._make, csv.reader(points_file))
    
        # get all combinations of points in csv
        locations_pairs = list(combinations(locations,2))

        for location_pair in locations_pairs:
            distance = get_distance(location_pair[0], location_pair[1])
