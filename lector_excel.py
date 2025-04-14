import pandas as pd

def imprimir_columnas(ruta_archivo_excel):
    try:
        datos_excel = pd.read_excel(ruta_archivo_excel)
        columnas = datos_excel.columns.tolist()
        print("Columnas del archivo Excel:")
        for columna in columnas:
            print(columna)
    except FileNotFoundError:
        print("El archivo no se encontró o no se pudo leer.")



def leer_excel(ruta_archivo_excel):
    try:
        datos_excel = pd.read_excel(ruta_archivo_excel)
        print("Contenido del archivo Excel:")
        print(datos_excel.to_string(index=False))
    except FileNotFoundError:
        print("El archivo no se encontró o no se pudo leer.")


def guardar_matriz_como_excel(matriz, nombre_archivo):

    dataframe = pd.DataFrame(matriz)
    dataframe.to_excel(nombre_archivo, index=False, header=False)
    # print(f"Matriz guardada como '{nombre_archivo}' en formato Excel con Pandas.")



def obtener_matriz_desde_excel(ruta_excel):
    try:
        datos_excel = pd.read_excel(ruta_excel)
        columnas = datos_excel.columns.tolist()
        matriz_python = datos_excel.values
        return columnas, matriz_python
    except Exception as e:
        print("Error al leer el archivo Excel:", e)
        return None, None





if __name__ == "__main__":
    ruta_del_archivo = 'Maestro de Productos LINEA OFICINA.xlsx' 
    # matriz = leer_excel(ruta_del_archivo)
    matriz = obtener_matriz_desde_excel(ruta_del_archivo)
    for i in range(len(matriz)):
        print(matriz[i][0])


# ruta_del_archivo = 'PROVEEDORES CASCO ENVIAR A NANY.xlsx' 
# imprimir_columnas(ruta_del_archivo)
