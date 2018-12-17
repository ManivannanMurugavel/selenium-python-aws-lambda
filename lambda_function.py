import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from time import sleep

def lambda_handler(event, context):
    print("getting url: " + event['url'] + ". . .")

    if 'url' in event.keys():
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1280x1696')
        chrome_options.add_argument('--user-data-dir=/tmp/user-data')
        chrome_options.add_argument('--hide-scrollbars')
        chrome_options.add_argument('--enable-logging')
        chrome_options.add_argument('--log-level=0')
        chrome_options.add_argument('--v=99')
        chrome_options.add_argument('--single-process')
        chrome_options.add_argument('--data-path=/tmp/data-path')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--homedir=/tmp')
        chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
        chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
        chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"

        driver = webdriver.Chrome(chrome_options=chrome_options)
        sleep(1)
        driver.get(event['url'])
    else:
        print("Error: ")
        return ("Couldnt get url from event object")
    
    #first song
    xpath_time = '//div[@class="PlaylistItem-time"]//h5[1]'
    xpath_song_name = '//div[@class="PlaylistItem u-mb1"]//h3[1]'
    xpath_song_artist = '//div[@class="PlaylistItem u-mb1"]//div[@class="u-h3 u-mb1 u-lightWeight"][1]'
    xpath_song_album = '//div[@class="PlaylistItem u-mb1"]//div[@class="u-h5 u-mb0 u-italic u-normalCase"]'

    song_time = driver.find_element_by_xpath(xpath_time).get_attribute('innerHTML')
    song_name = driver.find_element_by_xpath(xpath_song_name).get_attribute('innerHTML')
    song_artist = driver.find_element_by_xpath(xpath_song_artist).get_attribute('innerHTML')
    song_album = driver.find_element_by_xpath(xpath_song_album).get_attribute('innerHTML')
    
    #TODO: get second and third songs, handle error relating to "AIR BREAK" condition

    recent_songs = []
    first_song = {
        'time': song_time,
        'name': song_name,
        'artist': song_artist,
        'album': song_album
    }
    print(first_song)
    recent_songs.append(first_song)

    driver.close()
    driver.quit()

    return first_song
