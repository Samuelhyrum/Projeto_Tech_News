import requests
from time import sleep


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    sleep(1)
    response = None
    try:
        response = requests.get(url, headers={
            "user-agent": "Fake user-agent"
            }, timeout=3)
    except requests.ReadTimeout:
        return None
    finally:
        if response:
            return response.text
        else:
            return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
