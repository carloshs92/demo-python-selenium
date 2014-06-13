# -*- coding: utf-8 -*-
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
        self.driver.implicitly_wait(30)
        self.base_url = "http://local.ofertop.pe/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_pruebas_de_registro(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("a.fancybox-item.fancybox-close").click()
        driver.find_element_by_css_selector(u"li.register_link > a[title=\"Regístrate\"]").click()
        driver.find_element_by_css_selector("a.fancybox-item.fancybox-close").click()

        driver.find_element_by_id("txtName").clear()
        driver.find_element_by_id("txtName").send_keys("prueba")
        driver.find_element_by_id("txtLastName").clear()
        driver.find_element_by_id("txtLastName").send_keys("demo")
        driver.find_element_by_css_selector("div.form_control.relative > #txtEmail").clear()
        driver.find_element_by_css_selector("div.form_control.relative > #txtEmail").send_keys("carlos.hs.92@demo.com")
        driver.find_element_by_id("txtPassword1").clear()
        driver.find_element_by_id("txtPassword1").send_keys("carlos123")
        driver.find_element_by_id("txtRepeatPassword").clear()
        driver.find_element_by_id("txtRepeatPassword").send_keys("carlos123")
        driver.find_element_by_id("txtDocument").clear()
        driver.find_element_by_id("txtDocument").send_keys("46941256")
        driver.find_element_by_id("txtPhone1").clear()
        driver.find_element_by_id("txtPhone1").send_keys("25415231")
        driver.find_element_by_id("txtPhone2").clear()
        driver.find_element_by_id("txtPhone2").send_keys("1155995588")
        Select(driver.find_element_by_id("selAddress")).select_by_visible_text("Calle")
        driver.find_element_by_id("txtAddress").clear()
        driver.find_element_by_id("txtAddress").send_keys("Santa Anita")
        Select(driver.find_element_by_id("selProvince")).select_by_visible_text("Oyon")
        Select(driver.find_element_by_id("selDistrict")).select_by_visible_text("Caujul")
        driver.find_element_by_id("chkTerms").click()

        driver.find_element_by_id("sbmRegister").click()
    
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
