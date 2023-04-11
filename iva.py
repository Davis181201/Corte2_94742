import csv

# Función para leer el archivo Alimentos.csv y organizar los productos por tarifa de IVA
def leer_archivo():
    alimentos = {"0": [], "0.05": [], "0.19": []}
    with open("Alimentos.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader) # saltar la primera fila del archivo CSV
        for row in csv_reader:
            codigo = row[0]
            descripcion = row[1]
            tarifa = row[2]
            alimentos[tarifa].append((codigo, descripcion))
    return alimentos

# Función para calcular el valor bruto de un producto alimenticio
def calcular_valor_bruto():
    alimentos = leer_archivo()
    while True:
        producto = input("Ingrese el código o descripción del producto (o escriba 'salir' para terminar): ")
        if producto.lower() == "salir":
            break
        valor_neto = float(input("Ingrese el valor neto del producto: "))
        for tarifa, lista_productos in alimentos.items():
            for codigo, descripcion in lista_productos:
                if producto.lower() == codigo.lower() or producto.lower() == descripcion.lower():
                    valor_base = valor_neto / (1 + float(tarifa))
                    valor_iva = valor_neto - valor_base
                    print(f"Valor base del producto: {valor_base:.2f}")
                    print(f"Valor del IVA: {valor_iva:.2f}")
                    break
            else:
                continue
            break
        else:
            print("El producto ingresado no se encuentra en el archivo Alimentos.csv")

# Función principal
def main():
    calcular_valor_bruto()

# Ejecución de la función principal
if __name__ == "__main__":
    main()