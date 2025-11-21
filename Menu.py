from funciones_stark import*


def Menu():
    print("")
    print("1- Imprimir los nombres de todos los Superhéroes.")
    print("2- Conocer el peso de cada Superhéroe.")
    print("3- Conocer al Superhéroe mas ALTO.")
    print("4- Conocer al Superhéroe mas BAJO.")
    print("5- Conocer el PROMEDIO de altura general de todos los Superhéroes.")
    print("6- Conocer al Superhéroe de MAYOR PESO.")
    print("7- Conocer al Superhéroe de MENOR PESO.")
    print("8- Presione 8 para terminar el programa.")



while True:
    Menu()
    print()

    usuario = input("Elija una de las opciones para conocer alguno de los datos expuestos:\n")
    
    if not usuario.isdigit():
        print("Error, debe ingresar uno de los valores enteros indicados al principio.")
    else:
        usuario = int(usuario)


        if usuario == 1:
            print("*** A CONTINUACIÓN, EL NOMBRE DE TODOS LOS HÉROES ***\n")
            imprimir_nombre(lista_personajes, "nombre")

        if usuario == 2:
            print("*** A CONTINUACIÓN, EL NOMBRE DE TODOS LOS HÉROES CON SU PESO ***\n")
            imprimir_nombre_altura(lista_personajes)

        if usuario == 3:
            print("*** HÉROE DE MAYOR ALTURA")
            print(hallar_valor_mayor_menor_lista_dict(lista_personajes, "altura", "maximo"))

        if usuario == 4:
            print("*** HÉROE DE MENOR ALTURA")
            print(hallar_valor_mayor_menor_lista_dict(lista_personajes, "altura", "minimo"))

        if usuario == 5:
            print("*** PROMEDIO DE ALTURA ***")
            print(f"El promedion de altura toal es de :{promedio_altura_heroes(lista_personajes)}")

        if usuario == 6:
            print("*** HÉROE DE MAYOR PESO")
            print(hallar_valor_mayor_menor_lista_dict(lista_personajes, "peso", "maximo"))


        if usuario == 7:
            print("*** HÉROE DE MENOR ALTURA")
            print(hallar_valor_mayor_menor_lista_dict(lista_personajes, "peso", "minimo"))

        if usuario == 8:
            print("SALIENDO DEL PROGRAMA...")
            break

        if type(usuario) != int:
            print("Error, debe ingresar uno de los valores enteros indicados al principio.")




    