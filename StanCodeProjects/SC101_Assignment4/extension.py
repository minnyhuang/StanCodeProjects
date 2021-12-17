"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        ###########################################
        #                                         #
        #      TODO: 回傳特定年份的新生兒男女總人數    #
        #                                         #
        ###########################################
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")
        items = soup.find_all('tbody')
        count_m = 0
        count_f = 0

        for item in items:
            for i in range(len(item.find_all('td'))-2):
                tds = item.find_all('td')[i].text
                if i % 5 == 2:
                    count_m += int(tds.replace(',', ''))
                if i % 5 == 4:
                    count_f += int(tds.replace(',', ''))
        print('Male Number: ', count_m)
        print('Female Number: ', count_f)


if __name__ == '__main__':
    main()
