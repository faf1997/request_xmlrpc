from lector_excel import obtener_matriz_desde_excel, guardar_matriz_como_excel
# from reemplazar_clientes import normalizar_strings



def esta_contenido(matriz, valor:str, col:int):
    for fila in matriz:
        if fila[col] == valor:
            return True
        
    return False

    



    # print(matriz[i][col_inicio], "###", matriz[i+1][col_inicio], "#####", coincide)






if __name__ == "__main__":
    """
    pasos del código:
        contar las lineas que componen al producto
        contar la cantidad de variantes
        clonar las lineas que componen al producto temporalmente
        replicar las lineas clonadas por la cantidad de variantes y quitar las variantes en las repeticiones
    """



    ruta_xlsx_2 = "account_payment_group_anin.xlsx"
    ruta_xlsx = "account_payment_group_food.xlsx"
    columnas_1, matriz_1 = obtener_matriz_desde_excel(ruta_xlsx)
    columnas_2, matriz_2 = obtener_matriz_desde_excel(ruta_xlsx_2)


    matriz_aux = []

    contenidos = []
 
    col = 0



    for i in range(len(matriz_1)):
        validacion = esta_contenido(matriz_2, matriz_1[i][col], col)
        if not validacion:
            matriz_aux.append(matriz_1[i])
        else:
            contenidos.append(matriz_1[i])










    # guardar_matriz_como_excel(matriz_aux, 'diferencias_con_food_anin.xlsx')
    guardar_matriz_como_excel(contenidos, 'coincidencias_anin.xlsx')