# ARCHIVO: Lab13-caesar-cipher.py
# PROPÓSITO: implementar un cifrado César
#            usando funciones definidas por el usuario
# ─────────────────────────────────────────────

# ── 1. FUNCIÓN: duplicar el alfabeto ──────────
# Recibe el alfabeto y lo concatena consigo mismo
# Ejemplo: "ABC" → "ABCABC"
# Sirve para poder desplazar letras sin salirse del rango
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet



