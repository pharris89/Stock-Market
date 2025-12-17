# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 20:02:27 2022

@author: Paula Harris
"""


count = 0

sum = 0

full_name = input("What is your full name? ")
min_price = float(input("What's the minimum price? "))
price_list = [27.3, 53.2, 77.5, 92.1, 110.7]

for price in price_list:
    sum=sum+price
    if price > min_price:
        count = count + 1 
print("Hello",full_name,"the minimum price is ",min_price)
print("There are ",count,"prices greater than the minimum price")
print("The total price is ",sum)

