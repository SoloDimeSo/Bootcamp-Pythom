class Producto:
    def __init__(self, nombre, precio, stock= 0):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock
        
    @property
    def obtener_nombre(self):
        return self._nombre
    
    @property
    def obtener_precio(self):
        return self._precio
    
    @property
    def obtener_stock(self):
        return self.obtener_stock
    
    @obtener_stock.setter
    def obtener_stock(self, cantidad):
        if cantidad < 0: 
            self._stock = 0
        else:
            self._stock = cantidad
            
    def __str__(self):
        return f" Producto: {self.obtener_nombre}     Precio: {self.obtener_precio}     Stock:{self.obtener_stock}"   
    
    
    
        