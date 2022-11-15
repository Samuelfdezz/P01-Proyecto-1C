import csv
from collections import namedtuple
from datetime import datetime

tumores = namedtuple("Tumor", "serial,category_number,category_name,classification,icdo,grade_int,datetime,male")

def lee_datos(fichero):
    with open(fichero, encoding="utf-8") as f:
        lector= csv.reader(f)
        next(f)
        result = []
        for tumor in lector:
            tupla = tumores(int(tumor[0]), int(tumor[1]), tumor[2], tumor[3], int(tumor[4]), float(tumor[5]), datetime.strptime(tumor[6], "%m/%d/%Y"), tumor[-1])

            result.append(tupla)

        return result

def filtra_por_genero(tumores):
    res = []
    for tumor in tumores:
        if tumor.male=="TRUE":
            res.append(tumor)
    return res

def media_icdo(tumores):
    res = []
    for tumor in tumores:
       res.append(tumor.icdo)
    return sum(res)/len(res)

def max_grado(tumores):
    return max(tumores,key=lambda tumor:tumor.grade_int)

def ordenar_por_categ(tumores):
    return sorted(tumores,key=lambda tumor:tumor.icdo,reverse=True)

def agrupar_por_nombre(tumores):
    res={}
    for tumor in tumores:
        clave=tumor.category_name
        if clave not in res:
            res[clave]=[tumor]
        else:
            res[clave].append(tumor)
    return res
        