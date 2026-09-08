# Ejercicio 1: Recuperación de la secuencia de proteínas de la preproinsulina humana

# Abrimos el archivo con la secuencia limpia de la preproinsulina
with open("preproinsulin-seq-clean.txt") as f:
    preproinsulin = f.read()

# Mostramos la secuencia completa
print("Preproinsulina completa:")
print(preproinsulin)
print("Total de aminoácidos:", len(preproinsulin))

# Ejercicio 2: Obtención de las cadenas de la insulina humana

# Cadena señal (aminoácidos 1-24)
lsinsulin = preproinsulin[0:24]

# Cadena B (aminoácidos 25-54)
binsulin = preproinsulin[24:54]

# Cadena C (aminoácidos 55-89)
cinsulin = preproinsulin[54:89]

# Cadena A (aminoácidos 90-110)
ainsulin = preproinsulin[89:110]

# Mostramos cada cadena con su largo
print("\nCadena señal (1-24):", lsinsulin, "→", len(lsinsulin), "aa")
print("Cadena B (25-54):   ", binsulin,  "→", len(binsulin),  "aa")
print("Cadena C (55-89):   ", cinsulin,  "→", len(cinsulin),  "aa")
print("Cadena A (90-110):  ", ainsulin,  "→", len(ainsulin),  "aa")