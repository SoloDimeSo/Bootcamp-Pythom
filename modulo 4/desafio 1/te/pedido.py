from te import Te

sabor =int (input("  Ingrese el sabor del te"))
formato =int (input("  Ingrese los gramos"))

te = Te(sabor, formato)

print(f"El sabor del te es: {te.obtener_sabor()}")
print(f"El formato de {te.formato} gramos")
print(f"El precio del te es de: {Te.obtener_precio(formato)} ")
tiempo, recomendacion = Te.obtener_tiempo_y_recomendacion(sabor)
print(f"El tiempo de preparacion es: {tiempo}")
print(f"Se recomienda { recomendacion}")
print(f"Vence en: {Te.duracion}")