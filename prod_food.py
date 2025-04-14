import xmlrpc.client

# Datos de conexión
url = 'https://foodnovelty.odoo.com/'
db = 'foofnovelty-production-11887835'
username = 'lconversano@backen.com.ar'
password = 'e2540fdb95ec4ffa63394f998aad31da373dea2d'

# Crear un objeto de conexión común
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
# Autenticar
uid = common.authenticate(db, username, password, {})

# Crear un objeto de conexión para los métodos del modelo
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Definir el dominio de búsqueda (puedes ajustar el dominio según sea necesario)
domain = []  # Aquí puedes especificar criterios de búsqueda, como [('field_name', '=', 'value')]

# Definir los campos que deseas leer
fields = ['id', 'checkbook_ids', 'bank_id', 'display_name', 'nro_cuenta']

# Realizar la búsqueda y leer los registros en una sola llamada
records = models.execute_kw(db, uid, password, 'account.journal', 'search_read', [domain], {'fields': fields})

# Imprimir los registros obtenidos
for record in records:
    print(record)