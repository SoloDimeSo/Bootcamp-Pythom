class Pizza:
    ingredientes_proteicos_posibles = ["pollo", "vacuno", "carne vegetal"]
    ingredientes_vegetales_posibles = ["tomate", "aceitunas", "champiñones"]
    tipos_de_masa_posibles = ["tradicional", "delgada"]

    def __init__(self):
        self.ingrediente_proteico = None
        self.ingrediente_vegetal_1 = None
        self.ingrediente_vegetal_2 = None
        self.tipo_de_masa = None
        self.es_valida = None

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        return elemento in valores_posibles

    def hacer_pedido(self):
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico (pollo, vacuno, carne vegetal): ")
        self.ingrediente_vegetal_1 = input("Ingrese el primer ingrediente vegetal (tomate, aceitunas, champiñones): ")
        self.ingrediente_vegetal_2 = input("Ingrese el segundo ingrediente vegetal (tomate, aceitunas, champiñones): ")
        self.tipo_de_masa = input("Ingrese el tipo de masa (tradicional, delgada): ")

        self.es_valida = self.validar_pedido()

    def validar_pedido(self):
        ingredientes_validos = (
            self.validar_elemento(self.ingrediente_proteico, self.ingredientes_proteicos_posibles) and
            self.validar_elemento(self.ingrediente_vegetal_1, self.ingredientes_vegetales_posibles) and
            self.validar_elemento(self.ingrediente_vegetal_2, self.ingredientes_vegetales_posibles) and
            self.validar_elemento(self.tipo_de_masa, self.tipos_de_masa_posibles)
        )
        return ingredientes_validos


