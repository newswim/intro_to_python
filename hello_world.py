# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 01:40:17 2016

@author: dm
"""

def countVowels (str):
    total = 0
    for letter in str:
        if (letter == 'a'
         or letter == 'e'
         or letter == 'i'
         or letter == 'o'
         or letter == 'u'):
            total+=1
    print('Number of vowels: ', total)
    return

countVowels('blahblahzzzzuiozee')
