from datos_personajes import *

def mostrar_dato(lista:list[dict], dato_puntual:str)->str:
# recorre una lista de diccionarios e imprime, si existe, el valor de alguna de las claves.
    for dato in range(len(lista)):
        if dato_puntual not in lista_personajes[dato]:
            print("No es un dato que corresponda con la búsqueda...")
            break
        else:
            print(lista[dato][dato_puntual])

def obtener_dato(lista:list[dict], clave:str)->list:
# obtenemos algún tipo de dato dentro de una lista de diccionarios a partir de alguna de sus claves.
    datos_a_obtener = []
    for i in range(len(lista)):
        datos_a_obtener.append(lista[i][clave])
    return datos_a_obtener
# print(obtener_dato(lista_personajes, "nombre"))

def convertir_dato_float(lista:list):
# convertir a float un dato de tipo numérico dentro de una lista de diccionarios.
    dato_convertido = []
    for i in range(len(lista)):
        dato = float(lista[i])
        dato_convertido.append(round(dato,2))
    return dato_convertido

def maximo(lista:list):
# retornamos el valor maximo hallado dentro de una lista.
    mayor = lista[0]
    for i in lista:
        if mayor < i:
            mayor = i
    return mayor


def minimo(lista:list):
# retornamos el valor minimo hallado dentro de una lista.
    menor = lista[0]
    for i in lista:
        if menor > i:
            menor = i
    return menor

def hallar_valor_mayor_menor_lista_dict(lista:list[dict], dato:str, alto_o_bajo:str):
# Recorrer la lista y determinar cuál es el superhéroe con un valor MÁXIMO o MÍNIMO según desée el usuario.

    msj = ""
    # asignamos el valor de max_min de acuerdo a lo que decida ingresar el usuario.
    if alto_o_bajo == "minimo":
        max_min = minimo(convertir_dato_float(obtener_dato(lista, dato)))
    else:
        alto_o_bajo == "maximo"
        max_min = maximo(convertir_dato_float(obtener_dato(lista, dato)))

    for heroe in range(len(lista)):
        if max_min == float(lista[heroe][dato]):
            msj = f"Nombre: {lista[heroe]["nombre"]}\n{dato.capitalize()}: {lista[heroe][dato]}"
    return msj

# print(heroe_mas_alto(lista_personajes, "peso", "minimo"))

import time



# Medimos el tiempo
# inicio = time.perf_counter()
# resultado = hallar_valor_mayor_menor_lista_dict(lista_personajes, "peso", "minimo")
# fin = time.perf_counter()

# print(f"El resultado es {resultado}")
# print(f"La función tardó {fin - inicio:.6f} segundos.")


def suma_lista(lista:float):
    if type(lista) != list:
        return 0
    contador = 0
    for i in lista:
        contador += i
    return contador

def promedio(lista):
# obtiene el promedio de una lista de numeros.
    if type(lista) != list:
        return 0
    prome = suma_lista(lista) / len(lista)
    return prome

