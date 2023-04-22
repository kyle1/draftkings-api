import requests
from typing import List, Optional


class DraftGroup:
    def __init__(self, json: dict):
        self.draft_group_id = json['DraftGroupId']
        self.contest_type_id = json['ContestTypeId']
        self.start_date = json['StartDate']
        self.start_date_est = json['StartDateEst']
        self.sort_order = json['SortOrder']
        self.draft_group_tag = json['DraftGroupTag']
        self.game_type_id = json['GameTypeId']
        self.game_type = json['GameType']
        self.sport_sort_order = json['SportSortOrder']
        self.sport = json['Sport']
        self.game_count = json['GameCount']
        self.contest_start_time_suffix = json['ContestStartTimeSuffix']
        self.contest_start_time_type = json['ContestStartTimeType']
        self.games = json['Games']
        self.draft_group_series_id = json['DraftGroupSeriesId']
        self.game_set_key = json['GameSetKey']
        self.allow_ugc = json['AllowUGC']

    
def get_draft_groups(sport: Optional[str] = None) -> List[DraftGroup]:
    url = 'https://www.draftkings.com/lobby/getcontests'
    if sport != None:
        url += f'?sport={sport}'
    response = requests.get(url)
    draft_groups_json: dict = response.json()['DraftGroups']
    draft_groups: List[DraftGroup] = [DraftGroup(json) for json in draft_groups_json]
    return draft_groups
