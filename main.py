from ClaseMAnejadorAlumnos import ManejadorAlumno
from claseManejadorMateria import MateriasAprobadas

if __name__=="__main__":
    print('Inicia el programa')
    alumnos=ManejadorAlumno()
    alumnos.inicalizar()
    print("alumnos")
    alumnos.mostrar()
    alumnos.ordenarAlumnos()
    print("alumnos ordenados")
    alumnos.mostrar()
    materia=MateriasAprobadas()
    materia.inicializar()
    print("materias")
    #print(materia)
    print('Termina el programa')
    
