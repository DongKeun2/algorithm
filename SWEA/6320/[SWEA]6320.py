# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 15:38:41 2022

@author: ehdrm
"""

name_1 = input()
name_2 = input()
x_1 = input()
x_2 = input()

t = {name_1:x_1,name_2:x_2}

def win(x,y):
    if x == y:
        return print("draw")
    elif (x == "가위" and y == "바위") or (x == "바위" and y == "가위"):
        print("바위가 이겼습니다!")
    elif (x == "바위" and y == "보") or (x == "보"and y == "바위"):
        print("보가 이겼습니다!")
    elif (x == "보", y =="가위") or (x == "가위", y == "보"):
        print("가위가 이겼습니다!")
    else:
        print("가위, 바위, 보 중 하나를 입력해주세요.")

win(x_1,x_2)