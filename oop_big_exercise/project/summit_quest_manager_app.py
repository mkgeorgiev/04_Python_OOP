from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBER_TYPES = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    VALID_PEAK_TYPES = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."
        climber = self._get_climber(climber_name)
        if climber is not None:
            return f"{climber.name} has been already registered."
        new_climber = self._create_climber(climber_type, climber_name)
        self.climbers.append(new_climber)
        return f"{new_climber.name} is successfully registered as a {new_climber.__class__.__name__}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAK_TYPES:
            return f"{peak_type} is an unknown type of peak."
        new_peak = self._create_peak(peak_type, peak_name, peak_elevation)
        self.peaks.append(new_peak)
        return f"{new_peak.name} is successfully added to the wish list as a {new_peak.__class__.__name__}."

    def check_gear(self, climber_name: str, peak_name: str, gear: list):
        climber = self._get_climber(climber_name)
        peak = self._get_peak(peak_name)
        recommended_gear = set(peak.RECOMMENDED_GEAR)
        climber_gear = set(gear)
        missing_gear = recommended_gear - climber_gear
        if missing_gear: #### problem here
            climber.is_prepared = False

            return f"{climber.name} is prepared to climb {peak.name}."
        missing_gear = self._check_missing_gear(peak, gear)
        return f"{climber.name} is not prepared to climb {peak.name}. " \
               f"Missing gear: {', '.join(missing_gear)}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self._get_climber(climber_name)
        peak = self._get_peak(peak_name)
        if climber is None:
            return f"Climber {climber_name} is not registered yet."
        if peak is None:
            return f"Peak {peak_name} is not part of the wish list."
        if climber.is_prepared and climber.can_climb():
            climber.climb(peak)
            peak.is_conquered = True
            return f"{climber.name} conquered {peak.name} whose difficulty level is {peak.difficulty_level}."
        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        if not climber.can_climb():
            climber.rest()
            return f"{climber.name} needs more strength to climb {peak.name} and is therefore taking some rest."

    def get_statistics(self):
        successful_climbers = self._get_climbers_who_conquered()
        sorted_successful_climbers = self._sort_successful_climbers(successful_climbers)
        conquered_peaks = [p for p in self.peaks if p.is_conquered]
        result = f"Total climbed peaks: {len(conquered_peaks)}"
        if sorted_successful_climbers:
            result +="\n**Climber's statistics:**"+ '\n' + '\n'.join(str(climber) for climber in sorted_successful_climbers)
        return result

    # Helper methods
    def _get_climber(self, climber_name):
        collection = [c for c in self.climbers if c.name == climber_name]
        return collection[0] if collection else None

    def _create_climber(self, climber_type, climber_name):
        for type_of_climber in self.VALID_CLIMBER_TYPES:
            if type_of_climber == climber_type:
                new_climber = self.VALID_CLIMBER_TYPES[type_of_climber](climber_name)
                return new_climber

    def _get_peak(self, peak_name):
        collection = [p for p in self.peaks if p.name == peak_name]
        return collection[0] if collection else None

    def _create_peak(self, peak_type: str, peak_name: str, peak_elevation: int):
        for type_of_peak in self.VALID_PEAK_TYPES:
            if type_of_peak == peak_type:
                new_peak = self.VALID_PEAK_TYPES[type_of_peak](peak_name, peak_elevation)
                return new_peak

    def _check_missing_gear(self, peak, climber_gear):
        missing_gear = []
        for gear in peak.RECOMMENDED_GEAR:
            if gear not in climber_gear:
                missing_gear.append(gear)

        sorted_miss_gear = sorted(missing_gear)
        return sorted_miss_gear

    def _get_climbers_who_conquered(self):
        successful_climbers = []
        for climber in self.climbers:
            if climber.conquered_peaks and climber not in successful_climbers:
                successful_climbers.append(climber)
        return successful_climbers

    def _sort_successful_climbers(self, successful_climbers):
        sorted_climbers = sorted(successful_climbers, key=lambda x: (-len(x.conquered_peaks), x.name))
        for climber in sorted_climbers:
            if len(climber.conquered_peaks) > 1:
                climber.conquered_peaks.sort(key=lambda x: x.name)
        return sorted_climbers


climbing_app = SummitQuestManagerApp()

print(climbing_app.register_climber("ArcticClimber", "Alice"))
print(climbing_app.register_climber("SummitClimber", "Bob"))
print(climbing_app.register_climber("SummitClimber", "Alice"))
print(climbing_app.register_climber("SummitClimber", "Charlie"))

print(climbing_app.peak_wish_list("ArcticPeak", "MountEverest", 4000))
print(climbing_app.peak_wish_list("SummitPeak", "K2", 3000))
print(climbing_app.peak_wish_list("ArcticPeak", "Denali", 2500))
print(climbing_app.peak_wish_list("UnchartedPeak", "MysteryMountain", 2000))

print(climbing_app.check_gear("Alice", "MountEverest", ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]))
print(climbing_app.check_gear("Bob", "K2", ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]))
print(climbing_app.check_gear("Charlie", "Denali", ["Ice axe", "Crampons"]))

print(climbing_app.perform_climbing("Alice", "MountEverest"))
print(climbing_app.perform_climbing("Bob", "K2"))
print(climbing_app.perform_climbing("Charlie", "MysteryMountain"))
print(climbing_app.perform_climbing("Eve", "MountEverest"))

print(climbing_app.get_statistics())

