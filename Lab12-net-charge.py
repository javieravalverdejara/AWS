# Store the human preproinsulin sequence in a variable called preproinsulin:
# (secuencia completa de la proteína precursora, antes de ser procesada)
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
# cada variable guarda un fragmento distinto de la secuencia de insulina
lsInsulin = "malwmrllpllallalwgpdpaaa"           # péptido señal
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"       # cadena B de la insulina
aInsulin = "giveqcctsicslyqlenycn"                # cadena A de la insulina
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  # péptido C (se descarta al madurar)

# La insulina activa (madura) está formada por la unión de la cadena B + cadena A
insulin = bInsulin + aInsulin

# Diccionario con los valores de pKa de los 7 aminoácidos que pueden tener carga eléctrica.
# El pKa indica el pH en el que ese aminoácido cambia de estado (cargado/neutro).
# Los demás aminoácidos no contribuyen a la carga neta, por eso no están aquí.
pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

# Cuenta cuántas veces aparece cada uno de esos 7 aminoácidos dentro de "insulin".
# Ejemplo de resultado: {'y': 4.0, 'c': 6.0, 'k': 2.0, ...}
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

# Se inicia el pH en 0 (el extremo más ácido de la escala)
pH = 0
