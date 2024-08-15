# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:45:16 2024

@author:NguyenXuanAnhVy
"""

GPA=float(input("Nhap diem trung binh: "))
if GPA < 3.5 : print("Hoc luc kem")
if GPA < 3.5 and GPA < 5 : print("Hoc luc yeu")
if GPA >= 5 and GPA < 7 : print("Hoc luc trung binh")
if GPA >= 7 and GPA < 8 : print("Hoc luc kha")
if GPA >= 8 and GPA < 9 : print ("Hoc luc gioi")
if GPA >= 9 and GPA <= 10 : print ("Hoc luc xuat sac")
else: 
    print("Khong xac dinh")