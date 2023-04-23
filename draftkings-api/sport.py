class Sport:
    def __init__(self, json: dict):
        self.sport_id = json["sportId"]
        self.full_name = json["fullName"]
        self.sort_order = json["sortOrder"]
        self.has_public_contests = json["hasPublicContests"]
        self.is_enabled = json["isEnabled"]
        self.region_full_sport_name = json["regionFullSportName"]
        self.region_abbreviated_sport_name = json["regionAbbreviatedSportName"]
