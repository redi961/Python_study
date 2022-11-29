# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:03:50 2022

@author: user
"""

## 상단 경로 항상 주의할것 

import usecsv
import re

data = usecsv.opencsv("example2.csv")
print(data)
usecsv.writecsv("test3.csv", data)

## :5 = 4번까지 (5번의 앞까지)

# for i in total[:5]:
#     print(i)


total = usecsv.opencsv("popSeoul.csv")
for i in total:
    for j in i:
        try :
            i[i.index(j)] = float(re.sub(",","",j))
        except:
            pass
total

     