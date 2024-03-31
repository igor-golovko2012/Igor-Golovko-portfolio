# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:46:17 2023

@author: Наталья
"""
# эту функцию можно использовать для правильного употребления секунд, минут, часов, дней, недель месяцев и не только


def choose_plural(x, words):
    
    if 5 <= x <= 20 or 5 <= x % 10 <= 9 or x % 10 == 0 or 11 <= x % 100 <= 20:
        return str(x) + " " + words[2]
    elif x == 1 or x % 10 == 1:
        return str(x) + " " + words[0]
    else:
        return str(x) + " " + words[1]
    
    
for i in range(100):    
    print(choose_plural (i, ['год', 'года', 'лет']), 
          choose_plural (i, ['рубль', 'рубля', 'рублей']), 
          choose_plural (i, ['копейка', 'копейки', 'копеек']))
