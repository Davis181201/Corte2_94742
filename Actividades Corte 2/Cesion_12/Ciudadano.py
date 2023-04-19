class Ciudadano:
    def __init__(self, nombre: str, edad: int, cc: str):
        self.__nombre = nombre
        self.__edad = edad
        self.__cc = cc

    # ---------- Getters ----------
    def getNombre(self) -> str:
        return self.__nombre

    def getEdad(self) -> int:
        return self.__edad

    def getCc(self) -> str:
        return self.__cc

    # ----------- Setters-----------
    def setNombre(self, nombre: str):
        self.__nombre = nombre
    def setEdad(self, edad: int):
        if edad > 0:
            self.__edad = edad
        else:
            print("Edad inválida")
    def setCc(self, cc: str):
        if len(cc) >= 8 and len(cc) <= 10:
            self.__cc = cc
        else:
            print("Número de cédula inválido")




    #-------- Metodo Mostrar ---------
    def mostrar(self):
        print(f'Nombre: {self.__nombre} - Edad: {self.__edad} - CC: {self.__cc}')
    

    #----------- Metodo es Mayor de edad ----------
    def esMayorDeEdad(self):
        if self.__edad >= 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")

class Astronauta(Ciudadano):
    def __init__(self, nombre: str, edad: int, cc: str, misiones: int, experiencia: str):
        super().__init__(nombre, edad, cc)
        self.misiones = misiones
        self.experiencia= experiencia

    #---------- Getters -------
    def getMisiones(self):
        return self.misiones

    def getExperiencia(self):
        return self.experiencia
    
    #--------- Setters --------
    def setMisiones(self, misiones: int):
        self.misiones = misiones

    def setExperiencia(self, experiencia: str):
        self.experiencia = experiencia

    #-------- Metodo mostrar -------
    def mostrar(self):
        super().mostrar()
        print(f'Misiones: {self.misiones} - Experiencia: {self.experiencia} Años')

    #------- Metodo unico --------
    def realizarMision(self):
        print(f"{self.getNombre()} está realizando una misión espacial.\n")

class ProductorMusica(Ciudadano):
    def __init__(self, nombre: str, edad: int, cc: str, genero: str, l_trabajo: str):
        super().__init__(nombre, edad, cc)
        self.genero = genero
        self.l_trabajo = l_trabajo

    #----------- Getters -------
    def getGenero(self):
        return self.genero
    def getL_trabajo(self):
        return self.l_trabajo
    
    #----------- Setters ---------
    def setGenero(self, genero: str):
        self.genero = genero
    def setL_trabajo(self,l_trabajo: str):
        self.l_trabajo = l_trabajo


    #--------- Metodo mostrar ------
    def mostrar(self):
        super().mostrar()
        print(f'Género: {self.genero} - Lugar de Trabajo: {self.l_trabajo}')
    #--------- Metodo unico -------
    def producirCancion(self):
        print(f"{self.getNombre()} Esta Produciendo una nueva canción\n")

class Aeronautica(Ciudadano):
    def __init__(self, nombre: str, edad: int, cc: str, tipoLicencia: str, horasVuelo: int):
        super().__init__(nombre, edad, cc)
        self.tipoLicencia = tipoLicencia
        self.horasVuelo = horasVuelo

    #------ Getters ------
    def getTipoLicencia(self):
        return self.tipoLicencia

    def getHorasVuelo(self):
        return self.horasVuelo

    #------- Setters -------
    def setTipoLicencia(self, tipoLicencia: str):
        self.tipoLicencia = tipoLicencia

    def setHorasVuelo(self, horasVuelo: int):
        self.horasVuelo = horasVuelo

    #------ Metodo mostrar ----------
    def mostrar(self):
        super().mostrar()
        print(f'Tipo de licencia: {self.tipoLicencia} - Horas de vuelo: {self.horasVuelo}')

    #------- Metodo unico ---------
    def realizarMantenimiento(self, horas: int = None):
        if horas:
            print(f"Realizando mantenimiento en una aeronave por {horas} horas")
        else:
            print("Realizando mantenimiento básico en una aeronave")
    

def main():
    #-----Astronauta-----
    # nombre = input("Ingrese el nombre del astronauta: ")
    # edad = int(input("Ingrese la edad del astronauta: "))
    # cc = input("Ingrese el número de cédula del astronauta: ")
    # misiones = int(input("Ingrese el número de misiones del astronauta: "))
    # experiencia = input("Ingrese la experiencia del astronauta: ")

    # astronauta = Astronauta(nombre, edad, cc, misiones, experiencia)
    astronauta = Astronauta("Neil Armstrong",48,80547994,2,2)
    astronauta.mostrar()
    astronauta.realizarMision()
    
    
    #----- Musico -------
    # nombre = input("Ingrese el nombre del productor musical: ")
    # edad = int(input("Ingrese la edad del productor musical: "))
    # cc = input("Ingrese el número de cédula del productor musical: ")
    # genero = input("Ingrese el género musical del productor: ")
    # l_trabajo = input("Ingrese el lugar de trabajo del productor: ")

    # productor = ProductorMusica(nombre, edad, cc, genero, l_trabajo)
    productor = ProductorMusica("Quincy Jones",45,181592574,"Jazz","Hampton's band")
    productor.mostrar()
    productor.producirCancion()

    # -------Aeronautica------
    
    # nombre = input("Ingrese el nombre del piloto: ")
    # edad = int(input("Ingrese la edad del piloto: "))
    # cc = input("Ingrese el número de cédula del piloto: ")
    # tipoLicencia = input("Ingrese el tipo de licencia del piloto: ")
    # horasVuelo = int(input("Ingrese el número de horas de vuelo del piloto: "))
    # piloto = Aeronautica(nombre, edad, cc, tipoLicencia, horasVuelo)
    piloto = Aeronautica("Erich Hartmann",14,1587024,"piloto aviador",2000)
    piloto.mostrar()
    piloto.realizarMantenimiento()
    piloto.realizarMantenimiento(4)
   

   
    
if __name__ == "__main__":
    main()
