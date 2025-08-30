from models.academy_management import AcademyManagement

if __name__ == "__main__":
    academia = AcademyManagement()
    ...
    #academia.run()
    ingenieria = academia.create_career(code='ing', name='Ingeniería')
    programacion = academia.create_subject(code='prog', name='Programación')
    academia.add_subject_to_career(subject=programacion, career=ingenieria)
    programacion.careers = []
    print(programacion.careers)
    print(ingenieria.subjects)