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

