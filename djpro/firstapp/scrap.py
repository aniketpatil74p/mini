import requests
import bs4

from firstapp import views

def fun():
    res = requests.get("https://www.digikey.in/products/en")
    soup = bs4.BeautifulSoup(res.text,"lxml")
    # base_url = "https://www.digikey.in"
    mydivs = soup.find_all("a", {"class": "flymenu__item-title"})

    name_link = {}

    count = 1
    for i in mydivs:
        name = i.getText()
        link = i.get('href')
        name_link[name] = link

    count = 1
    name_num = {}
    for i in name_link.keys():
        name = i
        name_num[count] = name
        count += 1

    return name_num
        




def fun2():
    res = requests.get("https://www.digikey.in/products/en")
    soup = bs4.BeautifulSoup(res.text,"lxml")
    # base_url = "https://www.digikey.in"
    mydivs = soup.find_all("a", {"class": "flymenu__item-title"})

    name_link = {}

    count = 1
    for i in mydivs:
        name = i.getText()
        link = i.get('href')
        name_link[name] = link

    count = 1
    name_num = {}
    for i in name_link.keys():
        name = i
        name_num[count] = name
        count += 1

    return name_link
        
# def fun3():
#     import csv
#     import pandas as pd
#     filename =  r"firstapp\download\downloaded1.csv"
#     data = open(filename, encoding = "utf8")
#     csv_data = csv.reader(data)
#     data_lines = list(csv_data)
#     total_row  = (len(data_lines))
#     total_col = 0
#     list1 = []
#     for i in data_lines[0]:
#         if(total_col>=14):
#             list1.append(i)
#         total_col = total_col + 1

#     length = len(list1)
#     return length