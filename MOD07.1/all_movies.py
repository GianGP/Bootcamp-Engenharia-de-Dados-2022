#%%
from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# %%
driver = webdriver.Chrome('C:/Users/giang/Documents/Bootcamp_DE/A007/src/chromedriver.exe')
driver.implicitly_wait(10)
driver.get("https://pt.wikipedia.org/wiki/Nicolas_Cage")
tabela = driver.find_element(by=By.CSS_SELECTOR, value='.wikitable')

def tem_item(css_selector, driver=driver):
    try:
        driver.find_element(by=By.CSS_SELECTOR, value=css_selector)
        return True
    except:
        return False

#%%

tb_filmes = '.wikitable'

#%%
i = 0
while not tem_item(tb_filmes):
    i+=1
    if i > 50:
        break
    pass

tabela = driver.find_element(by=By.CSS_SELECTOR, value='.wikitable')

# %%
df = pd.read_html(tabela.get_attribute('outerHTML'))[0]

#%%
with open('print.png', 'wb') as f:
    f.write(driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[2]/td/div/div/div/a/img').screenshot_as_png)

#%%
driver.close()
# %%
df.to_csv('filmes_Nicolas_Cage.csv', sep=',', index=None)
# %%
