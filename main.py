import urllib.request
import os
from dotenv import load_dotenv
from datetime import datetime
from plyer import notification
from bs4 import BeautifulSoup

# side note
# when having problems with porting python files to exes
# while using plyer notifications then add this command to yout pyinstaller command: 
# --hidden-import plyer.platforms.win.notification

log = ""


def check_availability(url, phrase):
    global log
    try:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, features='html.parser')

        if phrase in soup.text:
            return False
        return True
    except:
        log += "Error parsing the website"


def stock_notification(product):
    notification.notify(
        title=f'{product} is in stock!',
        message='Go grab it NOW!',
        app_icon="assets/vegy_penis.ico",
    )


def main():
    load_dotenv()
    url = os.getenv("URL")
    phrase = os.getenv("PHRASE")
    product = os.getenv("PRODUCT")
    available = check_availability(url, phrase)

    if available:
        stock_notification(product)


if __name__ == '__main__':
    main()
