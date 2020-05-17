from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path=r'./chromedriver')

codigos = ["usuário_teste"]

senhas = ["213nj5"]

class Vamos:
	def _init_(self):
		
		options = webdriver.ChromeOptions()

		options.add_argument('lang=pt-br')

		

	def Login(self):
		driver.get('site-para-login')
		time.sleep(5)
		tam = len(codigos)
		for i in range(tam):
			chat_login = driver.find_element_by_xpath(f"//input[@class='jss47']")
			chat_login.click()
			time.sleep (2)

			chat_login.send_keys(codigos[i])
			chat_login = driver.find_element_by_xpath(f"//input[@type='password']")
			chat_login.click()
			time.sleep(2)
	
			chat_login.send_keys(senhas[i])
			chat_login = driver.find_element_by_class_name('jss64')
			chat_login.click()
			time.sleep(5)

						
			#BLOCO FUNCIONANDO---------------------------------------------------------------
			driver.get('https://escolha-qual-pagina-sera-aberta-utilizando-os-cookies-de-login-ativos-na-sesao')
			time.sleep(7)
			
bot = Vamos()
bot.Login()
