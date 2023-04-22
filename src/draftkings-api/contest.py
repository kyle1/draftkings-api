import requests
from typing import List, Optional


class Contest:
    def __init__(self, json: dict):
        self.uc = json['uc']
        self.ec = json['ec']
        self.mec = json['mec']
        self.fpp = json['fpp']
        self.s = json['s']
        self.n = json['n']
        self.attr = json['attr']
        self.nt = json['nt']
        self.m = json['m']
        self.a = json['a']
        self.po = json['po']
        self.pd = json['pd']
        self.tix = json['tix']
        self.sdstring = json['sdstring']
        self.sd = json['sd']
        self.id = json['id']
        self.tmpl = json['tmpl']
        self.pt = json['pt']
        self.so = json['so']
        self.ftw = json['fwt']
        self.is_owner = json['isOwner']
        self.start_time_type = json['startTimeType']
        self.dg = json['dg']
        self.ulc = json['ulc']
        self.cs = json['cs']
        self.game_type = json['gameType']
        self.ssd = json['ssd']
        self.dgpo = json['dgpo']
        self.cso = json['cso']
        self.ir = json['ir']
        self.rl = json['rl']


class ContestDetail:
    def __init__(self, id: int):
        response = requests.get(f'https://api.draftkings.com/contests/v1/contests/{id}?format=json')
        json = response.json()['contestDetail']

        self.contest_summary = json['contestSummary']
        self.payout_summary = [PayoutSummaryTier(ps_json) for ps_json in json['payoutSummary']]
        self.payout_description = json['PayoutDescription']
        self.is_cash_prize_only = json['IsCashPrizeOnly']
        self.scoring_style_id = json['scoringStyleId']
        self.contest_state_detail = json['contestStateDetail']
        self.sport = json['sport']
        self.is_guaranteed = json['isGuaranteed']
        self.is_private = json['isPrivate']
        self.is_resizable = json['isResizable']
        self.was_resized = json['wasResized']
        self.exclusions = json['exclusions']
        self.accepted_tickets = json['acceptedTickets']
        self.payout_descriptions = json['payoutDescriptions']
        self.payout_description_metadata = json['payoutDescriptionMetadata']
        self.fpp_award = json['fppAward']
        self.sort_order = json['sortOrder']
        self.filters = json['filters']
        self.contest_start_time = json['contestStartTime']
        self.game_type_id = json['gameTypeId']
        self.ticket_only_entry = json['ticketOnlyEntry']
        self.game_set_key = json['gameSetKey']
        self.contest_key = json['contestKey']
        self.name = json['name']
        self.draft_group_id = json['draftGroupId']
        self.play_type_id = json['playTypeId']
        self.entries = json['entries']
        self.maximum_entries = json['maximumEntries']
        self.maximum_entries_per_user = json['maximumEntriesPerUser']
        self.entry_fee = json['entryFee']
        self.crown_amount = json['crownAmount']
        self.total_payouts = json['totalPayouts']
        self.contest_state = json['contestState']
        self.attributes = json['attributes']


class PayoutSummaryTier:
    def __init__(self, json: dict):
        self.min_position = json['minPosition']
        self.max_position = json['maxPosition']
        self.tier_payout_descriptions = json['tierPayoutDescriptions']
        self.payoutDescriptions = json['payoutDescriptions']


def get_contests(sport: Optional[str] = None) -> List[Contest]:
    url = 'https://www.draftkings.com/lobby/getcontests'
    if sport != None:
        url += f'?sport={sport}'
    response = requests.get(url)
    contests_json: dict = response.json()
    contests: List[Contest] = [Contest(json) for json in contests_json]
    return contests