from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import urllib.request
import os
from configparser import ConfigParser


nikeURL = 'https://www.nike.com/t/mens-basketball-t-shirt-RxlfV9/DV1214-100'
colorElem = 'css-7aigzk colorway-container d-sm-ib d-lg-tc pr1-sm pb1-sm'
sizeElem = 'skuAndSize__27962549'
addCartElem = 'ncss-btn-primary-dark btn-lg add-to-cart-btnncss-btn-primary-dark btn-lg add-to-cart-btn'

def setupConfig(file: str) -> ConfigParser:
	print("Parsing Configuration...")
	config = ConfigParser()
	config.read("file")
	return config

class CheckoutBot():
	'''Bot automates purchasing a product given a product URL, credentials and size/color'''
	def __init__(self,config, URL, size, color):
		self.username = config.get("NIKE_ACCOUNT", "USERNAME")
		self.password = config.get("NIKE_ACCOUNT", "PASSWORD")
		self.ID = config.get("NIKE_ACCOUNT", "ID")
		self.card = config.get("CREDIT_CARD", "CCNUM")
		self.ccsecurity = config.get("CREDIT_CARD", "CCV")
		self.expiration_month = config.get("CREDIT_CARD", "EXPM")
		self.expiration_year = config.get("CREDIT_CARD", "EXPY")
		self.driver = webdriver.Chrome()
		self.URL = driver.get(URL)
		self.addcartElement = driver.find_element(By.CLASSNAME, addCartElem)
		self.colorElement = driver.find_element(By.CLASSNAME, color)
		self.sizeElement = driver.find_element(By.ID, size)

	def login(self) -> None:
		'''Uses the webdriver to locate the login fields and logs the user in using the passed credentials'''
		pass

	def purchase(self) -> None:
		'''Execute a purchase'''
		pass

	def _selectColor(self) -> None:
		'''Uses the webdriver to select the color of item to be checked out'''
		pass

	def _selectSize(self) -> None:
		'''Uses the webdriver to select the size of item to be checked out'''
		pass

	def _addToCart(self) -> None:
		'''Uses the webdriver to create and execute an action chain to reach the checkout page'''
		pass

	def _checkout(self) -> None:
		'''Uses the webdriver to complete checkout of order'''
		pass

if __name__ == "__main___":
	config = setupConfig("config.ini")
	print("Launching Bot...")
	bot = CheckoutBot(config, nikeURL, sizeElem, colorElem)
	time.sleep(1)
	print("Logging in...")
	bot.login()
	print("Making purchase...")
	bot.purchase()
	print("Purchase complete!")
