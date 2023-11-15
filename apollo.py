from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pickle
from auth_date import apollo_login, apollo_pass

options = webdriver.ChromeOptions()
options.add_argument('user-agent=Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0')

driver = webdriver.Chrome()

try:

	# driver.get("https://app.apollo.io/#/settings/account/mailboxes")
	# driver.maximize_window()
	# time.sleep(10)

	# email_login = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/form/div[5]/div/div/input')
	# email_login.send_keys(apollo_login)
	# time.sleep(1)

	# password = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/form/div[6]/div/div[1]/div/input')
	# password.send_keys(apollo_pass)
	# time.sleep(1)
	# button_login = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/form/div[7]/button')
	# button_login.click()
	# time.sleep(40)

	# pickle.dump(driver.get_cookies(), open(f"{apollo_login}_cookies", "wb")) # сохранение куки
	
	#Авторизация с куки
	driver.get("https://app.apollo.io/#/settings/account/mailboxes")
	driver.maximize_window()
	time.sleep(5)

	for cookie in pickle.load(open(f"{apollo_login}_cookies", "rb")):
		driver.add_cookie(cookie)

	time.sleep(5)
	driver.refresh()
	time.sleep(30)

except Exception as ex:
	print(ex)
# finally:
# 	driver.close()
# 	driver.quit()
