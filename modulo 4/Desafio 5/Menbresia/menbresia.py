from abc import ABC, abstractclassmethod
import sys

menbresias = {
        1: "basica",
        2: "familiar",
        3:  "sin conexion",
        4:  "pro"
}


class Menbresia(ABC): #clase abstratacta
    def __init__(self, correo_suscriptor, nro_tarjeta) -> None:
        self.__correo_suscriptor = correo_suscriptor 
        self.__nro_tarjeta = nro_tarjeta 
        
    @property
    def correo_suscriptor(self):
        return self.__correo_suscriptor # Para poder obtener este valor desde cualquier parte del programa cuando se llame
    
    @property
    def __nro_tarjeta(self):
        return self.__nro_tarjeta # Para poder obtener este valor desde cualquier parte del programa cuando se llame
    
    @abstractclassmethod
    def cambiar_suscripcion(self):
        pass
    
    def _crear_nva_menbresia(self, nva_menbresia): # Este metodo es "protected", y se identifica poniendo un _ antes de su nombre.
        if nva_menbresia == 1:
            print("Bienvenido a su suscripción: **BASICA**")
            return Basica(self.correo_suscriptor, self.__nro_tarjeta) # Acá estamos haciendo agregación
        elif nva_menbresia == 2:
            print("Bienvenido a su suscripción: **FAMILIAR**")
            return Familiar(self.correo_suscriptor, self.__nro_tarjeta) # Acá estamos haciendo agregación
        elif nva_menbresia == 3:
            print("Bienvenido a su suscripción: **SIN CONEXION**")
            return Sin_conexion(self.correo_suscriptor, self.__nro_tarjeta) # Acá estamos haciendo agregación
        elif nva_menbresia ==4:
            print("Bienvenido a su suscripción: **PRO**")
            return Pro(self.correo_suscriptor, self.__nro_tarjeta) # Acá estamos haciendo agregación
        else:
            print("No se reconoce menbresia")
            sys.exit(1) #Este comando termina la ejecucion del programa... Se debe importar sys
            
class Gratis(Menbresia): # Esta es la clase solicta del diagrama
    costo = 0
    dispositivo = 1
    def __init__(self, correo_suscriptor, nro_tarjeta) -> None: 
        super().__init__(correo_suscriptor, nro_tarjeta)
        print("... SU SUSCRIPCION ES GRATUITA...:/")
    
    def cambiar_suscripcion(self, nva_menbresia):
        
        if nva_menbresia in [1,2,3,4]:
            return self._crear_nva_menbresia(nva_menbresia)
        else:
            return self
        
class Basica(Menbresia): # Es la que esta al lado de la solita y hereda menbresia
    costo = 3000
    dispositivo = 2
    
    def __init__(self, correo_suscriptor, nro_tarjeta) -> None: #Trae los datos de la clase abstracta o base (menbresia)
        super().__init__(correo_suscriptor, nro_tarjeta)
        if isinstance(self, Familiar) or isinstance(self, Sin_conexion): # Acá estamos preguntando si el objeto o instancia pertenece a la clase "Familiar" o "Sin_conexion"
            self.__dias_gratis = 7 #Para hacer una variable protected se debe utilizar __(2)
        elif isinstance(self, Pro):
            self.__dias_gratis = 15

    def cancelar_suscripcion(self): #cuando llamemos a cancelar suscripcion cen esta clase, se bajará a "gratis". esto es "agregacion"
        return Gratis (self.correo_suscriptor, self.__nro_tarjeta)

        
    def cambiar_suscripcion(self, nva_menbresia): # acá estamos en la mebresia basica, por lo que el cambio deberá realizarse desde la 2 a la 4 que son menbresias mayores
        if nva_menbresia in [2,3,4]:
            return self._crear_nva_menbresia(nva_menbresia)
        else:
            return self       
        
class Familiar(Basica): # esta hereda de la clase anterior "Basica" que hereda de la abstracta "menbresia"
    corto = 5000
    dispositivo = 5
    
        
    def cambiar_suscripcion(self, nva_menbresia): # acá estamos cambiando de menbresia 
        if nva_menbresia in [1,3,4]:
            return self._crear_nva_menbresia(nva_menbresia)
        else:
            return self      
        
    def control_parental(self):
        pass

    
class Sin_conexion(Menbresia): # esta hereda de la clase anterior "familiar" que hereda de la abstracta "menbresia"
    costo = 3500
    dispositivo = 2
    
        
    def cambiar_suscripcion(self, nva_menbresia): # acá estamos cambiando de menbresia 
        if nva_menbresia in [1,2,4]:
            return self._crear_nva_menbresia(nva_menbresia)
        else:
            return self
        
    def contenido_max(self):
        pass
    

class Pro(Menbresia):
    costo = 7000
    dispositivo = 6
    
        
    def cambiar_suscripcion(self, nva_menbresia): # acá estamos cambiando de menbresia 
        if nva_menbresia in [1,2,4]:
            return self._crear_nva_menbresia(nva_menbresia)
        else:
            return self
        
    #def main():
    #    pass
    
    #if __name__ == "__main__":
    #    main()
        
g = Gratis("correo@correo.cl, 4520 2050 23")

print(type(g))
print("Costo de Suscripción:", g.costo)
print("Dispositivos Permitidos:", g.dispositivo)

b = g.cambiar_suscripcion(1)
print(type(b))
print("Costo de Suscripción:", b.costo)
print("Dispositivos Permitidos:", b.dispositivo)

f = b.cambiar_suscripcion(2)
print(type(b))
print("Costo de Suscripción:", f.costo)
print("Dispositivos Permitidos:", f.dispositivo)

f = f.cambiar_suscripcion(1)
print(type(b))
print("Costo de Suscripción:", f.costo)
print("Dispositivos Permitidos:", f.dispositivo)

f = f.cambiar_suscripcion(4)
print(type(b))
print("Costo de Suscripción:", f.costo)
print("Dispositivos Permitidos:", f.dispositivo)

#vamos a cancelar la suscripcion del usuario "f" en este momento es "Pro"... por concecuencia, nos deberia dejar en el gratis

f = f.cancelar_suscripcion()
print("Costo de Suscripción:", f.costo)
print("Dispositivos Permitidos:", f.dispositivo)


