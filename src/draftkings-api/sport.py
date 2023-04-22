import requests
from typing import List


class Sport:
    def __init__(self, json):
        self.sport_id: None
        self.full_name: None
        self.sort_order: None
        self.has_public_contests: None
        self.is_enabled: None
        self.region_full_sport_name: None
        self.region_abbreviated_sport_name: None

        self._json_to_obj(json)

    def __str__(self):
        return f'{self.sport_id} {self.full_name}'

    def _json_to_obj(self, json: dict):
        self.sport_id = json['sportId']
        self.full_name = json['fullName']
        self.sort_order = json['sortOrder']
        self.has_public_contests = json['hasPublicContests']
        self.is_enabled = json['isEnabled']
        self.region_full_sport_name = json['regionFullSportName']
        self.region_abbreviated_sport_name = json['regionAbbreviatedSportName']


def get_sports() -> List[Sport]:
    response = requests.get("https://api.draftkings.com/sites/US-DK/sports/v1/sports?format=json")
    sports_json = response.json()
    sports: List[Sport] = []
    for sport_json in sports_json['sports']:
        sport = Sport(sport_json)
        sports.append(sport)
    return sports
