import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from src.Functions.Function import Function_Test


class Test1(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path="../driver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://test-qa.inlaze.com/auth/sign-in')
        self.driver.maximize_window()
        t = 2

    def test_1_register(self):  # Funcion para logear y llenar campos
        f = Function_Test(self.driver)
        f.register_User()

    def test_2_login_fallido(self):  # Funcion login erroneo
        f = Function_Test(self.driver)
        f.login_fallido()

    def test_3_login_exitoso(self):  # Funcion login exitoso
        f = Function_Test(self.driver)
        f.login_exitoso()

    def test_4_logout(self):  # Funcion logout exitoso
        f = Function_Test(self.driver)
        f.logout()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()