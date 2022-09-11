import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs

url = input('Enter a youtube url of the following form : https://www.youtube.com/user/CHANNEL_ID/videos\n')
if 'www.youtube.com' and 'videos' not in url:
    print('Please restart program and enter a correct youtube URL')
    sys.exit()
else:
    driver = webdriver.Firefox()
    driver.get(url)

driver.find_element(By.XPATH, '//button[@aria-label="Reject all"]').click()
time.sleep(1.5)

views = []
titles = []
release_dates = []
vid_to_scrape = []

for elements in driver.find_elements(By.XPATH, '//a[@id="thumbnail"]'):
    vid_to_scrape.append(elements.get_attribute('href'))

vid_to_scrape.remove(None)  # Silly line, but it does remove the null/None object from the vid_to_scrape list
driver.execute_script('window.open("");')

for vids in vid_to_scrape:
    driver.switch_to.window(driver.window_handles[1])
    driver.get(vids)
    html = driver.page_source
    soup = bs(html, 'html.parser')
    elements_views = soup.findAll('meta', attrs={'itemprop': 'interactionCount'})
    elements_title = soup.findAll('meta', attrs={'name': 'title'})
    elements_releaseDate = soup.findAll('meta', attrs={'itemprop': 'datePublished'})

    
    for element in elements_views:
        views.append(int(element.get('content')))
    for element in elements_title:
        titles.append(element.get('content'))
    for element in elements_releaseDate:
        release_dates.append(element.get('content'))

driver.close()

for i in range(0, len(views)-1):
    print(release_dates[i] + " - " + titles[i] + " : " + '{:,}'.format(views[i]))
    
