#1 Importar Bibliotecas
from selenium import webdriver
import pytest


#2 Classe
class Test_selenium_webdriver():
    # Definição de Inicio - Executa antes do teste
    def setup_method(self):
        #Declarar o objeto do Selenium e instanciar como o navegador desejado
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30) # Selenium irá esperar até 30 segs pelos elementos
        self.driver.maximize_window() # Maximizar a janela do navegador

    # Definição de Fim - Executa depois do teste
    def teardown_method(self):
        # Destruir o objeto do Selenium
        self.driver.quit()

    # Definição do Teste
    def testar_comprar_curso_mantis(self):
        # O Selenium abre a URL indicada - site alvo do teste
        self.driver.get('https://www.iterasys.com.br')
        self.driver.find_element('xpath', '//*[@id="16237702146520"]/div').click()
        self.driver.find_element(By.ID, 'auto-i-5363671004826667').send_keys('python')
        self.driver.find_element(By.CLASS, 'content-card-name variant-primary').click()









