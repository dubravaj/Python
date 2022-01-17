# Python classes
# usage of instance methods
# usage of class method
import json
from typing import Tuple


class Segment:
    """Segment represents part of the route"""

    def __init__(self, start_lat: float, start_long: float, end_lat: float, end_long: float):
        self.start_lat = start_lat
        self.start_long = start_long
        self.end_lat = end_lat
        self.end_long = end_long

    def get_coordinates(self) -> Tuple[float, float, float, float]:
        """Get start and end coordinates"""
        return self.start_lat, self.start_long, self.end_lat, self.end_long

    @classmethod
    def from_json(cls, filename: str):
        """Create segment from JSON"""
        with open(filename, "r") as f:
            segment_json = json.load(f)
            segment_start = segment_json["segmentStart"]
            segment_end = segment_json["segmentEnd"]
            segment = cls(segment_start["lat"], segment_start["long"], segment_end["lat"], segment_end["long"])
            return segment


class Route:
    """Route class represent one route with many segments"""

    segments = []

    def add_segment(self, segment: Segment) -> None:
        """
            Add new segment
        Args:
            segment new segment
        """
        self.segments.append(segment)


if __name__ == "__main__":
    segment = Segment.from_json("segment.json")
    route = Route()
    route.add_segment(segment)
