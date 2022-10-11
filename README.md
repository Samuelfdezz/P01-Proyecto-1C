# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  22/23)
Autor/a: SAmuel Fernández Fernández   uvus: Samferfer1

Aquí debes añadir la descripción del dataset y un enunciado del dominio del proyecto.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **tumores.py**: Describe aquí el módulo principal.
  * **test_tumores.py**: Describe aquí el módulo de pruebas.
  * **\<modulo2.py\>**: Añade descripciones para el resto de módulos que pueda tener tu proyecto. Por ejemplo, sería conveniente tener un módulo separado con funciones genéricas para dibujar gráficas y/o otro con funciones genéricas de conversión de tipos. 
* **/data**: Contiene el dataset o datasets del proyecto
    * **tumores.csv**: Añade una descripción genérica del dataset.
    
## Estructura del *dataset*

Aquí debes describir la estructura del dataset explicando qué representan los datos que contiene y la descripción de cada una de las columnas.

El dataset está compuesto por 8 columnas, con la siguiente descripción:

* **serial**: de tipo int, representa el numero de lista que ocupa el paciente
* **category_number**: de tipo int, representa la gravedad del tumor que tiene el paciente
* **category_name**: de tipo str, representa el tipo de tumor que tiene el paciente
* **classification**: de tipo str, representa el subtipo de tumor que tiene el paciente
* **icd-o**: de tipo int, representa la clasificacion de tumor que tiene el paciente
* **grade_int**: de tipo float, representa lo avanzado que esta el tumor al momento de su analisis
* **datetime**: de tipo date, representa la fecha en la que se detecta el tumor
* **male**: de tipo boolean, representa el genero del paciente

## Tipos implementados

Descrbe aquí la o las namedtuple que defines en tu proyecto.

tumor es la namedtuple que contiene los datos de cada paciente y su tumor
## Funciones implementadas
Añade aquí descripciones genéricas de las funciones, que luego debes acompañar con comentarios de tipo documentación en el código

La funcion lee_datos , obtiene los valores del csv, y los añade en la tupla
### tumores.py>

* **lee_datos**: definimos la funcion lee_datos, que mete en una tupla los valores del csv

### test_tumores.py>

* **test_lee_datos**: Incluye la tupla a la variabla datos, y muestra los 3 primeros y 3 ultimos pacientes del csv
