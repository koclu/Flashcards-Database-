import json
from os import name


class Users:

    def __init__(self, name="Name", level=1, totaltime=0):
        self.name = name
        self.level = level
        self.totaltime = totaltime

    @classmethod
    def readjson_user(cls):
        with open("users.json") as f:
            cls.users_dict = json.load(f)

    @classmethod
    def save_to_json(cls, self):
        """data is stored as in the example : {
        "omer": {
            "level": 7
        },
        "yusuf": {
            "level": 4
        },
        "ayse": {
            "level": 1
        }
        }"""
        cls.readjson_user()
        cls.users_dict[self.name] = {
            "level": self.level, "totaltime": self.totaltime}
        with open("users.json", "w") as f:
            json.dump(cls.users_dict, f, indent=2)

    def checkname(self):
        for names in Users.users_dict.keys():
            if self.name == names:
                return True
   # --------------------------About Level----------------------------

    def readjsonword(self):
        with open("words.json") as f:
            self.wordsdata = json.load(f)
        self.wordsid = [i for i in range(1, len(self.wordsdata.keys()))]

    def get_level_id(self):
        self.readjsonword()
        self.levelid = self.wordsid[(self.level*20)-20:self.level*20]
        return self.levelid

    def levelcheck(self):
        if len(self.levelid) == 0:
            self.level += 1
            Users.save_to_json(self)
            self.get_level_id()

    def totalprogress(self):
        # turns %
        self.readjsonword()
        return (self.level * 100) / (len(self.wordsid)/20)
    # ----------------------About Game ---------------------------------


"""    def play(self):
        for id in self.get_level_words():
            print(self.wordsdata[str(id)]["Dutch"])"""

"""
isim = Users("omer", 7)
for id in isim.get_level_words():
    print(isim.wordsdata[str(id)]["Dutch"])
"""
isim = Users("faruk", 2)
