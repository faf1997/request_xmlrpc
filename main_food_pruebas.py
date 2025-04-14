from xml_rpc import RequestXMLRPC

from lector_excel import guardar_matriz_como_excel

if __name__ == '__main__':
    url = 'https://foodnovelty-pruebas-13386688.dev.odoo.com/'
    db = 'foodnovelty-pruebas-13386688'
    username = 'lconversano@backen.com.ar'
    password = '638a51a8c075a6093c78bab8ec9ff4b8094c0e6a'
    account_payment_group = 'account.payment'#'account.move'

    r = RequestXMLRPC(url, db, username, password)

    domain = [('check_number', '=', '123123123132123123123')]
    searched_ids = r.search(model=account_payment_group, domain=domain)

    print(searched_ids)
    payments_fields = r.get_fields(model=account_payment_group)
    # print(payments_fields)
    id = searched_ids[0]
    matriz = r.print_data_fields(account_payment_group, ids=[id], field_list=payments_fields)
    # matriz.insert(0, ['Nombre del campo', 'Valor'])
    # guardar_matriz_como_excel(matriz, f'account_payment_group_anin.xlsx')








