# example of using composition instead of inheritance

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from collections import defaultdict, namedtuple
from typing import Dict, List

# geo point represents latitude and longtitude values
GeoPoint = namedtuple("GeoPoint",['lat','long'])
VRParams = namedtuple("VRParams", ['param1','param2','param3'])


class Route(ABC):
    """Represents route information"""

    @abstractmethod
    def get_route_parameters() -> dict:
        """Get parameters"""
    @abstractmethod
    def compute_route_score() -> int:
        """Compute route score"""

@dataclass
class StandardRoute(Route):
    """Represent standard route"""
    start: GeoPoint
    end: GeoPoint
    length: float
    units: str
    difficulty: int
    country: str    
    
    def get_route_parameters(self) -> dict:
        return {
            "start": self.start,
            "end": self.end,
            "length": self.length,
            "units": self.units,
            "difficulty": self.difficulty,
            "country": self.country
        }
    
    def compute_route_score(self) -> int:
        return self.difficulty

@dataclass
class VRRoute(Route):
    """Represent virtual reality route"""
    start: GeoPoint
    end: GeoPoint
    length: float
    units: str
    difficulty: int
    country: str
    vr_params: VRParams

    def get_route_parameters(self) -> dict:
        return {
            "start": self.start,
            "end": self.end,
            "length": self.length,
            "units": self.units,
            "difficulty": self.difficulty,
            "country": self.country,
            "vr_params": self.vr_params
        }
    
    def compute_route_score(self) -> int:
        return self.difficulty * self.vr_params.param3


class Activity(ABC):
    """Represent base activity interface"""

    @abstractmethod
    def get_attributes() -> dict:
        """Get activity properties"""
    
    @abstractmethod
    def get_activity_points() -> int:
        """Set point for making the activity"""


@dataclass
class RideActivity(Activity):
    """Basic ride activity"""

    duration: int
    route: Route
    ride_id: int
    points_coeff:float = 1

    def get_attributes(self) -> dict:
        return {
            "duration": self.duration,
            "route": self.route,
            "id": self.ride_id
        }
    
    def get_activity_points(self) -> int:
        return (self.duration % 10) * self.points_coeff

@dataclass
class RaceActivity(Activity):
    """Represents race activity."""

    duration: int
    standing: int
    race_id: int
    points_coeff: float = 1.5
    standing_bonus: Dict[int, int] = field(default_factory= lambda : {
        1: 20,
        2: 15,
        3: 10
    })
    bonus_points: int = 2

    def get_attributes(self) -> dict:
        return {
            "duration": self.duration,
            "standing": self.standing,
            "id": self.race_id
        }
    
    def get_activity_points(self) -> int:
        
        if self.standing in self.standing_bonus.keys():
            self.bonus_points = self.standing_bonus[self.standing]
        
        return (self.duration % 10) * self.points_coeff + self.bonus_points

@dataclass
class Rider:
    """Represents information about rider"""

    name: str
    id: int
    activities: List[Activity]

    def add_activity(self, activity: Activity) -> None:
        self.activities.append(activity)

def main():
    
    route_start = GeoPoint(49.08474534713918, 19.591743005940934)
    route_end = GeoPoint(48.97235503231782, 19.583718331869377)

    standard_route = StandardRoute(start=route_start, end=route_end, length=16.76, units="m", difficulty=4, country="SK")
    ride_activity = RideActivity(duration=54, route=standard_route, ride_id=24)

    rider = Rider(name="John", id=42, activities=[])
    rider.add_activity(ride_activity)

    print(f"Rider {rider.name} has {len(rider.activities)} activities.")
    print(f"Rider activities: ")
    for activity in rider.activities:
        print(f"Activity params: {activity.get_attributes()}, points: {activity.get_activity_points()}")

if __name__ == "__main__":
    main()