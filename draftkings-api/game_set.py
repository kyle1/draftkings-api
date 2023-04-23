from competition import Competition
from game_style import GameStyle


class GameSet:
    def __init__(self, json: dict):
        self.game_set_key = json["GameSetKey"]
        self.contest_start_time_suffix = json["ContestStartTimeSuffix"]
        self.competitions = [
            Competition(comp_json) for comp_json in json["Competitions"]
        ]
        self.game_styles = [GameStyle(gs_json) for gs_json in json["GameStyles"]]
        self.sort_order = json["SortOrder"]
        self.min_start_time = json["MinStartTime"]
        self.tag = json["Tag"]
