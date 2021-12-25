import csv
import pathlib
from itertools import combinations
from collections_utils import (
    GeoPoint,
    get_distance,
    create_mapping,
    chain_map_to_dict,
    most_common,
)

if __name__ == "__main__":

    filepath = pathlib.Path(__file__).parent.joinpath("points.csv")
    # read geo points from csv file
    with open(filepath, "r") as points_file:
        locations = map(GeoPoint._make, csv.reader(points_file))

        # get all combinations of points in csv
        locations_pairs = list(combinations(locations, 2))

        for location_pair in locations_pairs:
            distance = get_distance(location_pair[0], location_pair[1])

    # chain map example
    base_mapping = {
        "interpret": "Linkin Park",
        "city": "Aguora Hills",
        "state": "California",
    }
    genres_mapping = {
        "genres": [
            "alternative rock",
            "nu-metal",
            "rap rock",
            "electronic rock",
            "pop rock",
        ]
    }
    discography_mapping = {
        "albums": [
            ("Hibrid Theory", "2000"),
            ("Meteora", "2003"),
            ("Minutes to Midnight", "2007"),
            ("A Thousand Suns", "2010"),
            ("Living Things", "2012"),
            ("The Hunting Party", "2014"),
            ("One More Light", "2017"),
        ]
    }

    full_info = create_mapping(base_mapping, genres_mapping, discography_mapping)
    full_map = chain_map_to_dict(full_info)
    print(full_map)

    # counter example

    # insuline amino acid sequence
    PROTEIN = "MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSL\
    QPLALEGSLQKRGIVEQCCTSICSLYQLENYCN"
    # get 5 most common amino acids in the sequence
    most_common_amino_acids = most_common(PROTEIN, 5)
