import requests
from typing import List


class Sport:
    def __init__(self, json: dict):
        self.sport_id = json['sportId']
        self.full_name = json['fullName']
        self.sort_order = json['sortOrder']
        self.has_public_contests = json['hasPublicContests']
        self.is_enabled = json['isEnabled']
        self.region_full_sport_name = json['regionFullSportName']
        self.region_abbreviated_sport_name = json['regionAbbreviatedSportName']


def get_sports() -> List[Sport]:
    response = requests.get('https://api.draftkings.com/sites/US-DK/sports/v1/sports?format=json')
    sports_json: dict = response.json()['sports']
    sports: List[Sport] = [Sport(json) for json in sports_json]
    return sports
