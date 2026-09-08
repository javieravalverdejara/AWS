# Trabajo con bucles.

# Ejercicio 1: Trabajo con un bucle while.

#Utilice la función print() para informar al usuario acerca del juego.
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#Importación aleatoria y escritura de un bucle.
import random

#random:valores aleatorios enteros. 
#randint(1,10):Números enteros (random integer) y valores que definan al rango.
number = random.randint(1,10)

#Monitoree si el usuario adivinó su número con la creación de una variable llamada isGuessRight.
isGuessRight = False

#Para gestionar la lógica del juego, cree un bucle while.
#El bucle whilerepetirá el código dentro del bucle hasta que se adivine el número correcto, lo que está representado por la condición isGuessRight != Trueen el código. Además, Python utiliza la sangría con espacios para determinar los bloques lógicos, es decir, qué instrucciones se consideran parte del bucle while.
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

#Pseudocódigo del bucle while
# Condición de entrada al bucle: Mientras isGuessRight sea distinto de True (es decir, el usuario aún no ha adivinado), continuar dentro del bucle.
# Pedir input: Solicitar al usuario que ingrese un número entre 1 y 10, y guardar esa respuesta en la variable guess.
# Comparar la respuesta: Convertir guess a número entero y compararlo con el número secreto almacenado en number.
# Si la respuesta es correcta:
# Informar al usuario qué número ingresó y felicitarlo por haber ganado.
# Cambiar isGuessRight a True.
# El bucle evalúa su condición nuevamente: como isGuessRight ya es True, sale del bucle y el juego termina.
# Si la respuesta es incorrecta:
# Informar al usuario qué número ingresó y avisarle que no es el correcto.
# El bucle evalúa su condición nuevamente: como isGuessRight sigue siendo False, vuelve al paso 2 y repite el proceso.
# Concepto clave: La variable isGuessRight actúa como un "interruptor". El bucle sigue girando mientras esa variable valga False, y se detiene en el momento en que el usuario acierta y la variable cambia a True.
