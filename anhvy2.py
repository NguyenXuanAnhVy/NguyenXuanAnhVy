# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:09:51 2024

@author: Anhvy
"""
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
if a==0:
    if b ==0:
        print("Phuong trinh co vo so nghiem")
    else:
        print("Phuong trinh co nghiem")
else:
    x = -b/a
    print("Phuong trinh co nghiem la:", x)