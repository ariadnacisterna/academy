from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.exam import Exam
    from models.career import Career
    from models.teacher import Teacher

class Subject:
    def __init__(self, code: str, name: str) -> None:
        self._code = code
        self._name = name
        self._exams: list['Exam'] = []
        self._careers: list['Career'] = []
        self._teachers: list['Teacher'] = []

    def _add_teacher(self, teacher: 'Teacher') -> None:
        self._teachers.append(teacher)

    def _add_career(self, career: 'Career') -> None:
        self._careers.append(career)
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        self._name = value
    
    @property
    def code(self) -> str:
        return self._code
    
    @code.setter
    def code(self, value: str) -> None:
        self._code = value
    
    @property
    def careers(self) -> list['Career']:
        return self._careers

    @property
    def teachers(self) -> list['Teacher']:
        return self._teachers

    def __str__(self) -> str:
        return f'{self._code}: {self._name}'