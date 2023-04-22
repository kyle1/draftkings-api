import requests
from typing import List


class Draftable:
    def __init__(self, json: dict):
        self.draftable_id = json['draftableId']
        self.first_name = json['firstName']
        self.last_name = json['lastName']
        self.display_name = json['displayName']
        self.short_name = json['shortName']
        self.player_id = json['playerId']
        self.player_dk_id = json['playerDkId']
        self.position = json['position']
        self.roster_slot_id = json['rosterSlotId']
        self.salary = json['salary']
        self.status = json['status']
        self.is_swappable = json['isSwappable']
        self.is_disabled = json['isDisabled']
        self.news_status = None if 'newsStatus' not in json else json['newsStatus']
        self.player_image_50 = json['playerImage50']
        self.player_image_160 = json['playerImage160']
        self.alt_player_image_50 = json['altPlayerImage50']
        self.alt_player_image_160 = json['altPlayerImage160']
        self.competition = json['competition']
        self.competitions = json['competitions']
        self.draft_stat_attributes = json['draftStatAttributes']
        self.player_attributes = json['playerAttributes']
        self.team_league_season_attributes = json['teamLeagueSeasonAttributes']
        self.player_game_attributes = json['playerGameAttributes']
        self.team_id = json['teamId']
        self.team_abbreviation = json['teamAbbreviation']
        self.draft_alerts = json['draftAlerts']
        self.player_game_has = json['playerGameHash']


def get_draftables(draft_group_id) -> List[Draftable]:
    response = requests.get(f'https://api.draftkings.com/draftgroups/v1/draftgroups/{draft_group_id}/draftables')
    draftables_json = response.json()['draftables']
    draftables = [Draftable(json) for json in draftables_json]
    return draftables