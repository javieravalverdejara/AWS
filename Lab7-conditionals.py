# Trabajo con condicionales

# Ejercicio 1: Trabajo con la instrucción if

#Utilice la función input()para obtener información del usuario
userReply = input("Do you need to ship a package? (Enter yes or no) ")

#Instrucción de condicionamiento
#Nota : El símbolo ==es un operador de comparación. Significa es igual a
if userReply == "yes":
    print("We can help you ship that package!")

# Ejercicio 2: Trabajo con la instrucción else

#El caso por defecto, sí la condicion no ocurrio.
else:
    print("Please come back when you need to ship a package. Thank you.")

#Ejercicio 3: Trabajo con la instrucción elif

userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")

if userReply == "stamps":
    print("We have many stamp designs to choose from.")

#Evalúa una condición alternativa
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
    
    