from te import Te

te1 = Te(1, 300)
te2 = Te(2, 500)

type_te1 = type(te1)
type_te2 = type(te2)

print(type_te1)
print(type_te2)

if type_te1 == type_te2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")
    