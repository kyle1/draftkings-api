import requests
from typing import List, Optional


class Contest:
    def __init__(self, json):
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


def get_contests(sport: Optional[str] = None):
    url = 'https://www.draftkings.com/lobby/getcontests'
    if sport != None:
        url += f'?sport={sport}'
    response = requests.get(url)
    contests_json = response.json()
    contests: List[Contest] = []
    for contest_json in contests_json['Contests']:
        contest = Contest(contest_json)
        contests.append(contest)
    return contests

contests = get_contests('LOL')