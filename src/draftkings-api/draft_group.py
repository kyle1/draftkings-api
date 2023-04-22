import requests
from typing import List, Optional


class DraftGroup:
    def __init__(self, json):
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

    
def get_draft_groups(sport: Optional[str] = None):
    url = 'https://www.draftkings.com/lobby/getcontests'
    if sport != None:
        url += f'?sport={sport}'
    response = requests.get(url)
    draft_groups_json = response.json()
    draft_groups: List[DraftGroup] = []
    for dg_json in draft_groups_json['DraftGroups']:
        draft_group = DraftGroup(dg_json)
        draft_groups.append(draft_group)
    return draft_groups

dgs = get_draft_groups('MLB')
for dg in dgs:
    print(dg.draft_group_id)
    print('\n')
