class Table:
    def __init__(self,table_number):
        self.table_number = table_number
        self.table_status = ' NOT OCCUPIED '
        self.charge = 0.0
        # To track multiple sessions change self.session to an array
        self.session = None

    def __repr__(self):
        return (f" {self.table_number} \n {self.table_status}\n")

class Session:
    def __init__(self):
        self.start_time = 'TEST     '
        self.display_start = '     '
        self.table_end = '     '
        self.display_end = '     '
        self.time_played = '      '
        self.time_played_hours = '  '
        self.time_played_minutes = '  '
        self.display_played = '      '