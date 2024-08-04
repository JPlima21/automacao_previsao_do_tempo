from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementNotSelectableException, TimeoutException, WebDriverException
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

    #Tratamento de erro
    print('Acessando o site...')
    try:
        driver.get(url)
        sleep(1)
    except TimeoutException as e:
        print(f'Erro ao acessar o site {url} : {e}')
        return None
    except WebDriverException as e:
        print(f'Erro ao acessar o site {url} : {e}')
        return None
    
    print('Pegando informações...')
    try:
        pesquisa = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@class="search-input"]')))
        sleep(1)
        pesquisa.send_keys('Fortaleza ceará' + Keys.ENTER)
        sleep(1)
        wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="temp-container"]/div[@class="temp"]')))
        wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="real-feel"]')))
        wait.until(EC.presence_of_all_elements_located((By.XPATH,'//span[@class="phrase"]')))
        
        #Pegando a temperatura atual, sensação termica e condição atual
        temp_atual = driver.find_element(By.XPATH,'//div[@class="temp-container"]/div[@class="temp"]')
        sensacao_termica = driver.find_element(By.XPATH,'//div[@class="real-feel"]')
        condicao_temp = driver.find_element(By.XPATH,'//span[@class="phrase"]')

        sensacao_texto = sensacao_termica.text
        atual_texto = temp_atual.text
        condicao_texto = condicao_temp.text

        print(condicao_texto)
        print(f' temperatura atual: {atual_texto}')
        print(sensacao_texto + 'C')
    except:
        print(f'Erro! elemento não encontrado')

    finally:
        driver.quit()

def email():
    pass

def exe_script():
    driver, wait = config_driver()
    get_weather(driver, wait)

exe_script()