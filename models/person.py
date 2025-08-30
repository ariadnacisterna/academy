from datetime import date
from models.address import Address

class Person:
    def __init__(self, name: str, dob: date, file: int, city: str, 
                 street: str, number: int) -> None:
        self.name = name
        self.dob = dob
        self.file = file
        self.address = Address(city, street, number)

    @property
    def age(self) -> int:
        today = date.today()
        age = today.year - self.dob.year

        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        
        return age