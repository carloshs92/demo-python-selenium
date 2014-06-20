# -*- coding: utf-8 -*-
from form_input_data import register
from selenium import webdriver
from form_keys import *
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest

class PruebasDeRegistro(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://paginadeprueba.pe/registro"
        self.verificationErrors = []
        self.accept_next_alert = False
        self.debug = False

    def printText(self, text):
        if self.debug:
            print text

    def test_pruebas_de_registro(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("a.fancybox-item.fancybox-close").click()

        for data in register.getList():
            print u'--> Probando la prueba: %s ' % data['cod']
            driver.find_element_by_id(FIELD_NAME).clear()
            driver.find_element_by_id(FIELD_NAME).send_keys(data[FIELD_NAME])
            self.printText( 'nombre ingresado')

            driver.find_element_by_id(FIELD_LASTNAME).clear()
            driver.find_element_by_id(FIELD_LASTNAME).send_keys(data[FIELD_LASTNAME])
            self.printText('apellido ingresado')

            driver.find_element_by_css_selector("div.form_control.relative > #txtEmail").clear()
            driver.find_element_by_css_selector("div.form_control.relative > #txtEmail").send_keys(data[FIELD_EMAIL])
            self.printText( 'correo ingresado' )

            driver.find_element_by_id(FIELD_PASSWORD).clear()
            driver.find_element_by_id(FIELD_PASSWORD).send_keys(data[FIELD_PASSWORD])
            self.printText( 'contraseña ingresado')

            driver.find_element_by_id(FIELD_CONFIRM).clear()
            driver.find_element_by_id(FIELD_CONFIRM).send_keys(data[FIELD_CONFIRM])
            self.printText( 'contraseña repetida ingresado')

            Select(driver.find_element_by_id(SELECT_DOCUMENT)).select_by_visible_text(data[FIELD_DOCUMENT].keys()[0])
            driver.find_element_by_id(FIELD_DOCUMENT).clear()
            driver.find_element_by_id(FIELD_DOCUMENT).send_keys(data[FIELD_DOCUMENT][data[FIELD_DOCUMENT].keys()[0]])
            self.printText( 'documento ingresado')

            if data[FIELD_CHECK_TERMS]:
                driver.find_element_by_id(FIELD_CHECK_TERMS).click()
                self.printText( 'checks ingresado')

            if data['is_error']:
                if data['error']['location']== FIELD_EMAIL:
                    error_id = driver.find_element_by_css_selector("div.form_control.relative > #txtEmail").get_attribute('data-parsley-id')
                else:
                    driver.find_element_by_id(SUBMIT_REGISTER).click()
                    error_id = driver.find_element_by_id(data['error']['location']).get_attribute('data-parsley-id')

                message = driver.find_element_by_css_selector('#parsley-id-%s > li' % error_id).text
                assert data['error']['message'] == message, u'Mensaje erroneo en la prueba: %s , %s == %s' % (data['cod'], data['error']['message'], message)
                print u'--> Exito en %s el campo %s dio como mensaje %s al ingresar %s' % (data['cod'], data['error']['location'], data['error']['message'], data['error']['value'])

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
