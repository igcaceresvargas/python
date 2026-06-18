pokemon = {
    "Pikachu":["Impactrueno","Ataque Rapido"],
    "Charmander":["Ascuas","Arañazo"],
    "Squirtle":["Pistola Agua","Placaje"]
}

def mostrar_pokedex():
    for nombre, movimientos in pokemon.items():
        print(nombre)

        for movimiento in movimientos:
            print("-",movimiento)
        print()

def agregar_movimiento():
    nombre = input("Pokemon: ")
    movimiento = input("Movimiento: ")

    if nombre in pokemon:
        pokemon[nombre].append(movimiento)
        print("Movimiento agregado correctamente")
    else:
        print("El Pokemon no esta registrado")

def mostrar_movimientos():
    nombre = input("Ingrese Pokemon: ")
    if nombre in pokemon:
        print("Movimientos:")
        for movimiento in pokemon[nombre]:
            print("-",movimiento)
        print()
    else:
        print("El pokemon no esta registrado")

def contar_movimientos():
    nombre = input("Ingrese Pokemon: ")