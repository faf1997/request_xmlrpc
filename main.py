from xml_rpc import RequestXMLRPC

if __name__ == '__main__':
    url = 'http://localhost:8069'
    db = 'pruebas'
    username = 'admin'
    password = 'admin'

    r = RequestXMLRPC(url, db, username, password)
    #crear
    partner = {
        'name': 'Cosme Fulanito',
        'street': 'Calle Falsa 123'
    }
    # r.create(data_fields=partner)


    # #Buscar por condición
    domain = [('name','=','AFIP')]
    model = 'res.partner'
    searched_ids = r.search(domain=domain)
    

    #leer datos específicos del partner
    specific_fields = ['name', 'street', 'country_id', 'state_id']
    
    data_user = r.read(ids=searched_ids,fields=specific_fields)
    for field in data_user:
        print(field)


    # buscar el país del partner
    model = 'res.country',
    print([data_user[0]['country_id'][0]])
    country = r.read(
        model=model
    )
    print(country)
    
    # r.update()






