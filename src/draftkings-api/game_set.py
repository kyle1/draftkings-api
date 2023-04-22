import requests
from typing import List, Optional

from competition import Competition
from game_style import GameStyle


class GameSet:
    def __init__(self, json: dict):
        self.game_set_key = json['GameSetKey']
        self.contest_start_time_suffix = json['ContestStartTimeSuffix']
        self.competitions = [Competition(comp_json) for comp_json in json['Competitions']]
        self.game_styles = [GameStyle(gs_json) for gs_json in json['GameStyles']]
        self.sort_order = json['SortOrder']
        self.min_start_time = json['MinStartTime']
        self.tag = json['Tag']

  
def get_game_sets(sport: Optional[str] = None) -> List[GameSet]:
    url = 'https://www.draftkings.com/lobby/getcontests'
    if sport != None:
        url += f'?sport={sport}'
    response = requests.get(url)
    game_sets_json: dict = response.json()['GameSets']
    game_sets: List[GameSet] = [GameSet(json) for json in game_sets_json]
    return game_sets