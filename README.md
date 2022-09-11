# ytb_scraping
Scrapes video infos from a youtube channel link e.g(https://www.youtube.com/channel/CHANNEL_ID/videos). Does not use Youtube API

Requires geckodriver for selenium to be able to use Firefox

The program is slow to collect information since each youtube page has to be loaded in a browser for the interesting informations to be displayed in the page source code. Using only BS4 and requests will not have any results.
