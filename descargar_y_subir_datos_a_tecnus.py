import xmlrpc.client
import json

####prod
# url = 'https://tecnus.odoo.com/'
# db = 'ntsystemwork-cl-tecnus-produccion-11177060'
# username = 'lconversano@backen.com.ar'
# password = '0eb2863a2c63fd7375e02be772fad289b0b2f523'

url = 'https://foodnovelty-pruebas-deposito-cheques-14429048.dev.odoo.com/'
db = 'foodnovelty-pruebas-deposito-cheques-14429048'
username = 'lconversano@backen.com.ar'
password = '8ee6eefeca00bad5fd2044c65c13466f02e92705'


# Conexión
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')


def filtrar_campos(lista1, lista2):
    """quitar campos repetidos""" 
    set1 = set(lista1)
    set2 = set(lista2)
    lista = list(set1 | set2)
    print(lista)
    return lista

def filtrar_datos(lista_de_tuplas)->dict:
    datos_filtrados = {}
    for modelo, campos in lista_de_tuplas:
        if not modelo in datos_filtrados:
            datos_filtrados[modelo] = campos
        else:
            datos_filtrados[modelo] = filtrar_campos(datos_filtrados[modelo], campos)
    return datos_filtrados


def cargar_datos_desde_archivo(input_file, new_models, new_db, new_uid, new_password, failed_output_file):
    # Leer los datos del archivo JSON
    with open(input_file, 'r') as f:
        datos = json.load(f)

    # Diccionario para almacenar los registros que no se pudieron actualizar o crear
    failed_records = {}

    for model, records in datos.items():
        for record in records:
            try:
                # Asume que hay un campo único para identificar el registro, como 'id'
                # Aquí se usa 'id' como ejemplo; ajusta según tus necesidades
                existing_record = new_models.execute_kw(new_db, new_uid, new_password, model, 'search', [[('id', '=', record['id'])]])

                if existing_record:
                    # Si el registro existe, actualízalo
                    new_models.execute_kw(new_db, new_uid, new_password, model, 'write', [existing_record, record])
                    print(f"Registro actualizado en el modelo {model}: {record}")
                else:
                    # Si el registro no existe, créalo
                    new_models.execute_kw(new_db, new_uid, new_password, model, 'create', [record])
                    print(f"Registro creado en el modelo {model}: {record}")
            except Exception as e:
                print(f"Error al procesar el registro en el modelo {model}: {e}")
                # Agregar el registro fallido al diccionario
                if model not in failed_records:
                    failed_records[model] = []
                failed_records[model].append(record)
    
    # Guardar los registros fallidos en un archivo JSON
    with open(failed_output_file, 'w') as f:
        json.dump(failed_records, f, indent=4)



def obtener_enteros(lista)->list:
    num = [elemento for elemento in lista if isinstance(elemento, (int))]
    if len(num) == 1:
        return num[0]
    else:
        return num

def filtrar_ids(diccionario):
    d = {}
    for field in diccionario:
        if isinstance(diccionario[field],(list)):
            d[field] = obtener_enteros(diccionario[field])
        else:
            d[field] = diccionario[field]
    return d

def filtrar_modelo(lista_diccionarios):
    lista_nueva = []
    for i in range(len(lista_diccionarios)):
        lista_nueva.append(filtrar_ids(lista_diccionarios[i]))
    return lista_nueva


def descargar_datos_y_guardar(models, db, uid, password, campos_de_los_modelos, output_file):
    datos = {}

    for model, fields in campos_de_los_modelos.items():
        try:
            # Leer los datos del modelo
            records = models.execute_kw(db, uid, password, model, 'search_read', [[]], {'fields': fields})
            datos[model] = filtrar_modelo(records)#filtrar_ids(records)
            # print(records)
            # break
        except Exception as e:
            print(f"Error al leer datos del modelo {model}: {e}")

    # Guardar los datos en un archivo JSON
    with open(output_file, 'w') as f:
        json.dump(datos, f, indent=4)









if __name__ == "__main__":
    empresa = 'tecnus'
    output_file_1 = f'datos_odoo_{empresa}.json'
    failed_output_file_2 = f'registros_fallidos_{empresa}.json'
    failed_output_file_3 = f'registros_fallidos_{empresa}_2.json'
    
    input_file_2 = f'datos_odoo_{empresa}.json'
    input_file_3 = f'registros_fallidos_{empresa}.json' 
    
    

    
    campos_de_los_modelos = [

    ('account.checkbook',[
        'id',
        'name',
        'journal_id',
        'sequence_id',
        'checkbook_type',
        'state',
        'next_number',
        'end_number',
        'checks_cancelled',

    ]),
        ('account.journal',[
        'id',
        'name',
        'checkbook_ids',
    ]),
    ('account.payment',[
        'id',
        'name',
        'check_number',
        'checkbook_id',
        'checkbook_type',
        'endosable',
        'display_checkbook_type',
        'display_check_number',
        'alpha_check_number',
        'category_check',
        'check_issue_date',
        'operation',
    ]),
    
    ('account.payment.group',[
        'id',
        'name',
        'last_check_number_by_checkbook',
    ]),
    
    ('res.company',[
        'id',
        'name',
        'ignore_journal_checkbook_sequence',
    ]),
    ('res.config.settings',[
        'id',
        'name',
        'ignore_journal_checkbook_sequence',
    ]),
    ]
    
    
    n = input("""
Ingrese un valor
[1] para copiar datos
[2] para subir datos
[3] subir datos residuales
""")
    if n == "1":
        # Ejecutar la función para descargar datos y guardarlos en un archivo JSON
        descargar_datos_y_guardar(models, db, uid, password, filtrar_datos(campos_de_los_modelos), output_file_1)

    if n == "2":
        # input_file = 'registros_fallidos.json'
        cargar_datos_desde_archivo(input_file_2, models, db, uid, password, failed_output_file_2)

    if n == "3":
        cargar_datos_desde_archivo(input_file_3, models, db, uid, password, failed_output_file_3)
        
        
        
        
        
        
        
        

"""
comandos foodnovelty:

git clone -b pruebas https://github.com/ntsystemwork/cl-foofnovelty.git

cd ./cl-foofnovelty/

git rm aeroo/aeroo_reports

git rm ingadhoc/aeroo

git rm a2systems/account_check_checkbook

git submodule init ntsystemwork/l10n_ar-hitofusion

git submodule update ntsystemwork/l10n_ar-hitofusion

git commit -m "replace account_check_checkbook"

git push

"""