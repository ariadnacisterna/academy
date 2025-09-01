from datetime import date
from models.address import Address

class Person:
    def __init__(self, name: str, dob: date, state: str, city: str, street: str, number: str, zip_code: str) -> None:
        self._name = name
        self._dob = dob
        self.address = Address(state, city, street, number, zip_code)

    @property
    def age(self) -> int:
        today = date.today()
        age = today.year - self._dob.year

        if (today.month, today.day) < (self._dob.month, self._dob.day):
            age -= 1
        
        return age