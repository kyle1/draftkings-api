class GameType:
    # Game type IDs can be found at https://www.draftkings.com/help/rules/
    # by clicking on a game type and viewing the second ID in the URL.
    def __init__(self, json: dict):
        self.game_type_id = json["gameTypeId"]
        self.game_type_name = json["gameTypeName"]
        self.game_type_description = json["gameTypeDescription"]
        self.lineup_configuration_id = json["lineupConfigurationId"]
        self.salary_cap = json["salaryCap"]
        self.game_count = json["gameCount"]
        self.team_count = json["teamCount"]
        self.unique_players = json["uniquePlayers"]
        self.allow_late_swap = json["allowLateSwap"]
        self.lineup_template = [
            LineupTemplateSlot(slot_json) for slot_json in json["lineupTemplate"]
        ]
        self.error_status = json["errorStatus"]
        self.rules_url = json["rulesUrl"]
        self.draft_type = json["draftType"]
        self.allowed_competition_attributes = json["allowedCompetitionAttributes"]
        self.scoring_divider = json["scoringDivider"]
        self.use_optimal_lineups = json["useOptimalLineups"]
        self.supports_players_tab = json["supportsPlayersTab"]
        self.show_bye_week_info = json["showByeWeekInfo"]
        self.glossary_terms = json["glossaryTerms"]
        self.original_draft_type = json["originalDraftType"]
        self.is_season_long = json["isSeasonLong"]
        self.error_codes = json["errorCodes"]


class LineupTemplateSlot:
    def __init__(self, json: dict):
        self.roster_slot = RosterSlot(json["rosterSlot"])
        self.order = json["order"]
        self.scoring_order = json["scoringOrder"]


class RosterSlot:
    def __init__(self, json: dict):
        self.id = json["id"]
        self.name = json["name"]
        self.description = json["description"]
        self.position_tip = json["positionTip"]
        self.position_tip_subtext = json["positionTipSubtext"]
        self.not_scoring = json["notScoring"]
