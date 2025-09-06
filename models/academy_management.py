from models.student import Student
from models.teacher import Teacher
from models.career import Career
from models.subject import Subject
from models.exam import Exam
from datetime import date


class AcademyManagement:
    def __init__(self) -> None:
        self._students: list['Student'] = []
        self._teachers: list['Teacher'] = []
        self._careers: list['Career'] = []
        self._subjects: list['Subject'] = []
        self._exams: list['Exam'] = []

    def __add_career(self, new_career: 'Career'):
        self._careers.append(new_career)

    def create_career(self, code: str, name: str) -> Career:
        new_career = Career(code=code, name=name)
        self.__add_career(new_career)
        return new_career

    def create_subject(self, code: str, name: str) -> Subject:
        new_subject = Subject(code=code, name=name)
        self._subjects.append(new_subject)
        return new_subject

    def add_subject_to_career(self, subject: 'Subject', career: 'Career') -> None:
        career._add_subject(subject)
        subject._add_career(career)
    
    def enroll_student(self, name: str, dob: date, state: str, city: str, street: str, number: str, zip_code: str, file_no: str, career: Career) -> Student:
        new_student = Student(name, dob, state, city, street, number, zip_code, file_no, career)
        self._add_student(new_student)
        return new_student
    
    def hire_teacher(self, name: str, dob: date, state: str, city: str, street: str, number: str, zip_code: str) -> Teacher:
        new_teacher = Teacher(name, dob, state, city, street, number, zip_code)
        self._add_teacher(new_teacher)
        return new_teacher
    
    def assign_subject_to_teacher(self, subject: 'Subject', teacher: 'Teacher') -> None:
        subject._add_teacher(teacher)
        teacher._add_subject(subject)
    
    @property
    def teachers(self) -> list['Teacher']:
        return self._teachers

    @property
    def careers(self) -> list['Career']:
        return self._careers
    
    @property
    def subjects(self) -> list['Subject']:
        return self._subjects
    
    @property
    def students(self) -> list['Student']:
        return self._students
    
    def _add_subject(self, *new_subjects: 'Subject') -> None:
        for new_subject in new_subjects:
            self._subjects.append(new_subject)
    
    def _add_student(self, *new_students: 'Student') -> None:
        for new_student in new_students:
            self._students.append(new_student)
    
    def _add_teacher(self, *new_teachers: 'Teacher') -> None:
        for new_teacher in new_teachers:
            self._teachers.append(new_teacher)