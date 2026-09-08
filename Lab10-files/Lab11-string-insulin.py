#!/usr/bin/env python3
# coding: utf-8

# ─────────────────────────────────────────────
# ARCHIVO: Lab11-string-insulin.py
# PROPÓSITO: trabajar con secuencias y pesos
#            de la insulina humana
# ─────────────────────────────────────────────

# ── 1. VARIABLES DE SECUENCIA ─────────────────

# Secuencia completa de la preproinsulina humana
# La barra invertida (\) divide la línea para cumplir PEP 8 (máx. 79 caracteres)
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
                "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Cadenas individuales de la insulina humana
lsInsulin = "malwmrllpllallalwgpdpaaa"        # señal (aa 1-24)
bInsulin  = "fvnqhlcgshlvealylvcgergffytpkt"  # cadena B (aa 25-54)
aInsulin  = "giveqcctsicslyqlenycn"           # cadena A (aa 90-110)
cInsulin  = "rreaedlqvgqvelgggpgagslqplalegslqkr"  # cadena C (aa 55-89)

# Insulina procesada = cadena B + cadena A
insulin = bInsulin + aInsulin


# ── 2. IMPRIMIR SECUENCIAS ────────────────────

# Imprime la secuencia completa de la preproinsulina
print("The sequence of human preproinsulin:")
print(preproInsulin)

# Imprime la cadena A usando concatenación de strings
print("The sequence of human insulin, chain a: " + aInsulin)


# ── 3. CÁLCULO DEL PESO MOLECULAR ────────────

# Diccionario con el peso molecular de cada aminoácido (en Daltons)
aaWeights = {
    'A': 89.09,  'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
    'G': 75.07,  'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17,
    'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20,
    'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19
}

# Lista de los 20 aminoácidos
aminoacids = ['A','C','D','E','F','G','H','I','K','L',
              'M','N','P','Q','R','S','T','V','W','Y']

# Contamos cuántas veces aparece cada aminoácido en la insulina
# .upper() convierte a mayúsculas para coincidir con las claves del diccionario
aaCountInsulin = {
    x: float(insulin.upper().count(x))
    for x in aminoacids
}

# Multiplicamos cantidad × peso de cada aminoácido y sumamos todo
molecularWeightInsulin = sum(
    aaCountInsulin[x] * aaWeights[x]
    for x in aminoacids
)

print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))


# ── 4. PORCENTAJE DE ERROR ────────────────────

# Peso molecular real de la insulina (dato de referencia)
# El calculado difiere porque no descuenta los enlaces entre aminoácidos
molecularWeightInsulinActual = 5807.63

# Fórmula: ((calculado - real) / real) × 100
print("Error percentage: " + str(
    ((molecularWeightInsulin - molecularWeightInsulinActual)
     / molecularWeightInsulinActual) * 100
))