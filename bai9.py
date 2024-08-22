# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:25:13 2024

@author: vy
"""
import math
a= float(input("Nhap gia tri a="))
b= float(input("Nhap gia tri b="))
ketqua= (((a**(1/2) - b**(1/2)) / (a**(1/4) - b**(1/4)))) - ((a**(1/2) + (a*b)**(1/4))) /(a**(1/4) + b**(1/4))
print("Ket qua la= ", ketqua)