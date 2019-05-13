
from selenium import webdriver
import unittest
import time

var_teste =	{
  "url": 'https://teamshift-qa.crossknowledge.com//'
}

# Creating a class as a pattern in unittest
class TestAuto(unittest.TestCase):
    #special methods
    def setUp(self): #setup initializate
        self.browser = webdriver.Firefox()

    def teststart(self):

        #01. Acessar o site: https://teamshift-qa.crossknowledge.com//
        self.browser.get(var_teste['url'])

        #02. Clicar no botão entrar
        self.browser.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Você não tem mais acesso ao TeamSHIFT.'])[1]/preceding::button[1]").click()

        #03. Clicar no campo E-mail
        self.browser.find_element_by_id("login-form__login").click()

        #04. Inserir E-mail
        self.browser.find_element_by_id("login-form__login").send_keys("maicon.figureredo@fakedominio.com")

        #05. Clicar no botão Próximo
        self.browser.find_element_by_xpath("//button[@type='submit'][@data-login-translation='Login']").click()

        #06. Inserir senha
        time.sleep(3)
        self.browser.find_element_by_id("login-form__password").send_keys("Nomade@1991")

        #07. Clicar no botão Login
        self.browser.find_element_by_xpath("//button[@data-login-translation='Login']").click()

        #08. Validar login no sistema
        time.sleep(5)
        self.assertTrue(self.browser.find_element_by_xpath("/html/body/main/header/nav/div[2]/ul/li[1]").text, 'Home')


    #def tearDown(self):# quit browser
        self.browser.quit()
