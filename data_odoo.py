data = [{'partner_type': 'customer', 'posted_before': False, 'company_id': 1, 'paired_internal_transfer_payment_id': False, 'currency_id': 19, 'name': 'PBNK1/2024/00001', 'is_internal_transfer': False, 'payment_type': 'inbound', 'partner_id': False, 'amount': 222, 'force_amount_company_currency': 0, 'amount_company_currency': 222, 'date': '2024-05-16', 'ref': False, 'journal_id': 40, 'payment_method_line_id': 29, 'payment_token_id': False, 'l10n_latam_check_number': False, 'l10n_latam_check_payment_date': False, 'l10n_latam_check_bank_id': False, 'l10n_latam_check_issuer_vat': False, 'partner_bank_id': False, 'destination_journal_id': False, 'l10n_latam_check_id': False, 'payment_group_id': 43, 'activity_ids': []}]




for key in data[0]:
    print(key, ": ", data[0][key]) 

