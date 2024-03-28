from error import DimensionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        try:
            if ancho < 1 or ancho > self.MAX:
                raise DimensionError("** El ancho", ancho, self.MAX)
            self.__ancho = ancho
        except DimensionError as e:
            print(e)

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        try:
            if alto < 1 or alto > self.MAX:
                raise DimensionError("** El alto", alto, self.MAX)
            self.__alto = alto  
        except DimensionError as e:
            print(e)


foto1 = Foto(100,200,"mis fotos.jpg")
print(foto1.alto)
print(foto1.ancho)

try:
    foto1.ancho = 600
    foto1.alto = 800
except:
    print()
    
finally:
    print(f"El tamaño de su foto es: {foto1.ancho} x {foto1.alto}")