# Trabajo con tipos de datos compuestos

#Creación de datos de un inventario de vehículos.
#car_fleet.csv

# Creación de un programa de inventario de vehículos.

#Importe los módulos que utilizará
import csv
import copy

#Defina el diccionario que funcionará como tipo compuesto para leer los datos tabulares:
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

#Utilizará un bucle for para recorrer las claves y valores del diccionario
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

#Defina una lista vacía para almacenar el inventario 
myInventoryList = []

# Copia del archivo CSV en memoria.

#Apertura segura del archivo (with open)
# Abre el archivo car_fleet.csv asignándolo a la variable csvFile. El uso de la sentencia with garantiza que el archivo se cierre automáticamente al terminar el bloque de código, incluso si ocurre un error durante la ejecución.
with open('car_fleet.csv') as csvFile:

#Preparación del lector (csv.reader)
#csv.reader(csvFile, delimiter=',') crea un objeto iterador que interpreta cada fila del archivo separada por comas. La variable lineCount = 0 actúa como un contador de líneas procesadas.
    csvReader = csv.reader(csvFile, delimiter=',')

#Procesamiento del encabezado (if lineCount == 0)
#En la primera iteración, la fila contiene los títulos de las columnas. Se usa ", ".join(row) para formatear la lista de nombres como una sola cadena, se muestra en consola y se suma 1 al contador.  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')

# Realiza una copia superficial de tipos de datos complejos.
currentVehicle = copy.deepcopy(myVehicle)

#Impresión del inventario de vehículos
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")