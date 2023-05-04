from ClaseAlumno import Alumno
import numpy as np
import csv

class ManejadorAlumno:
    __cantidad=0
    __dimension=0
    __incremento=5

    def __init__(self,dimension=1, incremento=5):
        self.__alumnos=np.empty(dimension,dtype=Alumno)
        self.__dimension=dimension
        self.__cantidad=0

    def agregarAlumno(self,unAlumno):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__alumnos.resize(self.__dimension)

        self.__alumnos[self.__cantidad]=unAlumno
        self.__cantidad+=1

    def inicalizar(self):
        print("inicializar")
        archivo=open("alumnos.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                dni=fila[0]
                apellido=fila[1]
                nombre=fila[2]
                carrera=fila[3]
                anio=fila[4]
                unAlumno=Alumno(dni,apellido,nombre,carrera,anio)
                self.agregarAlumno(unAlumno)
        archivo.close()

    def mostrar(self):
        for i in range(self.__cantidad):
            self.__alumnos[i].mostrar()
            
            
            
    def ordenarAlumnos(self):
        intercambio=True
        while intercambio:
            intercambio=False
            for i in range(len(self.__alumnos) -1):
                print(self.__alumnos[i])
                print("i={}".format(i))
                print(self.__alumnos[i+1])
                if (self.__alumnos[i]>self.__alumnos[i+1]):
                    self.__alumnos[i],self.__alumnos[i+1]=self.__alumnos[i+1],self.__alumnos[i]
                    intercambio=True

