class Te():
    duracion = 365
    
    def ___init__(self, sabor , formato):
        self.sabor = sabor
        self.formato = formato
        
    @staticmethod 
    def obtener_tiempo_y_recomendacion(sabor):
        if sabor == 1: #Te Negro
            tiempo = 3 
            recomendacion = "El te negro se recomienda Desayuno"
        elif sabor == 2: #Te verde
            tiempo = 5
            recomendacion = "El te verde se recomienda almuerzo"
        elif sabor == 3: #Te de Hierbas
            tiempo = 6
            recomendacion = "El te de hierbas se recomienda para el atardecer"
        return tiempo, recomendacion
        
    @staticmethod   
    def obtener_precio(formato):
        if formato == 300: #gramos
            precio = 3000
        elif formato == 500: #gramos
            precio = 5000
        return precio
    
    def obtener_sabor(self):
        if self.sabor == 1:
            texto = "Te Negro"
        elif self.sabor == 2:
            texto = "Te Verde"
        elif self.sabor == 3:
            texto = "Te de Hierbas"
        return texto    
        