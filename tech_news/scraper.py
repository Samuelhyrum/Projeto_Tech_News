from time import sleep
from bs4 import BeautifulSoup
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
    soup = BeautifulSoup(html_content, 'html.parser')
    selector = parsel.Selector(html_content)

    url = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css('h1::text').get().strip()
    timestamp = selector.css('.meta-date::text').get()
    category = selector.css('.label::text').get()
    writer = selector.css('.author a::text').get()
    reading_time = int(selector.css(
        '.meta-reading-time::text').get().split()[0])
    summary = soup.find('div', {
        'class': 'entry-content'}).find('p').text.strip()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
