from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def config_driver():
    chrome_option = webdriver.ChromeOptions()
    #configurações do navegador/site
    arguments = ['--lang=pt-br','--window-size=1200,1000', '--incognito','--disable-site-isolation-trials']

    #Loop para add argumentos no ChromeOptions
    for argument in arguments:
        chrome_option.add_argument(argument)

    driver = webdriver.Chrome(options=chrome_option)
    
    wait = WebDriverWait(
        driver, 
        timeout=10, 
        poll_frequency=2,
        ignored_exceptions=[NoSuchElementException, ElementNotInteractableException, ElementNotSelectableException]
    )
    return driver, wait

#Pegar informações do site
def get_weather(driver, wait):
    driver, wait = config_driver()
    url = 'https://www.accuweather.com/pt/world-weather'

    driver.get(url)
    sleep(1)
    pesquisa = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@class="search-input"]')))
    #pesquisa.click()
    sleep(1)
    pesquisa.send_keys('Fortaleza ceará' + Keys.ENTER)
    sleep(3)

    driver.quit()


def exe_script():
    driver, wait = config_driver()
    get_weather(driver, wait)

exe_script()