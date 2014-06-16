# -*- coding: utf-8 -*-
C_MESSAGE_REQUIRED = u'Este campo es requerido.'
C_MESSAGE_MAX = u'La longitud máxima es de %d caracteres.'
C_MESSAGE_MIN = u'La longitud mínima es de %d caracteres.'
C_MESSAGE_ONLY_NUMBERS = u'Ingrese solo números.'

C_FIELD_NAME = 'txtName'
C_FIELD_LASTNAME = 'txtLastName'
C_FIELD_EMAIL = 'txtEmail'
C_FIELD_PASSWORD = 'txtPassword1'
C_FIELD_CONFIRM = 'txtRepeatPassword'
C_FIELD_DOCUMENT = 'txtDocument'
C_FIELD_PHONE_1 = 'txtPhone1'
C_FIELD_PHONE_2 = 'txtPhone2'
C_FIELD_ADDRESS = 'txtAddress'
C_FIELD_CHECK_TERMS = 'chkTerms'

CODIGO = dict()
CODIGO[C_FIELD_NAME] = 'name'
CODIGO[C_FIELD_LASTNAME] = 'last_name'
CODIGO[C_FIELD_EMAIL] = 'email'
CODIGO[C_FIELD_PASSWORD] = 'password'
CODIGO[C_FIELD_CONFIRM] = 'confirm'
CODIGO[C_FIELD_DOCUMENT] = 'document'
CODIGO[C_FIELD_PHONE_1] = 'phone_1'
CODIGO[C_FIELD_PHONE_2] = 'phone_2'
CODIGO[C_FIELD_ADDRESS] = 'address'
CODIGO[C_FIELD_CHECK_TERMS] = 'check_terms'

C_VALUE_NAME = 'Carlos'
C_VALUE_LASTNAME = 'Huamani'
C_VALUE_EMAIL = 'carlos.hs.92@hola.com'
C_VALUE_PASSWORD = 'carlos123'
C_VALUE_CONFIRM = 'carlos123'
C_VALUE_DOCUMENT_DNI = '78459598'
C_VALUE_DOCUMENT_RUC = '78459598652'
C_VALUE_DOCUMENT_PASSPORT = '5421235687'
C_VALUE_DOCUMENT_CARD = '5421875421'
C_VALUE_PHONE_1 = '7854859'
C_VALUE_PHONE_2 = '87596598'
C_VALUE_ADDRESS = 'Jose Galvez'
C_VALUE_CHECK_TERMS = True

def makeDict(location, description, value):
    return {'location': location, 'description': description, 'value': value, 'cod': CODIGO[location]}

def makeRegister(cod, error=True, type_error=None, ubigeo=None, address=None, document=None):
    register = {'prueba': cod,
                'error': False,
                'type_error': '',
                'name': C_VALUE_NAME,
                'last_name': C_VALUE_LASTNAME,
                'email': C_VALUE_EMAIL,
                'password': C_VALUE_PASSWORD,
                'confirm': C_VALUE_CONFIRM,
                'type_document': 'DNI',
                'document': C_VALUE_DOCUMENT_DNI,
                'phone_1': C_VALUE_PHONE_1,
                'phone_2': C_VALUE_PHONE_2,
                'type_address':'Calle',
                'address': C_VALUE_ADDRESS,
                'select_ubigeo': False,
                'department':'',
                'province':'',
                'district':'',
                'check_terms': C_VALUE_CHECK_TERMS}
    if address is not None:
        register['type_address'] = address['type']
        register['address'] = address['value']
    if document is not None:
        register['type_document'] = document['type']
        register['document'] = document['value']
    if type_error is not None:
        register['error'] = error
        register['type_error'] = type_error
        register[type_error['cod']] = type_error['value']
    if ubigeo is not None:
        register['type_address'] = ubigeo['type']
        register['department'] = ubigeo['department']
        register['province'] = ubigeo['province']
        register['district'] = ubigeo['district']

    return register

ERRORR_REGISTER = dict()
ERRORR_REGISTER['c_name_validate'] = makeDict(C_FIELD_NAME, u'Solo letras, espacios y guiones (-)', 'Carlos123')
ERRORR_REGISTER['c_name_min'] = makeDict(C_FIELD_NAME, C_MESSAGE_MIN % 2, 'C')
ERRORR_REGISTER['c_name_max'] = makeDict(C_FIELD_NAME, C_MESSAGE_MAX % 50, 'Carlos'*9)
ERRORR_REGISTER['c_name_required'] = makeDict(C_FIELD_NAME, C_MESSAGE_REQUIRED, '')

ERRORR_REGISTER['c_last_name_validate'] = makeDict(C_FIELD_LASTNAME, u'Solo letras, espacios y guiones (-)', 'Huamani$')
ERRORR_REGISTER['c_last_name_min'] = makeDict(C_FIELD_LASTNAME, C_MESSAGE_MIN % 2, 'H')
ERRORR_REGISTER['c_last_name_max'] = makeDict(C_FIELD_LASTNAME, C_MESSAGE_MAX % 50, 'Huamani'*10)
ERRORR_REGISTER['c_last_name_required'] = makeDict(C_FIELD_LASTNAME, C_MESSAGE_REQUIRED, '')

ERRORR_REGISTER['c_email_validate'] = makeDict(C_FIELD_EMAIL, u'Ingrese un email válido.', 'demo.pe')
ERRORR_REGISTER['c_email_max'] = makeDict(C_FIELD_EMAIL, C_MESSAGE_MAX % 50, '%s@hotmail.com'%('carlos'*10))
ERRORR_REGISTER['c_email_required'] = makeDict(C_FIELD_EMAIL, C_MESSAGE_REQUIRED, '')
ERRORR_REGISTER['c_email_unique'] = makeDict(C_FIELD_EMAIL, u'El email está siendo actualmente usado', 'carlos.hs.92@gmail.com')

ERRORR_REGISTER['c_password_min'] = makeDict(C_FIELD_PASSWORD, C_MESSAGE_MIN % 6, 'rwrw')
ERRORR_REGISTER['c_password_max'] = makeDict(C_FIELD_PASSWORD, C_MESSAGE_MAX % 20, 'rw'*20)
ERRORR_REGISTER['c_password_required'] = makeDict(C_FIELD_PASSWORD, C_MESSAGE_REQUIRED, '')
ERRORR_REGISTER['c_password_weak_1'] = makeDict(C_FIELD_PASSWORD, u'La contraseña ingresada es insegura.', '123456')
ERRORR_REGISTER['c_password_weak_2'] = makeDict(C_FIELD_PASSWORD, u'La contraseña ingresada es insegura.', 'abc123')
ERRORR_REGISTER['c_password_weak_3'] = makeDict(C_FIELD_PASSWORD, u'La contraseña ingresada es insegura.', 'qwerty')

ERRORR_REGISTER['c_confirm_validate'] = makeDict(C_FIELD_CONFIRM, u'No coincide con el campo contraseña', 'rwrwrwrw')
ERRORR_REGISTER['c_confirm_required'] = makeDict(C_FIELD_CONFIRM, C_MESSAGE_REQUIRED, '')
#ERRORR_REGISTER['c_confirm_max'] = makeDict('confirm', C_MESSAGE_MAX % 20) NECESITA UN MAX_LENGTH

ERRORR_REGISTER['c_document_dni_max'] = makeDict(C_FIELD_DOCUMENT, u'El DNI debe ser de 8 dígitos', '2562541152')
ERRORR_REGISTER['c_document_dni_min'] = makeDict(C_FIELD_DOCUMENT, u'El DNI debe ser de 8 dígitos', '25415')
ERRORR_REGISTER['c_document_dni_validate'] = makeDict(C_FIELD_DOCUMENT, u'Ingrese un DNI válido', '!"#$%&/(')
ERRORR_REGISTER['c_document_ruc_max'] = makeDict(C_FIELD_DOCUMENT, u'El RUC debe ser de 11 dígitos', '25415236598208')
ERRORR_REGISTER['c_document_ruc_min'] = makeDict(C_FIELD_DOCUMENT, u'El RUC debe ser de 11 dígitos', '25415')
ERRORR_REGISTER['c_document_ruc_validate'] = makeDict(C_FIELD_DOCUMENT, u'Ingrese un RUC válido', 'ASWQWERTYHU')
ERRORR_REGISTER['c_document_passport_max'] = makeDict(C_FIELD_DOCUMENT, u'Ingrese un máximo de 12 caracteres', '321456987456587')
#ERRORR_REGISTER['c_document_passport_min'] = makeDict(C_FIELD_DOCUMENT, 'Ingrese un pasaporte válido', '254')
ERRORR_REGISTER['c_document_passport_validate'] = makeDict(C_FIELD_DOCUMENT, u'Ingrese un pasaporte válido', '%&$"#$"')
ERRORR_REGISTER['c_document_card_max'] = makeDict(C_FIELD_DOCUMENT, u'Ingrese un máximo de 12 caracteres', '55789545354426')
#ERRORR_REGISTER['c_document_card_min'] = makeDict(C_FIELD_DOCUMENT, 'Ingrese un carnet de extranjería válido')
ERRORR_REGISTER['c_document_card_validate'] = makeDict(C_FIELD_DOCUMENT, u'Ingrese un carnet de extranjería válido', '#"$"#$')
ERRORR_REGISTER['c_document_required'] = makeDict(C_FIELD_DOCUMENT, C_MESSAGE_REQUIRED, '')

ERRORR_REGISTER['c_phone_1_min'] = makeDict(C_FIELD_PHONE_1, C_MESSAGE_MIN % 7, '54632')
ERRORR_REGISTER['c_phone_1_max'] = makeDict(C_FIELD_PHONE_1, C_MESSAGE_MAX % 10, '2312987541545')
ERRORR_REGISTER['c_phone_1_only_numbers'] = makeDict(C_FIELD_PHONE_1, C_MESSAGE_ONLY_NUMBERS, 'ASDQWEQWE')
ERRORR_REGISTER['c_phone_1_required'] = makeDict(C_FIELD_PHONE_1, C_MESSAGE_REQUIRED, '')

ERRORR_REGISTER['c_phone_2_min'] = makeDict(C_FIELD_PHONE_2, u'Ingrese un mínimo de 3 caracteres', '12')
ERRORR_REGISTER['c_phone_2_max'] = makeDict(C_FIELD_PHONE_2, u'Ingrese un máximo de 10 caracteres', '25445687584152')
ERRORR_REGISTER['c_phone_2_validate'] = makeDict(C_FIELD_PHONE_2, u'Sólo números, asterisco(*), guion(-) y numeral(#).', '!"#$%&/')

ERRORR_REGISTER['c_address_validate'] = makeDict(C_FIELD_ADDRESS, u"Solo letras, espacios, guiones (-) y apóstrofes (')", '&%$#$#$')
ERRORR_REGISTER['c_address_max'] = makeDict(C_FIELD_ADDRESS, C_MESSAGE_MAX % 150, 'JAJAJAJOJO'*20)

ERRORR_REGISTER['c_terms_required'] = makeDict(C_FIELD_CHECK_TERMS, C_MESSAGE_REQUIRED, False)

##-------------------------------------------------------------------------------------------------------------------
REGISTER = list()
REGISTER.append(makeRegister('registro_1'))

REGISTER.append(makeRegister('registro_2', type_error=ERRORR_REGISTER['c_name_validate']))
REGISTER.append(makeRegister('registro_3', type_error=ERRORR_REGISTER['c_name_min']))
REGISTER.append(makeRegister('registro_4', type_error=ERRORR_REGISTER['c_name_required']))
REGISTER.append(makeRegister('registro_5', error=False, type_error=ERRORR_REGISTER['c_last_name_max']))

REGISTER.append(makeRegister('registro_6', type_error=ERRORR_REGISTER['c_last_name_validate']))
REGISTER.append(makeRegister('registro_7', type_error=ERRORR_REGISTER['c_last_name_min']))
REGISTER.append(makeRegister('registro_8', type_error=ERRORR_REGISTER['c_last_name_required']))
REGISTER.append(makeRegister('registro_9', error=False, type_error=ERRORR_REGISTER['c_last_name_max']))

REGISTER.append(makeRegister('registro_10', type_error=ERRORR_REGISTER['c_email_required']))
REGISTER.append(makeRegister('registro_11', type_error=ERRORR_REGISTER['c_email_unique']))
REGISTER.append(makeRegister('registro_12', type_error=ERRORR_REGISTER['c_email_validate']))
REGISTER.append(makeRegister('registro_13', error=False, type_error=ERRORR_REGISTER['c_email_max']))

REGISTER.append(makeRegister('registro_14', type_error=ERRORR_REGISTER['c_password_min']))
REGISTER.append(makeRegister('registro_15', type_error=ERRORR_REGISTER['c_password_required']))
REGISTER.append(makeRegister('registro_16', error=False, type_error=ERRORR_REGISTER['c_password_max']))

REGISTER.append(makeRegister('registro_17', type_error=ERRORR_REGISTER['c_confirm_required']))
REGISTER.append(makeRegister('registro_18', type_error=ERRORR_REGISTER['c_confirm_validate']))

REGISTER.append(makeRegister('registro_19', type_error=ERRORR_REGISTER['c_document_dni_validate']))
REGISTER.append(makeRegister('registro_20', type_error=ERRORR_REGISTER['c_document_dni_min']))
REGISTER.append(makeRegister('registro_21', type_error=ERRORR_REGISTER['c_document_ruc_validate'], document={'type':'RUC', 'value':'-'}))
REGISTER.append(makeRegister('registro_22', type_error=ERRORR_REGISTER['c_document_ruc_min'], document={'type':'RUC', 'value':'-'}))
REGISTER.append(makeRegister('registro_23', type_error=ERRORR_REGISTER['c_document_passport_validate'], document={'type':'Pasaporte', 'value':'-'}))
REGISTER.append(makeRegister('registro_24', type_error=ERRORR_REGISTER['c_document_card_validate'], document={'type':'Carné de Extranjería', 'value':'-'}))
REGISTER.append(makeRegister('registro_25', type_error=ERRORR_REGISTER['c_document_required']))
REGISTER.append(makeRegister('registro_26', type_error=ERRORR_REGISTER['c_phone_1_min']))
REGISTER.append(makeRegister('registro_27', type_error=ERRORR_REGISTER['c_phone_1_only_numbers']))
REGISTER.append(makeRegister('registro_28', type_error=ERRORR_REGISTER['c_phone_1_required']))
REGISTER.append(makeRegister('registro_29', type_error=ERRORR_REGISTER['c_phone_2_min']))
REGISTER.append(makeRegister('registro_30', type_error=ERRORR_REGISTER['c_phone_2_validate']))
REGISTER.append(makeRegister('registro_31', type_error=ERRORR_REGISTER['c_address_validate']))
REGISTER.append(makeRegister('registro_32', type_error=ERRORR_REGISTER['c_terms_required']))
REGISTER.append(makeRegister('registro_33', type_error=ERRORR_REGISTER['c_password_weak_1']))
REGISTER.append(makeRegister('registro_34', type_error=ERRORR_REGISTER['c_password_weak_2']))
REGISTER.append(makeRegister('registro_35', type_error=ERRORR_REGISTER['c_password_weak_3']))
