from datetime import date
from typing import TYPE_CHECKING

from models.person import Person

if TYPE_CHECKING:
    from models.subject import Subject

class Teacher(Person):
    def __init__(self, name: str, dob: date, state: str, city: str, street: str, number: str, zip_code: str) -> None:
        super().__init__(name, dob, state, city, street, number, zip_code)
        self._subjects: list['Subject'] = []

    def _add_subject(self, subject: 'Subject') -> None:
        self._subjects.append(subject)
    
    @property
    def subjects(self) -> list['Subject']:
        return self._subjects
    
    def __str__(self) -> str:
        return self._name