from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

search_item = "Formalwear men"

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://coolhunting.com/')
search_box = browser.find_element("xpath",'//*[@id="search-5"]/form/label/input')

search_box.send_keys(search_item)
time.sleep(5)
search_box.submit()
main = browser.find_element("xpath",'//*[@id="jetpack-instant-search__search-results-content"]/div[1]/ol')

articles = main.find_elements_by_tag_name("li")
links = []
for article in articles:
    header = article.find_element_by_tag_name("a")
    link = header.get_attribute('href')
    links.append(link)

new_items = []


for link in links:
    browser.get(link)
    record = dict()
    main = browser.find_element_by_class_name('entry-content')
    record["corpus_text"] = main.text
    new_items.append(record)

df = pd.DataFrame(new_items)
df.to_csv('Formalwear men.csv', sep=',', encoding='utf-8')
