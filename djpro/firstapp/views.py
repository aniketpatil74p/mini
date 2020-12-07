from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
import re
import requests
from bs4 import BeautifulSoup
from .scrap import fun
from .scrap import fun2
# from .scrap import fun3
from . import forms
from .forms import FormName
import os
#  Create your views here.

namenum = {}    
namelink = {}
 

def index(request):
    namenum = fun()
    List = list()
    for i in namenum.items():
        List.append(i)
    

    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

    if form.is_valid():
            print("VALIDATION SUCCESS!")
            return nextstep(request,form.cleaned_data['number'])
    
    Context = {
                'List': List,
                'form' : form,
    }

    template = loader.get_template("firstapp/index.html")
    res = template.render(Context,request)
    return HttpResponse(res)




def nextstep(request,num1):
    namenum = fun()
    namelink = fun2()   
    base_url = "https://www.digikey.in"
    name_prod = namenum[num1]
    url = namelink[name_prod]
    req_url = base_url + url
    # download 1 page
    import bs4
    res = requests.get(req_url)
    soup = bs4.BeautifulSoup(res.text,"lxml")
    tags = soup.find_all('span', {"class": "current-page"})
    try:
        strii = tags[0].getText()
    except IndexError:
        return HttpResponse("cant scrap ")
    pos = strii.find('/')
    newstr = strii[pos+1::]
    newstr = newstr.replace(',','')
    numofpages = int(newstr)
    need_num2  = 1
    requrl = req_url
    pos = requrl.rfind('/')
    need_num1 = int(requrl[pos+1::])
    need_url = "https://www.digikey.in/product-search/download.csv?FV=-8%7C{}&quantity=0&ColumnSort=0&page={}&pageSize=25".format(need_num1,need_num2)
    req = requests.get(need_url)
    url_content = req.content
    filename = "firstapp/download/downloaded{}.csv".format(need_num2)
    csv_file = open(filename, 'wb')
    csv_file.write(url_content)
    csv_file.close()



    import csv
    import pandas as pd
    filename =  r"firstapp\download\downloaded1.csv"
    data = open(filename, encoding = "utf8")
    csv_data = csv.reader(data)
    data_lines = list(csv_data)
    total_row  = (len(data_lines))
    total_col = 0
    list1 = []
    for i in data_lines[0]:
        if(total_col>=14):
            list1.append(i)
        total_col = total_col + 1

    Context = {
    
    }

    template = loader.get_template("firstapp/form_page.html")
    res = template.render(Context,request)
    return HttpResponse(res)


def form_name_view(request):
    from . import forms2
    from .scrap2 import fun3
    form = forms2.GeeksForm()

    if request.method == 'POST':
        form = forms2.GeeksForm(request.POST)
        
    if form.is_valid():
            print("VALIasfsadsadsdfssdffasfasdfsadfa!")
            # print(form.cleaned_data['geeks_field'])
            # print(type(form.cleaned_data['geeks_field']))
            # return HttpResponse("hi")
            # print(form.cleaned_data['key1'])                                                                                                                
            # print(form.cleaned_data['key2'])
            lenoflist = fun3()
            # print("printing fun3   ")
            # print(fun3())
            i = 0
            # print("lenof list is " )
            # print(lenoflist)
            listofdata = []
            if i < lenoflist:
                data = form.cleaned_data['key1']
                # print("data is ")
                # print(data)
                listofdata.append(data)
            i = i+1
            if i < lenoflist:
                data = form.cleaned_data['key2']
                listofdata.append(data)
            i = i+1
            if i < lenoflist:
                data = form.cleaned_data['key3']
                listofdata.append(data)
            i = i+1
            if i < lenoflist:
                data = form.cleaned_data['key4']
                listofdata.append(data)
            i = i+1
            if i < lenoflist:
                data = form.cleaned_data['key5']
                listofdata.append(data)
            i = i+1
            if i < lenoflist:
                data = form.cleaned_data['key6']
                listofdata.append(data)
            i = i+1
            if i < lenoflist:
                data = form.cleaned_data['key7']
                listofdata.append(data)
            i = i+1
            if i < lenoflist:
                data = form.cleaned_data['key8']
                listofdata.append(data)
            i = i+1
            if i < lenoflist:
                data = form.cleaned_data['key9']
                listofdata.append(data)
            i = i+1
            if i < lenoflist:
                data = form.cleaned_data['key10']
                listofdata.append(data)
           
            return finalfun(request,listofdata)
            # print("list of data is ")
            # print(listofdata)            

    import csv
    import pandas as pd
    filename =  r"firstapp\download\downloaded1.csv"
    data = open(filename, encoding = "utf8")
    csv_data = csv.reader(data)
    data_lines = list(csv_data)
    total_row  = (len(data_lines))
    total_col = 0
    list1 = []
    for i in data_lines[0]:
        if(total_col>=14):
            list1.append(i)
        total_col = total_col + 1

    # Context = {
    #     "List" : list1,
    # }

    context = {
        'form' : form,
            "List" : list1,

    }

    return render(request,'firstapp/form_page2.html',context)
    # return HttpResponse("hi")



def finalfun(request,listofdata):

    import csv

    # filename =  r"C:\Users\91956\Desktop\miniproject\djpro\firstapp\download\downloaded1.csv"
    filename =  "firstapp/download/downloaded1.csv"

    data = open(filename, encoding = "utf8")
    csv_data = csv.reader(data)
    data_lines = list(csv_data)
    total_row = len(data_lines)


    # listofdata = ['Voltage (Voltmeter)', '±20VDC', 'LCD - Black Characters', '3.5', '0.370" (9.40mm)', '-', '5VDC', 'Rectangular - 33.93mm x 21.29mm', 'Panel Mount', 'PC Pin']
    # listofdata = ['Voltage (Voltmeter)', '±199.9mVDC', 'LCD - Red Characters, Backlight', '3.5', '0.401" (10.20mm)', '-', '5VDC', 'Rectangular - 42.70mm x 23.60mm', 'Panel Mount', 'PC Pin']
    length = len(listofdata)


    def checkequal(l1,l2):
        for i in range(0,length):
            if(l1[i] != l2[i]):
                return False
        return True



    li = []
    for i in range(1,total_row):
        ls = data_lines[i][14:]
        while len(ls) > length:
            ls.pop()
        if(checkequal(ls,listofdata)):
            prod_name = { "name" : data_lines[i][5] }
            prod_quantity = { "qunatity" : data_lines[i][6] }
            prod_price = { "price" : data_lines[i][8]}

            li.append(prod_name)
            li.append(prod_quantity)
            li.append(prod_price)


    Context = {
                'list'     : li,
    }
    template = loader.get_template("firstapp/finaloutput.html")
    res = template.render(Context,request)
    return HttpResponse(res)
    # return HttpResponse("thanks for info")













