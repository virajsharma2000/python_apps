from bs4 import BeautifulSoup
import requests

def crawl_web(website_name):
 website_source_code = requests.get(website_name).text

 soup = BeautifulSoup(website_source_code,'html.parser')

 for links in soup.findAll('a'):
     if links.get('href').startswith('http'):
         website_to_scrap = links.get('href')

     else:
         website_to_scrap = '{}/{}'.format(website_name,links.get('href'))

     print(website_to_scrap)

     website_source_code = requests.get(website_to_scrap).text

     soup = BeautifulSoup(website_source_code,'html.parser')

     for paragraphs in soup.findAll('p'):
         text = paragraphs.get_text()

         print(text)


website_name = input('Enter website name: ')

crawl_web(website_name)
