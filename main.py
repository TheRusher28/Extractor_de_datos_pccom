from bs4 import BeautifulSoup
import requests

def process_web_page(url):
    req = requests.get(url)
    status_code = req.status_code
    
    if status_code == 200:
        html = BeautifulSoup(req.text, 'lxml')
        return html
    else:
        print('ERROR {}'.format(status_code))
        
def extract_info(html):
    #Extract_name
    name = html.select_one('h1.h4 > strong:nth-child(1)').text
    print('Name = {}'.format(name))
    
    #Extract price
    price = html.select_one('.baseprice').text
    print('Price = {} €'.format(price))
    
    #Extract discount percentage
    discount = html.select_one('div.precio:nth-child(4)')
    if discount == None:
        print('dto.0 %')
    else:
        print(discount.text)
    
    #Extract disponibility 
    disponibility = html.select_one('#enstock').text
    print('disponibility = {}'.format(disponibility))
    
    #Extract average rating
    avg_rating = html.select_one('div.col-md-4:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').text
    print('average rating = {}'.format(avg_rating))
    
    #Extract_first_opinion
    f_opinion = html.select_one('div.col-md-10:nth-child(2) > div:nth-child(1) > p:nth-child(1) > q:nth-child(1)').text
    print('First opinion = {}'.format(f_opinion))
    
    #Extract some specs
    specs = html.select_one('#ficha-producto-caracteristicas').text
    print('\n Specifications = {}' .format(specs))
    
html = process_web_page("Paste here the product's URL")
extract_info(html)
