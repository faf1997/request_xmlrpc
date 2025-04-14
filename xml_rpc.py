import xmlrpc.client


class RequestXMLRPC:
    def __init__(self, url:str, db:str, user:str, password:str) -> None:
        self.url = url
        self.db = db
        self.user = user
        self.password = password
        self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        self.uid = self.common.authenticate(self.db, self.user, self.password, {})
        self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    def search(self, model:str='res.partner', action:str='search', domain:list=[('customer_rank', '=', True)]):
        return self.models.execute_kw(
            self.db,
            self.uid,
            self.password,
            model,
            action,
            [domain]
            )
    
    def read(self, model:str='res.partner', action:str='read', ids:list=[], fields:list=['name']):
        return self.models.execute_kw(
            self.db,
            self.uid,
            self.password,
            model,
            action,
            ids,
            {'fields': fields}
            )
    
    def create(self, model:str='res.partner', action:str='create',data_fields:dict[str,str]={'name':'Nuevo UsuarioXMLRPC'}):
        self.models.execute_kw(
            self.db,
            self.uid,
            self.password,
            model,
            action,
            [data_fields]
            )

    def update(self, model:str='res.partner', action:str='write', id=1, data_fields:dict={'name':'Nuevo NombreXMLRPC'}):
        self.models.execute_kw(self.db,
            self.uid,
            self.password,
            model,
            action,
            [[id], data_fields]
            )

    def get_fields(self, model='account.move', fields=[]):
        fields_info = self.models.execute_kw(self.db, self.uid, self.password, model, 'fields_get', fields)
        return [str(key) for key in fields_info]

    def print_data_fields(self, model, ids, field_list):
        readed_fields = []
        for field in field_list:
            try: 
                data = self.read(model=model, ids=ids, fields=[field])
                readed_fields.append([str(field), str(data)])
                print(field, data)
            except:
                message = f'{field} no se pudo leer'
                readed_fields.append([str(field), message])
                print(message)
        return readed_fields

if __name__ == '__main__':
    url = 'https://aninmuebles-demo-13126541.dev.odoo.com/'
    db = 'aninmuebles-demo-13126541'
    user = 'romina@an-inmuebles.com.ar'
    password = 'fe81c95989cbe6ec0d73476fbad489183c4141f9'
    model = 'account.payment.group'#'account.move'
    r = RequestXMLRPC(url,db,user,password)
    invoice_ids = r.search(model=model, domain=[['partner_id', '=', 'AFIP']])
    print(invoice_ids)
    invoice_fields = r.get_fields(model=model)

    #pay = r.read(model=model,ids=invoice_ids[0],fields=invoice_fields)



    # elementos_a_eliminar = ['needed_terms']

    # lista_filtrada = [x for x in invoice_fields if x not in elementos_a_eliminar]

    # print(lista_filtrada)  # Output: [1, 3, 5]


    # for f in lista_filtrada:
    #     print(f)
    #     invoice_data = r.read(model=model,ids=invoice_ids,fields=[f])
    #     print(invoice_data)
    # print(invoice_data)
    
