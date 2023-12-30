import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class FormPratice (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_perfect_form(self):
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")
        elem = driver.find_element(By.ID, "firstName")
        elem.send_keys("CAMARO")
        elem = driver.find_element(By.ID, "lastName")
        elem.send_keys("AMARELO")
        elem = driver.find_element(By.ID, "userEmail")
        elem.send_keys("camaro@amarelo.com")
        select = driver.find_element(By.ID, 'gender-radio-1')
        driver.execute_script("arguments[0].click();", select)
        elem = driver.find_element(By.ID, "userNumber")
        elem.send_keys("6940028922",Keys.TAB)
        elem = driver.find_element(By.ID, "react-select-3-input")
        elem.send_keys("NCR", Keys.TAB)
        elem = driver.find_element(By.ID, "react-select-4-input")
        elem.send_keys("Noida",Keys.TAB)
        elem.send_keys(Keys.ENTER)
        sleep(5)
        try:
            elemento_confirmacao = self.driver.find_element(By.ID, "example-modal-sizes-title-lg")
            self.assertTrue(elemento_confirmacao.is_displayed())
            print("Formulário enviado com sucesso")
        except NoSuchElementException:
            print("O envio do formulário não pôde ser efetuado")

    def test_invalid_email_form(self):
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")
        elem = driver.find_element(By.ID, "firstName")
        elem.send_keys("CAMARO")
        elem = driver.find_element(By.ID, "lastName")
        elem.send_keys("AMARELO")
        elem = driver.find_element(By.ID, "userEmail")
        elem.send_keys("camaroamarelo")
        select = driver.find_element(By.ID, 'gender-radio-1')
        driver.execute_script("arguments[0].click();", select)
        elem = driver.find_element(By.ID, "userNumber")
        elem.send_keys("6940028922",Keys.TAB)
        elem = driver.find_element(By.ID, "react-select-3-input")
        elem.send_keys("NCR", Keys.TAB)
        elem = driver.find_element(By.ID, "react-select-4-input")
        elem.send_keys("Noida",Keys.TAB)
        elem.send_keys(Keys.ENTER)
        sleep(5)
        try:
            elemento_confirmacao = self.driver.find_element(By.ID, "example-modal-sizes-title-lg")
            self.assertFalse(elemento_confirmacao.is_displayed())

        except NoSuchElementException:
            print("O envio do formulário não pôde ser efetuado, email inválido")

    def test_blank_form(self):
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")
        elem = driver.find_element(By.ID, "userNumber")        
        elem = driver.find_element(By.ID, "react-select-3-input")
        elem.send_keys(Keys.TAB)
        elem.send_keys(Keys.TAB)
        elem.send_keys(Keys.ENTER)
        sleep(5)
        try:
            elemento_confirmacao = self.driver.find_element(By.ID, "example-modal-sizes-title-lg")
            self.assertFalse(elemento_confirmacao.is_displayed())

        except NoSuchElementException:
            print("O envio do formulário não pôde ser efetuado, formulário em branco")
    
    def test_invalid_number_form(self):
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")
        elem = driver.find_element(By.ID, "firstName")
        elem.send_keys("CAMARO")
        elem = driver.find_element(By.ID, "lastName")
        elem.send_keys("AMARELO")
        elem = driver.find_element(By.ID, "userEmail")
        elem.send_keys("camaro@amarelo.com")
        select = driver.find_element(By.ID, 'gender-radio-1')
        driver.execute_script("arguments[0].click();", select)
        elem = driver.find_element(By.ID, "userNumber")
        elem.send_keys("40028922",Keys.TAB)
        elem = driver.find_element(By.ID, "react-select-3-input")
        elem.send_keys("NCR", Keys.TAB)
        elem = driver.find_element(By.ID, "react-select-4-input")
        elem.send_keys("Noida",Keys.TAB)
        elem.send_keys(Keys.ENTER)
        sleep(5)
        try:
            elemento_confirmacao = self.driver.find_element(By.ID, "example-modal-sizes-title-lg")
            self.assertFalse(elemento_confirmacao.is_displayed())
        except NoSuchElementException:
            print("O envio do formulário não pôde ser efetuado, número de contato inválido")

    def test_reset_form(self):
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")
        elem = driver.find_element(By.ID, "firstName")
        elem.send_keys("CAMARO")
        elem = driver.find_element(By.ID, "lastName")
        elem.send_keys("AMARELO")
        elem = driver.find_element(By.ID, "userEmail")
        elem.send_keys("camaro@amarelo.com")
        select = driver.find_element(By.ID, 'gender-radio-1')
        driver.execute_script("arguments[0].click();", select)
        elem = driver.find_element(By.ID, "userNumber")
        elem.send_keys("6940028922",Keys.TAB)
        elem = driver.find_element(By.ID, "react-select-3-input")
        elem.send_keys("NCR", Keys.TAB)
        elem = driver.find_element(By.ID, "react-select-4-input")
        elem.send_keys("Noida")
        driver.refresh()
        sleep(5)
        elem = driver.find_element(By.ID, "firstName")
        self.assertFalse(elem.get_attribute("value")=="CAMARO")
        elem = driver.find_element(By.ID, "lastName")
        self.assertFalse(elem.get_attribute("value")=="AMARELO")
        elem = driver.find_element(By.ID, "userEmail")
        self.assertFalse(elem.get_attribute("value")=="camaro@amarelo.com")
        elem = driver.find_element(By.ID, "userNumber")
        self.assertFalse(elem.get_attribute("value")=="6940028922")
        try:
            elemento_confirmacao = self.driver.find_element(By.ID, "example-modal-sizes-title-lg")
            self.assertFalse(elemento_confirmacao.is_displayed())
        except NoSuchElementException:
            print("O envio do formulário não pôde ser efetuado, formulário recarregado")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()