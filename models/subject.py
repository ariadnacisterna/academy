from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.exam import Exam
    from models.career import Career
    from models.teacher import Teacher

class Subject:
    def __init__(self, code: str, name: str) -> None:
        self.code = code
        self.name = name
        self.exams: list['Exam'] = []
        self.careers: list['Career'] = []
        self.teachers: list['Teacher'] = []

    def add_teacher(self, teacher: 'Teacher') -> None:
        self.teachers.append(teacher)

    def add_career(self, career: 'Career') -> None:
        self.careers.append(career)

    def __str__(self) -> str:
        return f'{self.code}: {self.name}'