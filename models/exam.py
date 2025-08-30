from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.student import Student
    from models.subject import Subject

class Exam:
    def __init__(self, date: date, subject: 'Subject', student: 'Student') -> None:
        self.date = date
        self.subject = subject
        self.student = student