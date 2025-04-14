from xml_rpc import RequestXMLRPC

from lector_excel import guardar_matriz_como_excel

if __name__ == '__main__':
    url = 'http://localhost:8069'
    db = 'cheques'
    username = 'admin'
    password = 'admin'
    account_payment = 'account.payment'#'account.move'
    
    r = RequestXMLRPC(url, db, username, password)

    # domain = [('check_number', '=', '00000001')]
    # domain = [('check_number', '=', '00000099')]
    domain = [('check_number', '=', '00012312')]

    searched_ids = r.search(model=account_payment, domain=domain)

    print(searched_ids)
    payments_fields = r.get_fields(model=account_payment, )#fields=['id', 'l10n_latam_check_id', 'payment_method_code'] payment_method_code = 'out_third_party_checks'
    # print(payments_fields)
    id = 128#searched_ids[0]
    matriz = r.print_data_fields(account_payment, ids=[id], field_list=payments_fields)
    #matriz.insert(0, ['Nombre del campo', 'Valor'])
    #guardar_matriz_como_excel(matriz, f'account_payment_group_anin.xlsx')








