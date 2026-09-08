#!/usr/bin/env python3
# coding: utf-8

# ─────────────────────────────────────────────
# ARCHIVO: Lab12-net-charge.py
# PROPÓSITO: calcular la carga neta de la
#            insulina entre pH 0 y pH 14
# ─────────────────────────────────────────────

# ── 1. VARIABLES DE SECUENCIA ─────────────────

# Secuencia completa de la preproinsulina humana
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
                "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Cadenas individuales de la insulina humana
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin  = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin  = "giveqcctsicslyqlenycn"
cInsulin  = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Insulina procesada = cadena B + cadena A
insulin = bInsulin + aInsulin

# ── 2. DICCIONARIO DE pKa ─────────────────────
# Solo los aminoácidos que contribuyen a la carga neta
# y=tirosina, c=cisteína, k=lisina, h=histidina,
# r=arginina, d=ácido aspártico, e=ácido glutámico
pKR = {'y':10.07, 'c':8.18, 'k':10.53,
       'h':6.00,  'r':12.48, 'd':3.65, 'e':4.25}

# ── 3. CONTAR AMINOÁCIDOS ─────────────────────
# count() cuenta cuántas veces aparece cada aminoácido
# float() convierte el resultado a número decimal
# Solo contamos los 7 aminoácidos que afectan la carga neta
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})


# ── 4. BUCLE WHILE — CARGA NETA pH 0 a pH 14 ──
# Iniciamos el pH en 0
pH = 0

# El bucle se repite mientras pH sea menor o igual a 14
while (pH <= 14):

    # Fórmula de carga neta de la insulina
    # Aminoácidos positivos: k, h, r
    # Aminoácidos negativos: y, c, d, e
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
        for x in ['y','c','d','e']}.values())))

    # Imprime el pH y la carga neta con 2 decimales
    print('{0:.2f}'.format(pH), netCharge)

    # Incrementa el pH en 1
    pH += 1