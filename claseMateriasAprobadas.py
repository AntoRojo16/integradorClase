class Materia:
    __dni=0
    __nombre=""
    __fecha=0
    __nota=0
    __aprobacion=""
    
    
    def __init__ (self,dni,nombre,fecha,nota,aprobacion):
        self.__dni=dni
        self.__nombre=nombre
        self.__fecha=fecha
        self.__nota=nota
        self.__aprobacion=aprobacion
        
        
        
    def __str__(self):
        return("dni {},nombre {},fecha {}, nota {}, aprobacion {}".format(self.__dni,self.__nombre,self.__fecha,self.__nota,self.__aprobacion))
        
        
    