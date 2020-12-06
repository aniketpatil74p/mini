import csv
import pandas as pd

filename =  r"C:\Users\91956\Desktop\miniproject\djpro\firstapp\download\downloaded1.csv"
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


# merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
# print(merged_list)



df = pd.read_csv(filename)
property_dic = {}
for i in range(0,len(list1)):
    key = list1[i]
    saved_column = df[list1[i]]
    saved_column = set(saved_column)
    s1 = list(saved_column)
    s2 = list(saved_column)
    merged =  [(s1[i], s2[i]) for i in range(0, len(s1)) ]   
    # merged = tuple(merged) 
    value = merged
    value = tuple(value)
    property_dic[key] = value
    # print(type(merged))

# for i in property_dic.values():
#     print(i)

# print(property_dic['Frequency'])
for i in range(0,len(list1)):
    key = list1[i]
    print(property_dic[key])
    print()
    # list1[i] = forms.ChoiceField(choices =property_dic[key] )

# lis = list(property_dic.items())
# print(lis)



# for i in lis:
#     print(i)
# print(property_dic)

# for i in property_dic.values():
#     for j in i:
#         j = tuple(j)
#         print(j)
#     print()


# print(property_dic.values())










# GEEKS_CHOICES =( 
#     ("1", "One"), 
#     ("2", "Two"), 
#     ("3", "Three"), 
#     ("4", "Four"), 
#     ("5", "Five"), 
# ) 

# print(type(GEEKS_CHOICES))











# print(total_col)
# print(namelist[0])

# property_dic = {}
# for i in range(14,total_col):
#     key = namelist[i]
#     value = list[]
    


# data_lines = list(csv_data)
# totalrows = (len(data_lines))
# li = list()
# for row in data_lines[1:totalrows]:
#     li.append(row[17])
# li = set(li)
# li = list(li)
# print(type(li))
# print(li)

