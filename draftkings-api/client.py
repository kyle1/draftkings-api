import requests
from typing import List, Optional

from contest import Contest, ContestDetail
from draftable import Draftable
from game_type import GameType
from sport import Sport


TIMEOUT_SECONDS = 1


class DraftKingsClient:
    def __init__(self):
        self._session = requests.Session()

    def get_sports(self) -> List[Sport]:
        response = self._session.get(
            url="https://api.draftkings.com/sites/US-DK/sports/v1/sports",
            params={"format": "json"},
            timeout=TIMEOUT_SECONDS,
        )
        sports_json = response.json()["sports"]
        sports = [Sport(json) for json in sports_json]
        return sports

    def get_game_type(self, id: int) -> GameType:
        response = self._session.get(
            url=f"https://api.draftkings.com/lineups/v1/gametypes/{id}/rules",
            timeout=TIMEOUT_SECONDS,
        )
        game_type_json = response.json()
        game_type = GameType(game_type_json)
        return game_type

    def get_contests(
        self, sport: Optional[str] = None, as_json: bool = False
    ) -> List[Contest] | dict:
        response = self._session.get(
            url="https://www.draftkings.com/lobby/getcontests",
            params={"sport": sport},
            timeout=TIMEOUT_SECONDS,
        )
        contests_json = response.json()["Contests"]
        if as_json:
            return contests_json
        contests = [Contest(json) for json in contests_json]
        return contests

    def get_contest_detail(self, id: int) -> ContestDetail:
        response = self._session.get(
            url=f"https://api.draftkings.com/contests/v1/contests/{id}",
            params={"format": "json"},
            timeout=TIMEOUT_SECONDS,
        )
        contest_json = response.json()["contestDetail"]
        contest = ContestDetail(contest_json)
        return contest

    def get_draftables(
        self, draft_group_id: int, as_json: bool = False
    ) -> List[Draftable]:
        response = self._session.get(
            url=f"https://api.draftkings.com/draftgroups/v1/draftgroups/{draft_group_id}/draftables",
            timeout=TIMEOUT_SECONDS,
        )
        draftables_json = response.json()["draftables"]
        if as_json:
            return draftables_json
        draftables = [Draftable(json) for json in draftables_json]
        return draftables
