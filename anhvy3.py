# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:22:38 2024

@author: Student
"""

import math
a = float(input("Nhap gia tri a: "))
b = float(input("Nhap gia tri b: "))
c = float(input("Nhap gia tri c: "))
if a ==0:
    if b==0:
        if c ==0:
            print("Phuong trinh co vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else: 
        x = -c/b
        print ("Nghiem cua phuong trinh la:",x)
else:
     delta = b**2 - 4*a*c
     if delta > 0:
         x1 = (-b  + math.sqrt(delta))/ (2*a)
         x2 = (-b - math.sqrt(delta))/ (2*a)
         print("Phuong trinh co hai nghiem phan biet: x1 = {x1}, x2 = {x2}")
     elif delta == 0:
         x = -b/(2*a)
         print ("Phuong trinh co nghiem kep: x = {x}")
     else:
         print("Phuong trinh vo nghiem")
