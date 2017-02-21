from selenium import webdriver

brower = webdriver.Firefox()
brower.get('http://127.0.0.1:8000')

assert 'Django' in browser.title
