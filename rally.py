
class Rally:

    what_else = "None"

    def __init__(self, country = "None", price_euro = 0.0, duration_days = 0, theme = "None", length_km = 0.0, participants = 0):
        self.__country = country
        self.__price_euro = price_euro
        self.__duration_days = duration_days
        self.__theme = theme
        self.__length_km = length_km
        self.__participants = participants
        print (f"Look, a new option in {self.__country}")

    def __del__(self):
        print (f"Option in {self.__country} closed") 

    def __str__(self):
        return f"Special requirements: {self.get_what_else()}\n"\
               f"Country: {self.__country}\n"\
               f"Price: {self.__price_euro} Euro\n"\
               f"Duration: {self.__duration_days} days\n"\
               f"Dedicated to: {self.__theme}\n"\
               f"Length: {self.__length_km} km\n"\
               f"Number of participants: {self.__participants}\n"

    def __repr__(self):
        return f"Special requirements: {self.get_what_else()}\n"\
               f"Country: {self.__country}\n"\
               f"Price: {self.__price_euro} Euro\n"\
               f"Duration: {self.__duration_days} days\n"\
               f"Dedicated to: {self.__theme}\n"\
               f"Length: {self.__length_km} km\n"\
               f"Number of participants: {self.__participants}\n"

    @staticmethod
    def get_what_else():
        return Rally.what_else
