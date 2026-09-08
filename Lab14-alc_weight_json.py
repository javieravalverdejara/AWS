# Importar el módulo propio (jsonFileHandler.py) para poder usar su función
import jsonFileHandler

# Llamar a la función readJsonFile() del módulo, pasándole la ruta del archivo JSON.
# La función abre el archivo, lo lee y devuelve su contenido como un diccionario de Python.
data = jsonFileHandler.readJsonFile('files/insulin.json')

# Verificación de seguridad: si la lectura falló, data quedaría como cadena vacía ""
# Solo se continúa con el cálculo si el archivo se leyó correctamente
if data != "":
    # Se accede a los valores del diccionario usando corchetes con las claves del JSON
    # data['molecules']['bInsulin'] entra primero a "molecules", luego busca "bInsulin"
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']

    # Se arma la insulina activa uniendo la cadena B + cadena A
    insulin = bInsulin + aInsulin

    # Peso molecular real de la insulina, también leído desde el JSON
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']

    # Se imprimen los datos leídos para confirmar que la lectura del JSON funcionó
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    # str() convierte el número (float) en texto para poder concatenarlo con +
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))

    # Calculating the molecular weight of insulin
    # Getting a list of the amino acid (AA) weights
    # Se obtiene el diccionario de pesos de aminoácidos, ahora desde el JSON (no escrito a mano)
    aaWeights = data['weights']

    # Count the number of each amino acids
    # Cuenta cuántas veces aparece cada aminoácido dentro de la secuencia "insulin"
    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})

    # Multiply the count by the weights
    # Multiplica el conteo de cada aminoácido por su peso, y suma todo para obtener el peso total
    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
    ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())

    # Muestra el peso molecular aproximado calculado
    print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))

    # Calcula y muestra el porcentaje de error respecto al peso real:
    # (medido - real) / real * 100
    print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
else:
    # Si data sigue vacío, significa que el archivo no se pudo leer
    print("Error. Exiting program")