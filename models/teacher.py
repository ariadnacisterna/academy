from datetime import date
from typing import TYPE_CHECKING

from models.person import Person

if TYPE_CHECKING:
    from models.subject import Subject

class Teacher(Person):
    def __init__(
            self, name: str, dob: date, file: int, city: str, 
            street: str, number: int) -> None:
        super().__init__(name, dob, file, city, street, number)
        self.subjects: list['Subject'] = []

    def add_subject(self, subject: 'Subject') -> None:
        self.subjects.append(subject)