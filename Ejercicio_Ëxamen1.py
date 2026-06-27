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
       if items[codigo][1].lower == categoria:
           
           total += inventario[codigo][1]

    print("El stock es:", total)
    

