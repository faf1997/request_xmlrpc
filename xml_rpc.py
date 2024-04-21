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


