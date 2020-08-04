# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:41:27 2020

@author: USER
"""

score=[]
total=0
avg=0

p=int(input("請輸入人數:　"))

for i in range(p):
    s=int(input("請輸入分數: "))
    score.append(s)
for j in score:
    total=total+j
print("總分: ",total) 
print("平均: ",total/p) 