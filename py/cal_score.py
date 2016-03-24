# -*- coding: utf-8 -*-
'''
Calculate nutrition score based on
UK Department of Health Guide
@author: bambooom
'''

import math

def cal_A_pts(energy=0,sat_fat=0,sugar=0,sodium=0):
    ```
    energy in unit kJ
    sat_fat, sugar in unit g
    sodium in unit mg
    ```
    A_nutrition = [energy,sat_fat,sugar,sodium]
    A_coeff = [335.0,1.0,4.5,90.0] # 发现每一项都是和某个系数有关
    A_pts = [0,0,0,0]
    # energy
    for i in range(len(A_nutrition)):
        if A_nutrition[i] <= 10*A_coeff[i]:
            if A_nutrition[i] == math.floor(A_nutrition[i]):
                A_pts[i] = A_nutrition[i] - 1
            else:
                A_pts[i] = math.floor(A_nutrition[i]/A_coeff[i])
        else:
            A_pts[i] = 10

    return sum(A_pts)

def cal_C_pts(fvn=0,fibre=0,protein=0):
    ```
    fruit, vegetable & nuts %
    fibre in unit g
    protetin in unit g
    ```
    C_pts = [0,0,0]
    if fvn <= 40:
        C_pts[0] = 0
    elif fvn <= 60:
        C_pts[0] = 1
    elif fvn <= 80:
        C_pts[0] = 2
    else: # no 3, 4 pts
        C_pts[0] = 5

    C_nutrition = [fibre,protein]
    C_coeff = [0.7, 0.9]
    for i in range(len(C_nutrition)):
        if C_nutrition[i] <= 5*C_coeff[i]:
            if C_nutrition[i] == math.floor(C_nutrition[i]):
                C_pts[i+1] = C_nutrition[i] - 1
            else:
                C_pts[i+1] = math.floor(C_nutrition[i]/C_coeff[i])
        else:
            A_pts[i] = 5
    return sum(C_pts)
