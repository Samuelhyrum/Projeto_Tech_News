from time import sleep
import requests
import parsel


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
    selector = parsel.Selector(html_content)
    links = []
    try:
        links = selector.css(".entry-title > a::attr(href)").getall()
    finally:
        if links:
            return links
        else:
            return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = parsel.Selector(html_content)
    link_error = None
    try:
        next_page = selector.css(
            '.next.page-numbers::attr(href)').get()
    finally:
        if next_page:
            return next_page
        else:
            return link_error


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
