from datetime import date
from typing import TYPE_CHECKING

from models.person import Person

if TYPE_CHECKING:
    from models.career import Career

class Student(Person):
    def __init__(
            self, name: str, dob: date, file: int, city: str, 
            street: str, number: int, career: 'Career') -> None:
        super().__init__(name, dob, file, city, street, number)
        self.career = career