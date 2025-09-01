from datetime import date
from typing import TYPE_CHECKING

from models.person import Person

if TYPE_CHECKING:
    from models.career import Career

class Student(Person):
    def __init__(self, name: str, dob: date, state: str, city: str, street: str, number: str, zip_code: str, file_no: str, career: 'Career') -> None:
        super().__init__(name, dob, state, city, street, number, zip_code)
        self._file_no = file_no
        self._career = career

    @property
    def file_no(self) -> str:
        return self._file_no

    @property
    def career(self) -> 'Career':
        return self._career