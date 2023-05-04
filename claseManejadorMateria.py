import csv
from claseMateriasAprobadas import Materia


class MateriasAprobadas:
    __materias = []

    def __init__(self):
        self.__materias = []

    def agregarMateria(self, unaMateria):
        self.__materias.append(unaMateria)

    def inicializar(self):
        archivo = open("materiasAprobadas.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                dni = fila[0]
                nombre = fila[1]
                fecha = fila[2]
                nota = fila[3]
                aprobacion = fila[4]
                unaMateria = Materia(dni, nombre, fecha, nota, aprobacion)
                self.agregarMateria(unaMateria)
        archivo.close()

    def __str__(self):
        
        s = ""
        for materia in self.__materias:
            s += str(materia) +"\n"

        return s
