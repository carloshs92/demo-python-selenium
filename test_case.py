# -*- coding: utf-8 -*-
from time import sleep
from form_input_data import register
from selenium import webdriver
from form_keys import *
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest

class PruebasDeRegistro(unittest.TestCase):
    def setUp(self):
        self.binary = FirefoxBinary('/usr/bin/firefox/firefox')
        #self.driver = webdriver.Chrome('/usr/bin/chromedriver')
        self.driver = webdriver.Firefox(firefox_binary=self.binary)
        self.driver.implicitly_wait(30)
        self.base_url = "http://local.ofertop.pe/registro"
        self.verificationErrors = []
        self.accept_next_alert = False
        self.debug = False

    def printText(self, text):
        if self.debug:
            print text
    def waitFor(self, seconds):
        i = 0
        while seconds > i:
            i += 1
            print u'--> Esperando %d segundo(s)...' % i
            sleep(1)
    def test_pruebas_de_registro(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        #driver.find_element_by_css_selector("a.fancybox-item.fancybox-close").click()
        #driver.find_element_by_css_selector(u"li.register_link > a[title=\"Regístrate\"]").click()
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

            driver.find_element_by_id(FIELD_PHONE_1).clear()
            driver.find_element_by_id(FIELD_PHONE_1).send_keys(data[FIELD_PHONE_1])
            self.printText( 'telefono 1 ingresado')

            driver.find_element_by_id(FIELD_PHONE_2).clear()
            driver.find_element_by_id(FIELD_PHONE_2).send_keys(data[FIELD_PHONE_2])
            self.printText( 'telefono 2 ingresado')

            #Select(driver.find_element_by_id("selAddress")).select_by_visible_text(data['type_address'])
            #driver.find_element_by_id("txtAddress").clear()
            #driver.find_element_by_id("txtAddress").send_keys(data['address'])
            #self.printText( 'direccion ingresado')


            #if data['select_ubigeo']:
            #    Select(driver.find_element_by_id("selProvince")).select_by_visible_text("Oyon")
            #    Select(driver.find_element_by_id("selDistrict")).select_by_visible_text("Caujul")
            #    self.printText( 'ubigeo ingresado')

            if data[FIELD_CHECK_TERMS]:
                driver.find_element_by_id(FIELD_CHECK_TERMS).click()
                self.printText( 'checks ingresado')

            #driver.find_element_by_id("sbmRegister").click()

            if data['is_error']:
                if data['error']['location']== FIELD_EMAIL:
                    self.waitFor(6)
                    error_id = driver.find_element_by_css_selector("div.form_control.relative > #txtEmail").get_attribute('data-parsley-id')
                else:
                    driver.find_element_by_id(SUBMIT_REGISTER).click()
                    error_id = driver.find_element_by_id(data['error']['location']).get_attribute('data-parsley-id')

                if data[FIELD_CHECK_TERMS] == False:
                    message = driver.find_element_by_css_selector('#parsley-id-multiple-terminos > li').text
                else:
                    message = driver.find_element_by_css_selector('#parsley-id-%s > li' % error_id).text
                assert data['error']['message'] == message, u'Mensaje erroneo en la prueba: %s , %s == %s' % (data['cod'], data['error']['message'], message)
                print u'--> Exito en %s el campo %s dio como mensaje %s al ingresar %s' % (data['cod'], data['error']['location'], data['error']['message'], data['error']['value'])



            if data['chkTerms']:
                driver.find_element_by_id("chkTerms").click()
                self.printText( 'checks ingresado')

            #driver.find_element_by_css_selector(u"li.register_link > a[title=\"Regístrate\"]").click()
            #driver.find_element_by_css_selector("a.fancybox-item.fancybox-close").click()
    
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
