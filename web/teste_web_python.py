#1 Importar Bibliotecas
import time

from selenium import webdriver
import pytest


#2 Classe
class Test_selenium_webdriver():
    # Definição de Inicio - Executa antes do teste
    def setup_method(self):
        #Declarar o objeto do Selenium e instanciar como o navegador desejado
        self.driver =  webdriver.Chrome()
        self.driver.implicitly_wait(30) # Selenium irá esperar até 30 segs pelos elementos
        self.driver.maximize_window() # Maximizar a janela do navegador

    # Definição de Fim - Executa depois do teste
    def teardown_method(self):
        # Destruir o objeto do Selenium
        self.driver.quit()

    # Definição do Teste
    def testar_comprar_curso_python(self):
        # O Selenium abre a URL indicada - site alvo do teste
        self.driver.get('https://www.iterasys.com.br')
        # Selenium abre cursos
        self.driver.find_element('xpath', '//*[@id="16237702146520"]/div').click()
        time.sleep(3)
        # Selenium clica em aceitar os cookies
        self.driver.find_element('xpath', '//*[@id="page"]/div[4]/div[3]/button[2]/span/span').click()
        # Selenium clica no elemento de busca
        self.driver.find_element('xpath', '/html/body/div/div/div/div[1]/main/div/section/div/div/div/div/div/div[2]/div/div/div/input').click()
        # Selenium digita 'python' no campo de busca
        self.driver.find_element('xpath', '/html/body/div/div/div/div[1]/main/div/section/div/div/div/div/div/div[2]/div/div/div/input').send_keys('python')
        time.sleep(2)
        # Selenium encontra o produto 'python'
        self.driver.find_element('xpath', '/html/body/div/div/div/div[1]/main/div/section/div/div/div/div/main/a/main/h3').click()
        time.sleep(1)
        # Selenium verifica o valor do curso
        assert self.driver.find_element('xpath', '/html/body/div/div/div/div[1]/main/div[1]/div/section/div/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/p').text == 'R$ 27,90'








