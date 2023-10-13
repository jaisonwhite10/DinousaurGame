import selenium
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.EdgeOptions()
options.add_experimental_option('detach', True)

service = Service(r'C:\Users\Jaison White\Documents\Development\msedgedriver.exe')

driver = webdriver.Edge(options=options,service=service)
driver.get('https://elgoog.im/dinosaur-game/')

# Find Button to Turn on Bot
bot_status = driver.find_element(By.CSS_SELECTOR, 'input#botStatus')
bot_status.click()

# Click Space Bar Once To Start Game
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.SPACE)

timeout = time.time() + (60*5)

### Keeps Game going for 5 minutes after closes browser
game = True

while game:
    if time.time() < timeout:
        game = True

    else:
        game = False
        driver.quit()



