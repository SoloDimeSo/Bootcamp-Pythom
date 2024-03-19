from pizza import Pizza


print("Atributos de clase de la clase Pizza:")
print("Ingredientes proteicos posibles:", Pizza.ingredientes_proteicos_posibles)
print("Ingredientes vegetales posibles:", Pizza.ingredientes_vegetales_posibles)
print("Tipos de masa posibles:", Pizza.tipos_de_masa_posibles)


print("\nValidación de elemento 'salsa de tomate' en ['salsa de tomate', 'salsa bbq']:",
    Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))


pizza = Pizza()
pizza.hacer_pedido()


print("\nIngredientes de la pizza:")
print("Ingrediente proteico:", pizza.ingrediente_proteico)
print("Ingredientes vegetales:", pizza.ingrediente_vegetal_1, "y", pizza.ingrediente_vegetal_2)
print("Tipo de masa:", pizza.tipo_de_masa)
print("Es una pizza válida:", pizza.es_valida)
