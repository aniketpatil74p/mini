from django import forms
from django.core import validators

def mergefunction(s1,s2):
    merged = []
    for i in range(0, len(s1)):
        tup = (s1[i],s2[i])
        merged.append(tup)
    return merged

class GeeksForm(forms.Form): 
    # GEEKS_CHOICES =( 
    # ("1", "One"), 
    # ("2", "Two"), 
    # ("3", "Three"), 
    # ("4", "Four"), 
    # ("5", "Five"), 
    # ) 
    # geeks_field = forms.ChoiceField(choices = GEEKS_CHOICES)
    #   
    import csv
    import pandas as pd
    filename =  r"firstapp\download\downloaded1.csv"
    data = open(filename, encoding = "utf8")
    csv_data = csv.reader(data)
    data_lines = list(csv_data)
    total_row  = (len(data_lines))
    total_col = 0
    list1 = []
    list2 = []
    for i in data_lines[0]:
        if(total_col>=14):
            list1.append(i)
            list2.append(i)
        total_col = total_col + 1
    df = pd.read_csv(filename)
    property_dic = {}

    for i in range(0,len(list1)):
        key = list1[i]
        saved_column = df[list1[i]]
        saved_column = set(saved_column)
        s1 = list(saved_column)
        s2 = list(saved_column)
        merged = mergefunction(s1,s2)
        value = merged
        value = tuple(value)
        property_dic[key] = value


    k = (len(list1))    
    # print(property_dic)
    i = 0
    if i < k:
        key1 = forms.ChoiceField(choices = property_dic[list1[i]] )
    i = i + 1

    if i < k:
        key2 = forms.ChoiceField(choices = property_dic[list1[i]] )
    i = i + 1


    if i < k:
        key3 = forms.ChoiceField(choices = property_dic[list1[i]] )
    i = i + 1


    if i < k:
        key4 = forms.ChoiceField(choices = property_dic[list1[i]] )
    i = i + 1


    if i < k:
        key5 = forms.ChoiceField(choices = property_dic[list1[i]] )
    i = i + 1


    if i < k:
        key6 = forms.ChoiceField(choices = property_dic[list1[i]] )
    i = i + 1


    if i < k:
        key7 = forms.ChoiceField(choices = property_dic[list1[i]] )
    i = i + 1


    if i < k:
        key8 = forms.ChoiceField(choices = property_dic[list1[i]] )
    i = i + 1


    if i < k:
        key9 = forms.ChoiceField(choices = property_dic[list1[i]] )
    i = i + 1

    if i < k:
        key10 = forms.ChoiceField(choices = property_dic[list1[i]] )
    i = i + 1
