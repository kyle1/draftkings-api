import requests


class GameType:
    def __init__(self, id: int):
        json = self._get_game_type(id)
        self.game_type_id = json['gameTypeId']
        self.game_type_name = json['gameTypeName']
        self.game_type_description = json['gameTypeDescription']
        self.lineup_configuration_id = json['lineupConfigurationId']
        self.salary_cap = json['salaryCap']
        self.game_count = json['gameCount']
        self.team_count = json['teamCount']
        self.unique_players = json['uniquePlayers']
        self.allow_late_swap = json['allowLateSwap']
        self.lineup_template = [LineupTemplateSlot(slot_json) for slot_json in json['lineupTemplate']]

    def _get_game_type(self, id: int) -> dict:
        response = requests.get(f'https://api.draftkings.com/lineups/v1/gametypes/{id}/rules')
        return response.json()


class LineupTemplateSlot:
    def __init__(self, json: dict):
        self.roster_slot = RosterSlot(json['rosterSlot'])
        self.order = json['order']
        self.scoring_order = json['scoringOrder']


class RosterSlot:
    def __init__(self, json: dict):
        self.id = json['id']
        self.name = json['name']
        self.description = json['description']
        self.position_tip = json['positionTip']
        self.position_tip_subtext = json['positionTipSubtext']
        self.not_scoring = json['notScoring']