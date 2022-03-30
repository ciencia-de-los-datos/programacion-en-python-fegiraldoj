"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
from collections import Counter




def pregunta_01():
    """ 
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("data.csv", "r") as file:
        list_data = file.readlines()    

    suma = 0

    for values in list_data:
        values_tmp = values.split()
        suma += int(values_tmp[1])
    
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    with open("data.csv", "r") as file:
        list_data = file.readlines()

    column_a_list = []
    for values in list_data:
        values_tmp = values.split()
        column_a_list.append(values_tmp[0])

    column_a_distinct_list = list(dict.fromkeys(column_a_list))
    column_a_distinct_list.sort()
    values_occurence_list = []

    for column_a_value in column_a_distinct_list:
        values_occurence_list.append((column_a_value, column_a_list.count(column_a_value)))

    return values_occurence_list


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    with open("data.csv", "r") as file:
        list_data = file.readlines()

    column_a_list = []
    column_b_list = []
    for values in list_data:
        values_tmp = values.split()
        column_a_list.append(values_tmp[0])
        column_b_list.append(int(values_tmp[1]))

    columns_ab_list = list(zip(column_a_list,column_b_list))

    sums_dict = {}
    result_list = []
    for col_a, col_b in columns_ab_list:
        sums_dict[col_a] = col_b if col_a not in sums_dict else sums_dict[col_a] + col_b


    #result_list = [(k, v) for k, v in sums_dict.items()]
    #result_list = list(sums_dict.items())
    result_list = list(zip(sums_dict.keys(), sums_dict.values()))
    result_list.sort(key=lambda i:i[0])

    return result_list


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv", "r") as file:
        list_data = file.readlines()

    column_c_months_list = []
    for values in list_data:
        values_tmp = values.split()
        column_c_months_list.append(values_tmp[2][5:7])

    column_c_distinct = list(dict.fromkeys(column_c_months_list))
    column_c_distinct.sort()
    values_occurence_list = []

    for column_c_value in column_c_distinct:
        values_occurence_list.append((column_c_value, column_c_months_list.count(column_c_value)))
    
    return values_occurence_list


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv", "r") as file:
        list_data = file.readlines()

    column_a_list = []
    column_b_list = []
    for values in list_data:
        values_tmp = values.split()
        column_a_list.append(values_tmp[0])
        column_b_list.append(int(values_tmp[1]))

    columns_ab_list = list(zip(column_a_list,column_b_list))

    max_dict = {}
    min_dict = {}
    result_list = []
    for col_a, col_b in columns_ab_list:
        max_dict[col_a] = col_b if col_a not in max_dict else max_dict[col_a] if max_dict[col_a] > col_b else col_b
        min_dict[col_a] = col_b if col_a not in min_dict else min_dict[col_a] if min_dict[col_a] < col_b else col_b

    result_list = list(zip(max_dict.keys(), max_dict.values(), min_dict.values()))
    result_list.sort(key=lambda i:i[0])
    
    return result_list

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open("data.csv", "r") as file:
        list_data = file.readlines()

    column_e_list = []
    for values in list_data:
        values_tmp = values.split()
        [column_e_list.append(x) for x in values_tmp[4].split(",")]

    column_e_keys = []
    column_e_values = []
    [[column_e_keys.append(x), column_e_values.append(int(y))] for s in column_e_list for (x, y) in [s.split(":")]]

    column_e_list = list(zip(column_e_keys, column_e_values))

    max_dict = {}
    min_dict = {}
    result_list = []

    for key, value in column_e_list:
        max_dict[key] = value if key not in max_dict else max_dict[key] if max_dict[key] > value else value
        min_dict[key] = value if key not in min_dict else min_dict[key] if min_dict[key] < value else value

    result_list = list(zip(min_dict.keys(), min_dict.values(), max_dict.values()))
    result_list.sort(key=lambda i:i[0])

    return result_list

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 1 y 2. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    

    file = open("data.csv", "r")

    data = []
    column_b_distinct = []
    for row in csv.reader(file, delimiter="\t"):
        data.append([row[0], row[1]])
        column_b_distinct.append(row[1])

    column_b_distinct = list(dict.fromkeys([row[1] for row in data]))
    column_b_distinct.sort()

    return_list = []
    letter_list = []

    for x in column_b_distinct:
        for y in data:
            if x == y[1]:
                letter_list.append(y[0])
        
        tupla = (int(x),letter_list.copy())
        return_list.append(tupla)
        letter_list.clear()
        
    return return_list


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
