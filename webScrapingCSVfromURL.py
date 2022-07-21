from bs4 import  BeautifulSoup as bs
import requests
import os.path

DOMAIN = 'https://data.london.gov.uk/dataset/recorded_crime_rates'
URL = 'https://data.london.gov.uk/dataset/recorded_crime_rates'
FILETYPE = '.csv' #The desired file type

def get_soup(url):
    return bs (requests.get(url).text, 'html.parser')
    # requests.get(url) gets the all raw HTML
    # .text attribute contains the content of the response.Used to access the content. 
    # using html.parser as parser as we are parsing from a HTML document

for link in get_soup(URL).find_all('a'): # contents between <a> and </a> Anchor element. Defines a hyperlink
    file_link = link.get('href') # href attribute indicates the links desnination
    if FILETYPE in file_link: #if the link contains any .csv file extension
        print(file_link)
        path = os.path.join('/home/zareef/Documents/codes/web_scraping', link.text)
        with open(path, 'wb') as file: 
            '''
            open() creates a file in your local storage. wb' stands for "write bytes". 
            The name of the file will be same as the file name inside the href attribute. In our case files with .csv extensio.
            '''

            response = requests.get(DOMAIN + file_link) #gets the csv file link
            url_content = response.content #retrives the contents of the csv file
            file.write(url_content) #writes the contents of the csv file into the opened file.
            file.close() #close file after previous steps are done


