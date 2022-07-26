from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import urllib.request
import os
from configparser import ConfigParser


#TEST ITEM

nikeURL = 'https://www.nike.com/t/mens-basketball-t-shirt-RxlfV9/DV1214-100'




def setupConfig(file: str) -> ConfigParser:
	print("Parsing Configuration...")
	config = ConfigParser()
	config.read("file")
	return config

class CheckoutBot():
	'''Bot automates purchasing a product given a product URL, credentials and size/color'''
	def __init__(self,config, URL, size, color):

		self.driver = webdriver.Safari()
		self.action = ActionChains(driver)

		self.username = config.get("NIKE_ACCOUNT", "USERNAME")
		self.password = config.get("NIKE_ACCOUNT", "PASSWORD")
		self.ID = config.get("NIKE_ACCOUNT", "ID")
		self.card = config.get("CREDIT_CARD", "CCNUM")
		self.ccsecurity = config.get("CREDIT_CARD", "CCV")
		self.expiration_month = config.get("CREDIT_CARD", "EXPM")
		self.expiration_year = config.get("CREDIT_CARD", "EXPY")
		self.URL = URL

	def login(self) -> None:
		'''Uses the webdriver to locate the login fields and logs the user in using the passed credentials'''
		driver.get(self.URL)
		signButtonClass = 'nav-btn p0-sm d-sm-b body-4 u-bold ml2-sm mr2-sm'
		loginButtonId = '192ffd08-4d60-408c-8c75-821cad9c0cc7'
		passwordButtonId = '3104580a-d23b-43d1-8782-babc5be49fad'
		
		signInElement = driver.find_element(BY.CLASS_NAME, signButtonClass)
		loginElement = driver.find_element(By.ID, loginButtonId)
		passwordElement = driver.find_element(By.ID, passwordButtonId)

		action.move_to_element(signInElement)
		action.click(signInElement)
		action.move_to_element(loginElement)
		action.click(loginElement)
		action.send_keys(self.username)
		action.move_to_element(passwordElement)
		action.click(passwordElement)
		action.send_keys(self.password)
		action.perform()
		

	def purchase(self) -> None:
		'''Execute a purchase'''
		self._selectColor()
		self._selectSize()
		self._addToCart()
		#self._addToCart()
		#self._checkout()

	def _selectColor(self) -> None:
		'''Uses the webdriver to select the color of item to be checked out'''
		colorButtonClass = 'nr-pdp-colorway-DV1214-100'
		colorElement = driver.find_element(By.CLASS_NAME, colorButtonClass)
		action.move_to_element(colorElement)
		action.click(colorElement)
		

	def _selectSize(self) -> None:
		'''Uses the webdriver to select the size of item to be checked out'''
		sizeButtonId = 'skuAndSize__27962581'
		sizeElement = driver.find_element(By.ID, sizeButtonId)
		driver.move_to_element(sizeElement)
		driver.click(sizeElement)
		

	def _addToCart(self) -> None:
		'''Uses the webdriver to create and execute an action chain to reach the checkout page'''
		addCartClass = 'ncss-btn-primary-dark btn-lg add-to-cart-btn'
		addcartElement = driver.find_element(By.CLASS_NAME, addCartClass)
		action.move_to_element(addcartElement)
		action.click(addcartElement)
		

	def _checkout(self) -> None:
		'''Uses the webdriver to complete checkout of order'''
		checkoutClass = 'ncss-btn-primary-dark btn-lg mr3-sm css-1n4ymyz'
		checkoutButtonElement = driver.find_element(By.CLASS_NAME, checkoutClass)
		action.move_to_element(checkoutButtonElement)
		action.click(checkoutButtonElement)
        #IF Nike Account, all info should be filled, just need to click 'Place Order'
		placeorderID = ''
		placeorderBTN = driver.find_element(By.ID, placeorderID)
		action.move_to_element(placeorderBTN)
		action.click(placeorderBTN)
		#self._enterCard()
		pass
	
	def _enterCard(self) -> None:
		'''If needed, uses webdriver to autofill card info'''
		pass

if __name__ == "__main___":
	config = setupConfig("config_.ini")
	print("Launching Bot...")
	bot = CheckoutBot(config, nikeURL, sizeElem, colorElem)
	time.sleep(1)
	print("Logging in...")
	bot.login()
	print("Making purchase...")
	bot.purchase()
	print("Purchase complete!")

