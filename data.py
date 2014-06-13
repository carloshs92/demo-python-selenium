# -*- coding: utf-8 -*-
C_MESSAGE_REQUIRED = 'Este campo es requerido.'
C_MESSAGE_MAX = 'La longitud máxima es de %d caracteres.'
C_MESSAGE_MIN = 'La longitud mínima es de %d caracteres.'

def makeDict(location, description):
    return {'location': location, 'description': description}

ERRORR_REGISTER = dict()

ERRORR_REGISTER['c_name_letter'] = makeDict('name', 'Solo letras, espacios y guiones (-)')
ERRORR_REGISTER['c_name_min'] = makeDict('name', C_MESSAGE_MIN % 2)
ERRORR_REGISTER['c_name_max'] = makeDict('name', C_MESSAGE_MAX % 50)
ERRORR_REGISTER['c_name_required'] = makeDict('name', C_MESSAGE_REQUIRED)

ERRORR_REGISTER['c_lastname_letter'] = makeDict('location', 'Solo letras, espacios y guiones (-)')
ERRORR_REGISTER['c_lastname_min'] = makeDict('location', C_MESSAGE_MIN % 2)
ERRORR_REGISTER['c_lastname_max'] = makeDict('location', C_MESSAGE_MAX % 50)
ERRORR_REGISTER['c_name_required'] = makeDict('location', C_MESSAGE_REQUIRED)

ERRORR_REGISTER['c_email_validate'] = makeDict('email', 'Ingrese un email válido.')
ERRORR_REGISTER['c_email_max'] = makeDict('email', C_MESSAGE_MAX % 50)
ERRORR_REGISTER['c_email_required'] = makeDict('email', C_MESSAGE_REQUIRED)

ERRORR_REGISTER['c_password_min'] = makeDict('password', C_MESSAGE_MIN % 6)
ERRORR_REGISTER['c_password_max'] = makeDict('password', C_MESSAGE_MAX % 20)
ERRORR_REGISTER['c_password_required'] = makeDict('password', C_MESSAGE_REQUIRED)

ERRORR_REGISTER['c_confirm_validate'] = makeDict('confirm', 'No coincide con el campo contraseña')
ERRORR_REGISTER['c_confirm_required'] = makeDict('confirm', C_MESSAGE_REQUIRED)

REGISTER = list()
REGISTER.append({'error': False,
             'name': 'Carlos', 'last_name': 'Huamani', 'email':'carlos.hs.92@gmail.com',
             'password': 'carlos123', 'password_confirm':'carlos_123',
             'type_document':'DNI','document':'25413698',
             'phone1':'4569877', 'phone2':'45263299',
             'type_direction':'Calle','direccion':'Jose Galvez 123',
             'ubigeo': False})