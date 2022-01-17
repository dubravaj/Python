# dataclasses example
from dataclasses import asdict, dataclass, field
from operator import itemgetter

@dataclass
class Movie:
    name: str
    director: str
    year: int
    rating: float = field(default=0)
    reviews: dict[int,tuple[float, str]] = field(default_factory=dict, repr=False)

    def get_user_review(self, user_id: int) -> str:
        try:
            return self.reviews[user_id]
        except KeyError:
            print(f'User {user_id} not found.')
    
    def add_new_user_review(self, user_id: int, rating_review: tuple[float, str]) -> None:
        self.reviews.update({user_id: rating_review})
    
    
    def compute_overall_rating(self) -> None:
        rating = 0.0
        for (key, val) in self.reviews.items():
            rating += itemgetter(0)(val)
        self.rating = rating / len(self.reviews)

    def serialize(self) -> dict:
        return asdict(self)


if __name__ == "__main__":

    m = Movie(name="Matrix: Ressurections", director="Lana Wachowski", year=2021)
    m.add_new_user_review(1, (9.5, "Great! "))
    m.add_new_user_review(2, (7.2, "Overall good movie, but I previous ones cannot be compared to that."))
    m.compute_overall_rating()
    print(m.rating)
    print(m.serialize())
