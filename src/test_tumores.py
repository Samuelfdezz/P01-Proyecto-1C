from tumores import *



def test_lee_datos():
    datos = lee_datos(r".\data\tumores.csv")
    print(len(datos))
    print(datos[:3])
    print(datos[85:])



def main():
    test_lee_datos()






if "__main__" == __name__:
    main()

