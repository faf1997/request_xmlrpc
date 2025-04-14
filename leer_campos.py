import xmlrpc.client



# animuebles

# Datos de conexión
url = "https://equipavic-stg-16-12-24-17225651.dev.odoo.com/"
db = "equipavic-stg-16-12-24-17225651"
username = "mariano.bourlot@bourlot.com.ar"
password = "f413e9879ebf28051745efe53f67a19f2fda1034"

# Crear un objeto de conexión común
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
# Autenticar
uid = common.authenticate(db, username, password, {})

# Crear un objeto de conexión para los métodos del modelo
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Definir el dominio de búsqueda (puedes ajustar el dominio según sea necesario)
domain = [('id', '=', 1754)] #('NAME', '=', 'Ret Ganancias') # Aquí puedes especificar criterios de búsqueda, como [('field_name', '=', 'value')]

# Definir los campos que deseas leer
fields = []#['id', 'checkbook_ids', 'bank_id', 'display_name', 'nro_cuenta']

# Realizar la búsqueda y leer los registros en una sola llamada
records = models.execute_kw(db, uid, password, 'account.payment', 'search_read', [domain], {'fields': fields})

# Imprimir los registros obtenidos
if len(records) > 0:
    for field_name in records[0]:
        print(field_name,": " ,records[0][field_name])
        
else:
    print('No hay registros')