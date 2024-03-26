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
                    return
                
                
    class Restaurante(Tienda):
        pass
            
            
            
    class Supermercado(Tienda):
        def listar_productos(self):
            lista_productos = ""
            for producto in self.__producto:
                stock_info = f"Pocos productos disponibles ({producto.obtener_stock()})" if producto.obtener_stock() < 10 else ""
            lista_productos += f"Nombre: {producto.obtener_nombre()}, Precio: ${producto.obtener_precio()}, {stock_info}\n"
            return lista_productos
            
            
            
    class Farmacia(Tienda):
        def listar_productos(self):
            lista_productos = ""
            for producto in self.__producto:
                envio_gratis = "Envío gratis al solicitar este producto" if producto.obtener_precio() > 15000 else ""
                lista_productos += f"Nombre: {producto.obtener_nombre()}, Precio: ${producto.obtener_precio()}, {envio_gratis}\n"
            return lista_productos
                
            
        
        
        
    