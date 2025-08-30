from models.student import Student
from models.teacher import Teacher
from models.career import Career
from models.subject import Subject
from models.exam import Exam

class AcademyManagement:
    def __init__(self) -> None:
        self.students: list['Student'] = []
        self.teachers: list['Teacher'] = []
        self.__careers: list['Career'] = []
        self.subjects: list['Subject'] = []
        self.exams: list['Exam'] = []

    def __add_career(self, new_career: 'Career'):
        self.__careers.append(new_career)

    def create_career(self, code: str, name: str) -> Career:
        new_career = Career(code=code, name=name)
        self.__add_career(new_career)
        return new_career

    def create_subject(self, code: str, name: str) -> Subject:
        new_subject = Subject(code=code, name=name)
        self.subjects.append(new_subject)
        return new_subject

    def add_subject_to_career(self, subject: 'Subject', career: 'Career') -> None:
        career.add_subject(subject)
        subject.add_career(career)
