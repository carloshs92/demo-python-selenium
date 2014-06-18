# -*- coding: utf-8 -*-
from register import CreateRegister

C_FIELD_NAME = 'txtName'
C_FIELD_LASTNAME = 'txtLastName'
C_FIELD_EMAIL = 'txtEmail'
C_FIELD_PASSWORD = 'txtPassword1'
C_FIELD_CONFIRM = 'txtRepeatPassword'
C_FIELD_DOCUMENT = 'txtDocument'
C_FIELD_PHONE_1 = 'txtPhone1'
C_FIELD_PHONE_2 = 'txtPhone2'
C_FIELD_CHECK_TERMS = 'chkTerms'

modelo = dict()
modelo[C_FIELD_NAME] = 'Carlos'
modelo[C_FIELD_LASTNAME] = 'Huamani'
modelo[C_FIELD_EMAIL] = 'carlos.hs.92@gmail.com'
modelo[C_FIELD_PASSWORD] = 'carlos123'
modelo[C_FIELD_CONFIRM] = 'carlos123'
modelo[C_FIELD_DOCUMENT] = {'DNI':'54264895','RUC':'254152458963','Pasaporte':'4587DA45','Carné de Extranjería':'584E4E5D5'}
modelo[C_FIELD_PHONE_1] = '4875962'
modelo[C_FIELD_PHONE_2] = '99784562'
modelo[C_FIELD_CHECK_TERMS] = True

REGISTER = CreateRegister(modelo)

REGISTER.addError(C_FIELD_NAME, 'c_name_validate',  u'Solo letras, espacios y guiones (-)', u'###!!??¡¡')