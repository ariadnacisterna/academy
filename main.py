import os
import sys
from datetime import date
from models.academy_management import AcademyManagement
from tui.state import InitialMenu, Menu

class AcademyApp:
    def __init__(self):
        self.menu: Menu = InitialMenu()
        
    def mainLoop(self):
        try:
            while True:
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')

                self.menu = self.menu.execute()
        except KeyboardInterrupt:
            sys.exit()

def main() -> None:
    try:
        AcademyApp().mainLoop()
    except AttributeError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
        print('Ha ocurrido un error. Programa terminado.')

if __name__ == "__main__":
    academy = AcademyManagement()

    systems = academy.create_career(code='SIST001', name='Ingeniería en Sistemas')
    civil = academy.create_career(code="CIV002", name="Ingeniería Civil")
    
    programming = academy.create_subject(code='prog', name='Programación')
    mathematics = academy.create_subject(code="mat", name="Análisis Matemático 1")
    
    academy.add_subject_to_career(subject=programming, career=systems)
    academy.add_subject_to_career(subject=mathematics, career=systems)
    academy.add_subject_to_career(subject=mathematics, career=civil)
    
    math_teacher = academy.hire_teacher(name="Juan Pérez", dob=date(1980, 5, 15), state="Buenos Aires", city="CABA", street="Corrientes", number="1234", zip_code="C1043AAZ") 
    programming_teacher = academy.hire_teacher(name="José López", dob=date(1970, 6, 15), state="Tucumán", city="TUC", street="Córdoba", number="1234", zip_code="C1043ABZ")
    
    academy.assign_subject_to_teacher(subject=mathematics, teacher=math_teacher)
    academy.assign_subject_to_teacher(subject=programming, teacher=programming_teacher)
    
    student1 = academy.enroll_student(name="Ana García", dob=date(2000, 8, 20), state="Buenos Aires", city="CABA", street="Santa Fe", number="5678", zip_code="C1425BGH", file_no="EST001", career=systems)
    student2 = academy.enroll_student(name="Carlos Pérez", dob=date(1999, 3, 15), state="Córdoba", city="CBA", street="Belgrano", number="890", zip_code="X5000ABC", file_no="EST002", career=systems)
    student3 = academy.enroll_student(name="José Martínez", dob=date(1998, 7, 5), state="Mendoza", city="MZA", street="Las Heras", number="123", zip_code="M5500GHI", file_no="EST004", career=civil)
    student4 = academy.enroll_student(name="Laura Sánchez", dob=date(2000, 11, 25), state="Tucumán", city="TUC", street="24 de Septiembre", number="789", zip_code="T4000JKL", file_no="EST005", career=civil)
    
    Menu.academy_active = academy
    main()