# -*- coding: utf-8 -*-
from data import REGISTER
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest, time, re

class PruebasDeRegistro(unittest.TestCase):
    def setUp(self):
        self.binary = FirefoxBinary('/usr/bin/firefox/firefox')
        self.driver = webdriver.Firefox(firefox_binary=self.binary)
        self.driver.implicitly_wait(90)
        self.base_url = "http://local.ofertop.pe/"
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
        driver.find_element_by_css_selector(u"li.register_link > a[title=\"Regístrate\"]").click()
        driver.find_element_by_css_selector("a.fancybox-item.fancybox-close").click()

        for data in REGISTER:
            print data['prueba']
            driver.find_element_by_id("txtName").clear()
            driver.find_element_by_id("txtName").send_keys(data['name'])
            self.printText( 'nombre ingresado')

            driver.find_element_by_id("txtLastName").clear()
            driver.find_element_by_id("txtLastName").send_keys(data['last_name'])
            self.printText('apellido ingresado')

            driver.find_element_by_css_selector("div.form_control.relative > #txtEmail").clear()
            driver.find_element_by_css_selector("div.form_control.relative > #txtEmail").send_keys(data['email'])
            self.printText( 'correo ingresado' )

            driver.find_element_by_id("txtPassword1").clear()
            driver.find_element_by_id("txtPassword1").send_keys(data['password'])
            self.printText( 'contraseña ingresado')

            driver.find_element_by_id("txtRepeatPassword").clear()
            driver.find_element_by_id("txtRepeatPassword").send_keys(data['confirm'])
            self.printText( 'contraseña repetida ingresado')

            Select(driver.find_element_by_id("selDocument")).select_by_visible_text(data['type_document'])
            driver.find_element_by_id("txtDocument").clear()
            driver.find_element_by_id("txtDocument").send_keys(data['document'])
            self.printText( 'documento ingresado')

            driver.find_element_by_id("txtPhone1").clear()
            driver.find_element_by_id("txtPhone1").send_keys(data['phone_1'])
            self.printText( 'telefono 1 ingresado')

            driver.find_element_by_id("txtPhone2").clear()
            driver.find_element_by_id("txtPhone2").send_keys(data['phone_2'])
            self.printText( 'telefono 2 ingresado')

            Select(driver.find_element_by_id("selAddress")).select_by_visible_text(data['type_address'])
            driver.find_element_by_id("txtAddress").clear()
            driver.find_element_by_id("txtAddress").send_keys(data['address'])
            self.printText( 'direccion ingresado')


            if data['select_ubigeo']:
                Select(driver.find_element_by_id("selProvince")).select_by_visible_text("Oyon")
                Select(driver.find_element_by_id("selDistrict")).select_by_visible_text("Caujul")
                self.printText( 'ubigeo ingresado')

            if data['check_terms']:
                driver.find_element_by_id("chkTerms").click()
                self.printText( 'checks ingresado')

            #driver.find_element_by_id("sbmRegister").click()

            if data['check_terms']:
                driver.find_element_by_id("chkTerms").click()
                self.printText( 'checks ingresado')

            if data['error']:
                if data['type_error']['location'] != 'txtEmail':
                    error_id = driver.find_element_by_id(data['type_error']['location']).get_attribute('data-parsley-id')
                else:
                    error_id = driver.find_element_by_css_selector("div.form_control.relative > #txtEmail").get_attribute('data-parsley-id')
                print error_id
                message = driver.find_element_by_css_selector('#parsley-id-%s > li' % error_id).text
                assert data['type_error']['description'] == message, u'Mensaje erroneo en la prueba: %s , %s == %s' % (data['prueba'], data['type_error']['description'], message)
                print u'Exito en %s' % data['type_error']['description']


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
