# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:25:58 2024

@author: AnhVy23720911
"""
a=input("Nhap vao ngay thang nam: ")
dd, mm, yy = map(int, a.split("-"))

if yy % 4 == 0 and yy % 100 !=0 or yy % 400 ==0:
    kiem_tra = True
else:
    kiem_tra = False
     
a = [31,28,31,30,31,30,31,31,30,31,30,31] #dang list

if kiem_tra:
    a[1] = 29
if dd<1 or dd>a[mm-1]:
    print("Ngay khong hop le")
if mm<1 or mm>12:
    print("Thang khong hop le")
if yy<1:
    print("Nam khong hop le")
else:
    print("Ngay thang nam hop le")
    
if kiem_tra == True:
    print("Ngay thang nam hop le")
else:
    print("Ngay thang nam khong hop 24le")

