#%%
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#%%
url = 'https://portalcafebrasil.com.br/todos/podcasts/'

#%%
ret = requests.get(url)
# %%
ret.text

# %%

soup = bs(ret.text)
# %%
soup
# %%
soup.find('h5')

# %%
soup.find('h5').text

# %%
soup.find('h5').a['href']

# %%

lst_podcasts = soup.find_all("h5")
# %%
for item in lst_podcasts:
    print(f'EP: {item.text} - Link: {item.a["href"]}')

# %%

url = 'https://portalcafebrasil.com.br/todos/podcasts/page/{}/?ajax=true'

# %%
url.format(5)

# %%

def get_podcast(url):
    ret = requests.get(url)
    soup = bs(ret.text)
    return soup.find_all("h5")

# %%

get_podcast(url.format(5))


#%%
import logging
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

# %%



i = 1
lst_podcasts = []
lst_get = get_podcast(url.format(i))
log.debug(f"Coletado {len(lst_get)} episodios do link: {url.format(i)}")
while len(lst_get) > 0:
    lst_podcasts = lst_podcasts + lst_get
    i += 1
    lst_get = get_podcast(url.format(i))
    log.debug(f"Coletado {len(lst_get)} episodios do link: {url.format(i)}")



# %%

len(lst_podcasts)

# %%
lst_podcasts
# %%
df = pd.DataFrame(columns=["nome", "link"])
# %%
for item in lst_podcasts:
    df.loc[df.shape[0]] = [item.text, item.a['href']]

# %%
df.shape

# %%
df

# %%
df.to_csv("banco_de_podcast.csv", sep=";", index=False)
# %%
