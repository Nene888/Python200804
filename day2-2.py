# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:20:04 2020

@author: USER
"""

import random
xyz = random.randint(1,20)

while True:
    a=int (input("請輸入1~20的數字: "))    
    if a<0 and a>=20:
        print("錯誤")
    else:
        if xyz <a:
            print("小一點")
        elif xyz >a:
            print("大一點")
        else:
            print("BINGO")
            break
