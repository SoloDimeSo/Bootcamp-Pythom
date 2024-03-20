from pizza import Pizza


print("Atributos de clase de la clase Pizza:")
print("Carnes posibles:", Pizza.ingredientes_proteicos_posibles)
print("Vegetales posibles:", Pizza.ingredientes_vegetales_posibles)
print("Tipos de masa posibles:", Pizza.tipos_de_masa_posibles)


print("\n Validacion de Salsas:  'salsa de tomate' en ['salsa de tomate', 'salsa barbecue']:",
    Pizza.pizza_valida("salsa de tomate", ["salsa de tomate", "salsa barbecue"]))


pizza = Pizza()
pizza.hacer_pedido()


print("\nIngredientes de la pizza:")
print("Carnes: ", pizza.ingrediente_proteico)
print("Vegetales: ", pizza.ingrediente_vegetal_1, "y", pizza.ingrediente_vegetal_2)
print("Masa: ", pizza.tipo_de_masa)
print("Es una pizza válida:", pizza.es_valida)
