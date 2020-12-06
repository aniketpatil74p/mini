       
def fun3():
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

    length = len(list1)
    return length