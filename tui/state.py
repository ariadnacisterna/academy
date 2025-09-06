import sys
import time
from models.academy_management import AcademyManagement

class Menu:
    academy_active: None = None
    message: str = ''
    def execute(self):
        raise NotImplementedError()
    
class InitialMenu(Menu):
    def execute(self):
        Menu.message = ''
        print('Bienvenido a la facultad\n')
        print('1. Gestionar estudiantes')
        print('2. Gestionar profesores')
        print('3. Gestionar carreras')
        print('4. Gestionar materias')
        print('5. Salir')
        option = input('\nIngrese una opción: ')
        match option:
            case '1':
                return StudentMenu()
            case '2':
                return TeacherMenu()
            case '3':
                return CareerMenu()
            case '4':
                return SubjectMenu()
            case '5':
                return EndMenu()
            case _:
                print('Opción inválida')
                return self

class StudentMenu(Menu):
    def execute(self):
        print(f"ESTUDIANTES ({len(Menu.academy_active.students)}):")
        for student in Menu.academy_active.students:
            print(f"    {student._name} (Legajo: {student.file_no})")
            print(f"        Edad: {student.age}")
            print(f"        Carrera: {student.career}")
        input("\nPresiona Enter para continuar.")
        return InitialMenu()

class TeacherMenu(Menu):
    def execute(self):
        print(f"PROFESORES ({len(Menu.academy_active.teachers)}):")
        for teacher in Menu.academy_active.teachers:
            print(f"    {teacher._name}")
            print(f"        Enseña: {[str(s) for s in teacher.subjects]}")
        input("\nPresiona Enter para continuar.")
        return InitialMenu()

class CareerMenu(Menu):
    def execute(self):
        print(f"CARRERAS ({len(Menu.academy_active.careers)}):")
        for career in Menu.academy_active.careers:
            print(f"    {career}")
            print(f"        Materias: {[str(s) for s in career.subjects]}") 
        input("\nPresiona Enter para continuar.")
        return InitialMenu()

class SubjectMenu(Menu):
    def execute(self):
        print(f"MATERIAS ({len(Menu.academy_active.subjects)}):")
        for subject in Menu.academy_active.subjects:
            print(f"    {subject}")
            print(f"        En carreras: {[str(c) for c in subject.careers]}")
            print(f"        Profesores: {[str(t) for t in subject.teachers]}")     
        input("\nPresiona Enter para continuar.")
        return InitialMenu()

class EndMenu(Menu):
    def execute(self):
        print("Hasta pronto")
        Menu.academy_active = None
        sys.exit()

if __name__ == "__main__":
    academy = AcademyManagement()