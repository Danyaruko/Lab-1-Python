
class CarSharing:
    def __init__(self, country = "None", price = 0.0, days = 0, rating = 0, color = "None", seats = 0):
        self.__country = country
        self.__price = price
        self.__days = days
        self.__rating = rating
        self.__color = color
        self.__seats = seats
        print (f"Look, a new option in {self.__country}")
    def __del__(self):
        print (f"Option in {self.__country} closed") 
    def __str__(self):
        return f"""Availability: {self.get_available()}
Country: {self.__country}
Price: {self.__price} Euro  
Days: {self.__days} days
Rating: {self.__rating} of 10
Color: {self.__color}
Seats: {self.__seats} seats\n"""
    def __repr__(self):
        return f"""\nAvailability: {self.get_available()}
Country: {self.__country}
Price: {self.__price} Euro  
Days: {self.__days} days
Rating: {self.__rating} of 10
Color: {self.__color}
Seats: {self.__seats} seats\n"""
    available = True
    @staticmethod
    def get_available():
        return CarSharing.available
