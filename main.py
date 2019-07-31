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
        
        
