from datetime import datetime as dt

class todoItem:
    def __init__(self, name, date, time):
        self.name = name
        self.date = self.format_date(date)
        self.time = time

    def format_date(self, date):
        date = date.split('/')
        return dt(int(date[2]), int(date[0]), int(date[1]))
    