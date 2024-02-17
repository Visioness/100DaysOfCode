import requests
from bs4 import BeautifulSoup


URL = 'https://appbrewery.github.io/Zillow-Clone/'
class RentData:
    def __init__(self):
        response = requests.get(url=URL)
        self.soup = BeautifulSoup(response.text, 'html.parser')
    
    def get_data(self):
        self.addresses = [tag.getText().replace('|', '').strip() for tag in self.soup.find_all(attrs={'data-test': 'property-card-addr'})]
        self.links = [tag.get('href') for tag in self.soup.find_all(class_= 'StyledPropertyCardDataArea-anchor')]
        self.prices = [tag.getText().replace('/', '+').split('+')[0] for tag in self.soup.find_all(attrs={'data-test': 'property-card-price'})]

        return self.addresses, self.links, self.prices