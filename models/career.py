from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.subject import Subject

class Career:
    def __init__(self, code: str, name: str, 
                 subjects: list['Subject'] | None = None) -> None:
        self.code = code
        self.name = name
        self.__subjects = subjects if subjects else []

    def add_subject(self, *new_subjects: 'Subject') -> None:
        for new_subject in new_subjects:
            self.__subjects.append(new_subject)

    @property
    def subjects(self) -> str:
        return ','.join([str(subject) for subject in self.__subjects])
    
    def __str__(self) -> str:
        return f'{self.code}: {self.name}'