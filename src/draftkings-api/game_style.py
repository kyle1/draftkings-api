class GameStyle:
    def __init__(self, json: dict):
        self.game_style_id = json['GameStyleId']
        self.sport_id = json['SportId']
        self.sort_order = json['SortOrder']
        self.name = json['Name']
        self.abbreviation = json['Abbreviation']
        self.description = json['Description']
        self.is_enabled = json['IsEnabled']
        self.attributes = json['Attributes']