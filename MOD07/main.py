#%%
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# %%

cep = sys.argv[1]
#cep = '01228-100'

if cep:
    driver = webdriver.Chrome('C:/Users/giang/Documents/Bootcamp_DE/A007/src/chromedriver.exe')

    #%%
    # Acesso ao site da how
    #driver.get("https://howedu.com.br")
    #driver.find_element_by_xpath('//*[@id="post-11648"]/div/div/div/section[1]/div/div[1]/div/div[4]/div/div/a').click()
    # %%
    driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

    #%%
    elem_cep = driver.find_element_by_name('endereco')
    elem_cep.clear()
    elem_cep.send_keys(cep)

    # %%
    elem_cmb = driver.find_element_by_name('tipoCEP')
    elem_cmb.click()
    driver.find_element_by_xpath('//*[@id="formulario"]/div[2]/div/div[2]/select/option[6]').click()
    #%%
    driver.find_element_by_xpath('//*[@id="btn_pesquisar"]').click()
    # %%
    time.sleep(1)
    lista = driver.find_elements(by=By.CSS_SELECTOR, value='#resultado-DNEC > tbody > tr > td')
    lista = [l.text for l in lista]
    driver.close()
    # %%
    print(f"""
    Para o CEP {cep} temos:
    Endereço: {lista[0].split(" - ")[0]},
    Bairro: {lista[1]},
    Localidade: {lista[2]}
    """)

# %%
