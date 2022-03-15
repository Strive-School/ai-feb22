import requests
from bs4 import BeautifulSoup



url = f'https://www.imdb.com/search/title/?genres=comedy&start=201&explore=title_type,genres&ref_=adv_nxt'

page = requests.get(url)

descr = []
partial_url = []
page_content = BeautifulSoup(page.content, 'html.parser')

movie_div = page_content.find_all('div', class_='lister-item-content')

for el in movie_div:
    p_tags = el.find_all('p', class_='text-muted')

    description = p_tags[1].text

    descr.append(description)

    # h3_tags = el.find('h3', class_='lister-item-header')

    partial_url.append(el.h3.a['href']) # el -> h3 -> a['href']

print(partial_url[0])

# print(len(descr))

# f'https://www.imdb.com/title/{some_variable_here}/locations?ref_=tt_ql_sm'
# https://www.imdb.com/title/tt13403046/locations?ref_=tt_ql_sm
# https://www.imdb.com/title/tt8097030/locations?ref_=tt_ql_sm