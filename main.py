from bs4 import BeautifulSoup
import time
import requests

while True:
    page_to_scrape = requests.get("https://weather.com/weather/today/l/813bd949c1fb6516e4fb544ba7cc34b485913a00404074a098ae0aa4b383f35b")


    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

    mytext = soup.findAll('span', attrs={'CurrentConditions--tempValue--MHmYY'})

    test = str(mytext)

    for text in mytext:
        print(text.text)

    time.sleep(3)
