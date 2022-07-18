#%%
from selenium import webdriver
# %%

driver = webdriver.Chrome('C:/Users/giang/Documents/Bootcamp_DE/A007/src/chromedriver.exe')

# %%
driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

#%%
elem_cep = driver.find_element_by_name('endereco')
elem_cep.clear()
elem_cep.send_keys("01228-100")

# %%
elem_cmb = driver.find_element_by_name('tipoCEP')
elem_cmb.click()
driver.find_element_by_xpath('//*[@id="formulario"]/div[2]/div/div[2]/select/option[6]').click()
#%%
driver.find_element_by_xpath('//*[@id="btn_pesquisar"]').click()
# %%
