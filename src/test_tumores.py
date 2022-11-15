from tumores import *

datos = lee_datos(r"P01-Proyecto-1C\data\tumores.csv")

def test_lee_datos():
   
    print(len(datos))
    print(datos[:3])
    print(datos[85:])

def test_filtra_por_genero():
    print(filtra_por_genero(datos))

def test_media_icdo():
    print(media_icdo(datos))

def test_max_grado():
    print(max_grado(datos))

def test_ordenar_por_categ():
    print(ordenar_por_categ(datos))

def test_agrupar_por_nombre():
    print(agrupar_por_nombre(datos))


def main():
    ##test_lee_datos()
    test_filtra_por_genero()
    test_media_icdo()
    test_max_grado()
    test_ordenar_por_categ()
    test_agrupar_por_nombre()
    
if "__main__" == __name__:
    main()

