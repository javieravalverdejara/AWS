#Clasificación de valores

# Ejercicio 1: Crear una lista de varios tipos de datos.

#Defina una lista con diferentes tipos
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

#instrucción de bucle for para recorrer la lista e imprimir el tipo de dato de cada elemento en ella.
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))