#!/usr/bin/env python3
"""Proyecto sobre Python y el workflow Pull-Request en GitHub.

Cada participante debe completar su función y luego solicitar el Pull-Request.

Este código fue generado por:
https://github.com/ejdecena/calculo_numerico/codigos/generar_proyecto_pr.py
"""

def Alejandro_27525819():
    """
    Recibe como parámetro una lista y retorna el promedio de la lista.
    """
    pass


def Anibal_26887484(cadena):
  """
  Recibe como parámetro una cadena y retorna una lista con las vocales de la cadena.
  """
  "Lower y set inspiradas de la funcion de Jesus_22998438"
  vocales = set('aeiou')
  lista_vocales = []
  for letra in cadena.lower():
   if letra in vocales:
      lista_vocales.append(letra) 
  return lista_vocales  


def Ashly_27424492():
    """
    Recibe como parámetro un diccionario y retorna una lista con los valores del diccionario.
    """
    pass


def Danilo_27424264():
    """
    Recibe como parámetro los valores a, b, c y retorna el mínimo.
    """
    pass


def Diego_27650623():
    """
    Recibe como parámetro un diccionario y retorna una lista con las claves del diccionario.
    """
    pass


def Enrique_27000054():
    """
    Recibe como parámetro un diccionario y retorna el mínimo valor del diccionario.
    """
    pass


def Estefano_26778542():
    """
    Recibe como parámetro una lista y retorna el máximo valor de la lista.
    """
    pass


def Hector_25967387():
    """
    Recibe como parámetro una lista y retorna la lista invertida.
    """
    pass


def Jesus_22998438(cadena):
    """
    Recibe como parámetro una cadena y retorma una lista con las consonantes de la cadena.
    """
    consonants = set("bcdfghjklmnpqrstvwxyz")
    result = []
    for caracter in cadena:
      if caracter.lower() in consonants:
        result.append(caracter)
    return result


def Jose_27525799():
    """
    Recibe como parámetro un diccionario y retorna el máximo valor del diccionario.
    """
    pass


def Mauricio_27202233():
    """
    Recibe como parámetro una cadena y retorna la cadena invertida.
    """
    pass


def Miguel_26842695(lista):
    """
    Recibe como parámetro una lista y retorna el mínimo valor de la lista.
    """
    
    min= lista[0]
    
    for i in lista:
        if i < min:
            min=i

    return min
    

def Norlie_26707950(a,b,c):
    """
    Recibe como parámetro a, b, c y retorma el máximo.
    """
    if a>b and a>c:
        return a
    else:
        if b>c:
            return b
        else:
            return c
    

def Wuilmer_26625191(cadena):
    """
    Recibe como paŕametro una cadena y retorna el número de caracteres de la cadena.
    """
    tam=len(cadena)
    return tam

