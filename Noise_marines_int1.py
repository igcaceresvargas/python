piso1 = {
    "101":"Juan Velez",
    "102":"Maria Soto"
}

piso2 = {
    "201":"Pedro Rojas",
    "202":"Ana Diaz"
}

piso3 = {
    "301":"Carlos Perez",
    "302":"Claudia Torres"
}
piso4 = {
    "401":"Jose Gonzalez",
    "402":"Camila Muñoz"
}

print("Dueño departamento 202:",piso2["202"])
piso3["302"] = "Juan Velez"
print("Piso 3 Actualizado: \n",piso3)
piso1 ["103"] = "Pedro Sanchez"
print("Piso 1 actualizado \n",piso1)
del piso4["402"]
print("Piso 4 actualizado \n",piso4)
print("Departamentos piso 2 \n",piso2)
print("")
