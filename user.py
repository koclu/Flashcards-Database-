from os import name


class Users:

    def __init__(self, name="Name", level=1, totaltime=0):
        self.name = name
        self.level = level
        self.totaltime = totaltime
        self.atOnce = 0
        self.Attempts = 0
