# -*- coding: utf-8 -*-
# spyder 내에서 주석은 ctrl + 1
## 참조 csv는 파일의 저장경로와 동일하게 만들어둘것
## 추가로 우측 상단에 있는 경로 설정하여 파일을 사용함
## 아나콘다 라이브러리는 c 최상단 program data 폴더로 숨겨져있음

import csv
import re

def opencsv(filename):
    f = open(filename, "r")
    new = csv.reader(f)
    a_list=[]
    
    for line in new:
        a_list.append(line)
    
    return a_list

list1 = opencsv('a.csv')
print (list1)


############ with 형식
def opencsv(filename):
    with open(filename, "r")as f:
     reader = csv.reader(f)
     output = []
     for i in reader:
      output.append(i) 
    return output

list2 = opencsv('a.csv')
print (list2)

########### write방싱
def writecsv(filename, the_list):
    f = open(filename, "w", newline="")
    ## delimiter == 파일 구분자 지정 (기본적으로 , 사용)
    csvobject = csv.writer(f, delimiter=",")
    csvobject.writerows(the_list)
    f.close()
    
li = opencsv("example2.csv")
print(li)

data = [['이름', '국어', '영어', '수학'],
        ['a', '90', '80', '70'],
        ['b', '80', '70', '90'],
        ['c', '100', '100', '90' ]]

writecsv("test3.csv", data)

###########
def switch(listName):
    for i in listName:
        for j in i :
            try :
                i[i.index(j)] = float(re.sub(",","",j))
            except :
                pass
            return listName;
        



