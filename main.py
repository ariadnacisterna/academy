from models.academy_management import AcademyManagement
from datetime import date

if __name__ == "__main__":
    academia = AcademyManagement()

    sistemas = academia.create_career(code='sist', name='Ingeniería en Sistemas')
    civil = academia.create_career(code="civil", name="Ingeniería Civil")
    
    programacion = academia.create_subject(code='prog', name='Programación')
    matematica = academia.create_subject(code="mat", name="Análisis Matemático 1")
    
    academia.add_subject_to_career(subject=programacion, career=sistemas)
    academia.add_subject_to_career(subject=matematica, career=sistemas)
    academia.add_subject_to_career(subject=matematica, career=civil)
    
    profesor_mat = academia.hire_teacher("Juan Pérez", date(1980, 5, 15), "Buenos Aires", "CABA", "Corrientes", "1234", "C1043AAZ") 
    profesor_prog = academia.hire_teacher("José López", date(1970, 6, 15), "Tucumán", "TUC", "Córdoba", "1234", "C1043ABZ")
    
    academia.assign_subject_to_teacher(matematica, profesor_mat)
    academia.assign_subject_to_teacher(programacion, profesor_prog)
    
    estudiante1 = academia.enroll_student("Ana García", date(2000, 8, 20), "Buenos Aires", "CABA", "Santa Fe", "5678", "C1425BGH", "EST001", sistemas)
    estudiante2 = academia.enroll_student("Carlos Pérez", date(1999, 3, 15), "Córdoba", "CBA", "Belgrano", "890", "X5000ABC", "EST002", sistemas)
    estudiante3 = academia.enroll_student("José Martínez", date(1998, 7, 5), "Mendoza", "MZA", "Las Heras", "123", "M5500GHI", "EST004", civil)
    estudiante4 = academia.enroll_student("Laura Sánchez", date(2000, 11, 25), "Tucumán", "TUC", "24 de Septiembre", "789", "T4000JKL", "EST005", civil)
    
    print("\n" + "="*20)
    print("     FACULTAD")
    print("="*20)

    print(f"\nCARRERAS ({len(academia.careers)}):")
    for carrera in academia.careers:
        print(f"    {carrera}")
        print(f"        Materias: {[str(s) for s in carrera.subjects]}")
    
    print(f"\nCódigo de {sistemas._name} antes: {sistemas.code}")
    sistemas.code = "SIST001"
    print(f"Código de {sistemas._name} después: {sistemas.code}")
    
    print(f"\nCódigo de {civil._name} antes: {civil.code}")
    civil.code = "CIV002"
    print(f"Código de {civil._name} después: {civil.code}")

    print(f"\nMATERIAS ({len(academia.subjects)}):")
    for materia in academia.subjects:
        print(f"    {materia}")
        print(f"        En carreras: {[str(c) for c in materia.careers]}")
        print(f"        Profesores: {[str(t) for t in materia.teachers]}")

    print(f"\nPROFESORES ({len(academia.teachers)}):")
    for profesor in academia.teachers:
        print(f"    {profesor._name}")
        print(f"        Enseña: {[str(s) for s in profesor.subjects]}")

    print(f"\nESTUDIANTES ({len(academia.students)}):")
    for estudiante in academia.students:
        print(f"    {estudiante._name} (Legajo: {estudiante.file_no})")
        print(f"        Edad: {estudiante.age}")
        print(f"        Carrera: {estudiante.career}")