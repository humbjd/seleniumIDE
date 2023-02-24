
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTeste():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(30) # o robo ira esperar ate 30 segundos
    self.driver.maximize_window() #Maximizar janela do navegagor
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_teste(self):
    self.driver.get("https://www.uol.com.br/")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.ID, "lehaq8nt").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(4) > a")
    actions = ActionChains(self.driver)
    time.sleep(3)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(3) > a")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(3) > a").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".destaque .thumb-title").click()
    self.driver.find_element(By.CSS_SELECTOR, ".logo-uol-svg").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".hyperlink > div > .icon__image")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.execute_script("window.scrollTo(0,1204)")
    self.driver.execute_script("window.scrollTo(0,1800.800048828125)")
    self.driver.find_element(By.ID, "leh6r9fh").click()
  
