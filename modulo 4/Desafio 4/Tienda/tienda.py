from producto import Producto

class Tienda:
    def __init__(self, nombre_tienda, costo_delivery):
        self.__nombre_tienda = nombre_tienda
        self.__costo_delivery = costo_delivery
        self.__producto = []
        
        
    def ingresar_producto(self, arg_producto):
        for p in self.__producto:
            if p.obtener_nombre() == arg_producto.get_nombre():
                p.set_obtener_stock(p.obtener_stock() + arg_producto.obtener_stock())
                break
            else:
                self.__producto.append(arg_producto)
        
    def listar_productos(self):
        lista = ""
        for linea in self.__producto:
            linea += str(linea)+ "\n"
            return lista
        
    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.__producto:
            if producto.obtener_nombre() == nombre_producto:
                if producto.obtener_stock() < cantidad:
                    cantidad = producto.obtener_stock
    