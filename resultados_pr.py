#!/usr/bin/env python3
"""Respuestas esperadas de las funciones del proyecto."""


def Alejandro_27525819(lista):
    """
    Recibe como parámetro una lista y retorna el promedio de la lista.
    """
    return sum(lista)/len(lista)


def Anibal_26887484(cadena):
    """
    Recibe como parámetro una cadena y retorna una lista con las vocales de la cadena.
    """
    vocales     = "a", "e", "i", "o", "u"
    set_vocales = set()
    for c in cadena:
        if c.lower() in vocales:
            set_vocales.add(c.lower())
    return list(set_vocales)


def Ashly_27424492(diccionario):
    """
    Recibe como parámetro un diccionario y retorna una lista con los valores del diccionario.
    """
    return list(diccionario.values())


def Danilo_27424264(a, b, c):
    """
    Recibe como parámetro los valores a, b, c y retorna el mínimo.
    """
    return min(a, b, c)


def Diego_27650623(diccionario):
    """
    Recibe como parámetro un diccionario y retorna una lista con las claves del diccionario.
    """
    return list(diccionario.keys())


def Enrique_27000054(diccionario):
    """
    Recibe como parámetro un diccionario y retorna el mínimo valor del diccionario.
    """
    return min(diccionario.values())


def Estefano_26778542(lista):
    """
    Recibe como parámetro una lista y retorna el máximo valor de la lista.
    """
    return max(lista)


def Hector_25967387(lista):
    """
    Recibe como parámetro una lista y retorna la lista invertida.
    """
    return list(reversed(lista))


def Jesus_22998438(cadena):
    """
    Recibe como parámetro una cadena y retorma una lista con las consonantes de la cadena.
    """
    import string

    letras  = set(string.ascii_lowercase)
    vocales = set(("a", "e", "i", "o", "u"))

    consonantes = letras - vocales
    cons_cadena = set()
    for c in cadena:
        if c.lower() in consonantes:
            cons_cadena.add(c)

    return list(cons_cadena)


def Jose_27525799(diccionario):
    """
    Recibe como parámetro un diccionario y retorna el máximo valor del diccionario.
    """
    return max(diccionario.values())


def Mauricio_27202233(cadena):
    """
    Recibe como parámetro una cadena y retorna la cadena invertida.
    """
    return "".join(reversed(cadena))


def Miguel_26842695(lista):
    """
    Recibe como parámetro una lista y retorna el mínimo valor de la lista.
    """
    return min(lista)


def Norlie_26707950(a, b, c):
    """
    Recibe como parámetro a, b, c y retorma el máximo.
    """
    return max(a, b, c)


def Wuilmer_26625191(cadena):
    """
    Recibe como paŕametro una cadena y retorna el número de caracteres de la cadena.
    """
    return len(cadena)