import requests
import re
from bs4 import BeautifulSoup as bfs
import time
import datetime

def job():
    wether_url = "https://tenki.jp/"
    r = requests.get(wether_url)
    wether_date_list = []
    soup = bfs(r.text, "html.parser") # pythonが認識しやすいようにしてくれる手順

    today = re.search(r"\d\d月\d\d日",r.text)
    print(f"{today.group()} 全国の天気\n")
    # time.sleep(1)


    for entry in soup.find_all(class_="forecast-map-entry"):

        # print(str(entry)+"\nここまで\n")
        wether_date_info = {
        "city_name":entry.contents[0].strip(),
        "max_temp":entry.find(class_="max-temp").text,
        "min_temp":entry.find(class_="min-temp").text,
        "prob_precip":entry.find(class_="prob-precip").text
        }

        wether_date_list.append(wether_date_info)
        

    for i, date in enumerate(wether_date_list):
        print(f"{date['city_name']}\n最高気温:{date['max_temp']}\n最低気温:{date['min_temp']}\n降水確率:{date['prob_precip']}\n")
        # if i < len(wether_date_list)-1:
            # time.sleep(0.5)
    print('-'*30, datetime.datetime.now())
if __name__ == '__main__':
    job()