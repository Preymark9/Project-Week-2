from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import requests


def init_browser():

    # Initiate headless driver for deployment
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():


    browser = init_browser()
    movie_data = {}


# Box Office Guru Twitter

    movie_url = 'https://twitter.com/giteshpandya?lang=en'
    browser.visit(movie_url)
    movie_html = browser.html
    movie_soup = BeautifulSoup(movie_html, 'html.parser')
    movie_results = movie_soup.find('div', class_='js-tweet-text-container')
    box_office = movie_results.find('p', class_='tweet-text').text

    movie_data["box_office"] = box_office

    print("Box Office Guru Obtained")


# Forbes Twitter

    movie_url2 = 'https://twitter.com/ScottMendelson?lang=en'
    browser.visit(movie_url2)
    movie_html2 = browser.html
    movie_soup2 = BeautifulSoup(movie_html2, 'html.parser')
    movie_results2 = movie_soup2.find('div', class_='js-tweet-text-container')
    box_office2 = movie_results2.find('p', class_='tweet-text').text

    movie_data["box_office2"] = box_office2

    print("Box Office Forbes Obtained")

# Box Office Pro

    movie_url3 = 'https://twitter.com/BoxOffice?lang=en'
    browser.visit(movie_url3)
    movie_html3 = browser.html
    movie_soup3 = BeautifulSoup(movie_html3, 'html.parser')
    movie_results3 = movie_soup3.find('div', class_='js-tweet-text-container')
    box_office3 = movie_results3.find('p', class_='tweet-text').text

    movie_data["box_office3"] = box_office3

    print("Box Office Pro Obtained")


    return movie_data




