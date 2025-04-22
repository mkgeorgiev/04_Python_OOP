from project.band_members.singer import Singer
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band import Band
from project.concert import Concert


class ConcertTrackerApp:
    MUSICIAN_TYPES = {"Singer": Singer, "Drummer": Drummer, "Guitarist": Guitarist}
    CONCERT_SKILLS = {"Rock": {"Drummer": ["play the drums with drumsticks"],
                               "Singer": ["sing high pitch notes"],
                               "Guitarist": ["play rock"]},
                      "Metal":{"Drummer": ["play the drums with drumsticks"],
                               "Singer": ["sing low pitch notes"],
                               "Guitarist": ["play metal"]},
                      "Jazz": {"Drummer": ["play the drums with drum brushes"],
                               "Singer": ["sing high pitch notes","sing low pitch notes"],
                               "Guitarist": ["play jazz"]}}

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")
        musician = self._get_musician(name)
        if musician is not None:
            raise Exception(f"{musician.name} is already a musician!")
        new_musician = self._create_new_musician(musician_type, name, age)
        self.musicians.append(new_musician)
        return f"{new_musician.name} is now a {new_musician.__class__.__name__}."

    def create_band(self, name):
        band = self._get_band(name)
        if not band is None:
            raise Exception(f"{band.name} band is already created!")
        new_band = self._create_new_band(name)
        self.bands.append(new_band)
        return f"{new_band.name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self._get_concert(place)
        if not concert is None:
            raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")
        new_concert = self._create_new_concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{new_concert.genre} concert in {new_concert.place} was added."


    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self._get_musician(musician_name)
        band = self._get_band(band_name)
        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")
        if band is None:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        return f"{musician.name} was added to {band.name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self._get_band(band_name)
        musician = self._get_musician(musician_name)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")
        if musician not in band.members:
            raise Exception(f"{musician.name} isn't a member of {band.name}!")
        band.members.remove(musician)
        return f"{musician.name} was removed from {band.name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self._get_band(band_name)
        concert = self._get_concert(concert_place)
        if not self._check_band_members_classes(band_name):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        can_play = self._check_members_skills(band_name,concert_place)
        if not can_play:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")
        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."





    # Helper methods
    def _get_musician(self, name):
        collection = [m for m in self.musicians if m.name == name]
        return collection[0] if collection else None

    def _create_new_musician(self, musician_type, name, age):
        new_musician = self.MUSICIAN_TYPES[musician_type](name, age)
        return new_musician

    def _get_band(self, name):
        collection = [b for b in self.bands if b.name == name]
        return collection[0] if collection else None

    def _create_new_band(self, name):
        new_band = Band(name)
        return new_band

    def _get_concert(self, place: str):
        collection = [c for c in self.concerts if c.place == place]
        return collection[0] if collection else None

    def _create_new_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        return new_concert

    def _check_band_members_classes(self, band_name):
        band = self._get_band(band_name)
        contains_signer = any(isinstance(member, Singer) for member in band.members)
        contains_drummer = any(isinstance(member, Drummer) for member in band.members)
        contains_guitarist = any(isinstance(member, Guitarist) for member in band.members)
        return True if contains_signer and contains_guitarist and contains_drummer else False

    def _check_members_skills(self, band_name, concert_place):
        band = self._get_band(band_name)
        concert = self._get_concert(concert_place)
        concert_type = concert.genre
        can_play = False
        for type_of_concert in self.CONCERT_SKILLS:
            if type_of_concert == concert_type:
                for member in band.members:
                    for musician in self.CONCERT_SKILLS[type_of_concert]:
                        if member.__class__.__name__ == musician:
                            can_play = False
                            for skill in  self.CONCERT_SKILLS[type_of_concert][musician]:
                                if skill in member.skills:
                                    can_play = True
                                else:
                                    return False
        if can_play:
            return True




