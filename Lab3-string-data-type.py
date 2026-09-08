#Ejercicio 1: Presentar el tipo de dato de cadena
myString = "This is a string."
print(myString)

#type() función integrada type()para obtener el tipo de dato de la variable.
print(type(myString))

#Para convertir el valor de retorno del tipo en una cadena.
print(myString + " is of the data type " + str(type(myString)))

#Ejercicio 2: Trabajar con concatenación de cadenas

#concatenación de cadena 
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#Ejercicio 3: Trabajar con cadenas de entrada

#cadena de entrada
name = input("Whats is your name?")
print(name)

#Ejercicio 4: Dar formato a las cadenas de salida

#dar formato a las cadenas
color = input("What is your favorite color?")
animal = input("What is your favorite animal?")

#se puede usar con una o múltiples variables para dar formato a una cadena.
print("{}, you like a {} {}!".format(name,color,animal))

#Nota: La instrucción final print()utiliza la función format(). En la función format(), las llaves de apertura y cierre “{}” actúan como marcadores de posición para las variables que se transmitirán , es decir, se ubicarán entre los paréntesis de la función.
