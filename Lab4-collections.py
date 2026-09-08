# Ejercicio 1: Presentar el tipo de dato de lista

#Listas
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

# Posición en a lista

#Para acceder a la cadena apple
print(myFruitList[0])
#Para acceder a la cadena banana
print(myFruitList[1])
#Para acceder a la cadena cherry
print(myFruitList[2])

# modificación en los valores de la lista

#En esta actividad, cambiará cherry por orange
myFruitList[2] = "orange"
#Mestra la lista actual, actualizada.
print(myFruitList)

# Ejercicio 2: Presentar el tipo de dato de tupla

#Crea una tupla: Una tupla es similar a una lista, pero no se puede cambiar. Un tipo de dato que no se puede cambiar después de su creación se conoce como inmutable . Para definir una tupla, se utilizan paréntesis en lugar de corchetes ([]).
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

# Acceso a una tupla por posición.

#Para acceder a la cadena apple.
print(myFinalAnswerTuple[0])
#Para acceder a la cadena banana.
print(myFinalAnswerTuple[1])
#Para acceder a la cadena pineapple
print(myFinalAnswerTuple[2])

# Ejercicio 3: Presentar el tipo de dato de diccionario.

#Un diccionario es una lista cuyas posiciones tienen nombres asignados (claves).
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
#Muestra o imprime el diccionario.
print(myFavoriteFruitDictionary)
#Tipo de dato.
print(type(myFavoriteFruitDictionary))

#acceso al diccionario por nombre

#Para acceder a la fruta favorita de Akua.
print(myFavoriteFruitDictionary["Akua"])
#Para acceder a la fruta favorita de Saanvi.
print(myFavoriteFruitDictionary["Saanvi"])
#Para acceder a la fruta favorita de Paulo.
print(myFavoriteFruitDictionary["Paulo"])
