from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.subject import Subject

class Career:
    def __init__(self, code: str, name: str, subjects: list['Subject'] | None = None) -> None:
        self._code = code
        self._name = name
        self.__subjects = subjects if subjects else []

    def _add_subject(self, *new_subjects: 'Subject') -> None:
        for new_subject in new_subjects:
            self.__subjects.append(new_subject)

    @property
    def subjects(self) -> list:
        return self.__subjects
    
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
    def teachers(self) -> list['Teacher']:
        return self._teachers

    @property
    def careers(self) -> list['Career']:
        return self._careers
    
    def __str__(self) -> str:
        return f'{self._code}: {self._name}'