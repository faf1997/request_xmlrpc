from xml_rpc import RequestXMLRPC

from lector_excel import guardar_matriz_como_excel

if __name__ == '__main__':
    url = 'https://bernova.odoo.com/'
    db = 'fixon-bernova-produccion-13328521'
    username = 'soporte@fixon.com.ar'
    password = '25985115cfee23052074ca65d90b0be3291d3d75'
    card_instalment = 'account.move' #'sale.order'#

    r = RequestXMLRPC(url, db, username, password)

    # domain = [('name', '!=', 'FA-B 00005-00000015')]
    domain = [('id', '=', 7186)]
    searched_ids = r.search(model=card_instalment, domain=domain)

    print(searched_ids)
    payments_fields = r.get_fields(model=card_instalment)
    # print(payments_fields)
    id = searched_ids[0]
    matriz = r.print_data_fields(card_instalment, ids=[id], field_list=payments_fields)
    #matriz.insert(0, ['Nombre del campo', 'Valor'])
    #guardar_matriz_como_excel(matriz, f'account_payment_group_anin.xlsx')








