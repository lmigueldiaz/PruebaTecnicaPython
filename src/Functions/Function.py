import time

from selenium.webdriver.common.by import By


class Function_Test():

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        email = self.driver.find_element(By.XPATH, "//*[@id='email']")
        email.send_keys("lmigueldiazf@gmail.com")
        password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        password.send_keys("16Ilanze*")
        time.sleep(1)
        clic_button_sign = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        clic_button_sign.click()

    def register_User(self):
        clic_sign_up = self.driver.find_element(By.XPATH,
                                                "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/span/a")
        clic_sign_up.click()
        time.sleep(3)
        full_name = self.driver.find_element(By.XPATH, "//*[@id='full-name']")
        full_name.send_keys("Luis Diaz")
        email = self.driver.find_element(By.XPATH, "//*[@id='email']")
        email.send_keys("lmigueldiazf@gmail.com")
        time.sleep(1)
        password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        password.send_keys("16Ilanze*")
        confirm_password = self.driver.find_element(By.XPATH, "//input[@id='confirm-password']")
        confirm_password.send_keys("16Ilanze*")
        time.sleep(2)
        clic_button_sign = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        clic_button_sign.click()
        time.sleep(2)
        registro_exitoso = self.driver.find_element(By.XPATH, "//div[contains(@class, 'ml-3')]").text
        print(registro_exitoso)

    def login_fallido(self):
        email = self.driver.find_element(By.XPATH, "//*[@id='email']")
        email.send_keys("lmigueldiazf@yopmail.com")
        password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        password.send_keys("16Ilanze*")
        time.sleep(1)
        clic_button_sign = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        clic_button_sign.click()
        time.sleep(2)
        login_fallido = self.driver.find_element(By.XPATH, "//div[contains(@class, 'ml-3')]").text
        print(login_fallido)

    def login_exitoso(self):
        Function_Test.login(self)
        time.sleep(2)
        validar_nombre = self.driver.find_element(By.XPATH, "//h2[@class='font-bold']").text
        print(validar_nombre)

    def logout(self):
        Function_Test.login(self)
        time.sleep(2)
        clic_button_perfil = self.driver.find_element(By.XPATH,
                                                      "//img[@src='/assets/rengoku.webp']")
        clic_button_perfil.click()
        time.sleep(1)
        clic_button_logout = self.driver.find_element(By.XPATH,
                                                      "/html/body/app-root/app-panel-root/app-navbar/div/div[2]/div/ul/li[3]/a")
        clic_button_logout.click()