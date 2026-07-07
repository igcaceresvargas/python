#Ejercicio tipo examen

#items = {codigo: [nombre, categoria. rareza, tipo_magia]}
items = {
    "MAG001":["Agonia de Escarcha","Arma","Legendaria","Hielo"],
    "MAG002":["Anillo de Sauron","Accesorio","Epica","Magia"],
    "MAG003":["Pocion Curativa","Consumible","Comun","Vida"],
    "MAG004":["Corona Nemesis","Armadura","Legendaria","Dragon"],
    "MAG005":["Baston Lunar de Lileath","Arma","Epica","Hechizo"],
    "MAG006":["Cristal de Hielo","Material","Rara","Hielo"],
}

#inventario = {codigo: [precio, cantidad]}
inventario = {
    "MAG001":[5000,3],
    "MAG002":[2500,8],
    "MAG003":[100,50],
    "MAG004":[10000,1],
    "MAG005":[3500,4],
    "MAG006":[800,0],
}

def stock_categoria(categoria):
    total = 0

    for codigo in items:
       if items[codigo][1].lower() == categoria.lower():
           
           total += inventario[codigo][1]

    print("El stock es:", total)

def busqueda_precio(p_min,p_max):

    resultados = []

    for codigo in inventario:
        precio = inventario[codigo][0]
        stock = inventario[codigo][1]
        rareza = items[codigo][2]
        if precio >= p_min and precio <= p_max:
            if stock > 0:
                elemento = f"{rareza}--{codigo}"
                resultados.append(elemento)
    resultados.sort()
    print(resultados)

def actualizar_precio(codigo, precio):

    if codigo in inventario:
        inventario[codigo][0] = precio
        return True
    else:
        return False

def buscar_objeto(codigo):

    if codigo in inventario and codigo in items:
        nombre = items[codigo][0]
        categoria = items[codigo][1]
        rareza = items[codigo][2]
        tipo_magia = items[codigo][3]

        precio = inventario[codigo][0]
        stock = inventario[codigo][1]

        print(f"""
              ---Informacion del objeto---
              Codigo: {codigo}
              Nombre: {nombre}
              Categoria: {categoria}
              Rareza: {rareza}
              Tipo de magia: {tipo_magia}
              Precio: ${precio}
              Stock: {stock} unidades
              -----------------------------
              """)
        
    else: 
        print("El codigo no existe")

def mostrar_todo():
    numero_objeto = 1
    
    for codigo in inventario:
        nombre = items[codigo][0]
        categoria = items[codigo][1]
        rareza = items[codigo][2]
        tipo_magia = items[codigo][3]

        precio = inventario[codigo][0]
        stock = inventario[codigo][1]

        print(f"- Objeto {numero_objeto}-")
        print(f"""
              ---Informacion del objeto---
              Codigo: {codigo}
              Nombre: {nombre}
              Categoria: {categoria}
              Rareza: {rareza}
              Tipo de magia: {tipo_magia}
              Precio: ${precio}
              Stock: {stock} unidades
              -----------------------------
              """)
        numero_objeto += 1

while True:
    try:
        print("--- MENÚ DE LA TIENDA ---")
        print("1. Stock por categoría")
        print("2. Búsqueda por precio")
        print("3. Actualizar precio")
        print("4. Buscar objeto por código")
        print("5. Mostrar todos los objetos")
        print("6. Salir")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            cat = input("Ingrese categoria: ")
            stock_categoria(cat)

        elif opcion == 2:
            p_min = int(input("Ingrese precio minimo: "))
            p_max = int(input("Ingrese precio maximo: "))
            busqueda_precio(p_min, p_max)

        elif opcion == 3:
            

        