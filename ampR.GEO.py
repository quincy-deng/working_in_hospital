import os
csv_fl= r'C:\Users\dengqiuyang\OneDrive\文档\ampR_Geo.CSV'
with open(csv_fl) as f:
    fr = f.readline().split(',')
    loc = []
    locd = dict()
    for line in f:
        le = line.split(',')
        if le[2] not in loc:
            loc = []
            locd[4]
 