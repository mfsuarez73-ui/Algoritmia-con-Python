from datos_personajes import*
from funciones_aux import*

## Recorrer la lista imprimiendo por consola el nombre de cada superhéroe ##

def imprimir_nombre(lista:list[dict], dato:str):
    return mostrar_dato(lista, dato)

## Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo ##

def imprimir_nombre_altura(lista:list[dict]):
    name_heroe =  obtener_dato(lista, "nombre")
    altura_heroe = convertir_dato_float(obtener_dato(lista, "altura"))
                         
    for data in range(len(name_heroe)):
        print(f"Nombre: {name_heroe[data]}\nAltura: {altura_heroe[data]}")
        print("")

## Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO) ##

hallar_valor_mayor_menor_lista_dict(lista_personajes, "altura", "maximo")


## Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO) ##

hallar_valor_mayor_menor_lista_dict(lista_personajes, "altura", "minimo")


## Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO) ##

def promedio_altura_heroes(lista:dict):
    if type(lista) != list:
        return 0    
    return promedio(convertir_dato_float(obtener_dato(lista, "altura")))

# Calcular e informar cual es el superhéroe más y menos pesado.

# hallar_valor_mayor_menor_lista_dict(lista_personajes, "peso", "minimo")



# print(pregunta("Punisher"))

# imprimir_nombre(lista_personajes, "identidad")






