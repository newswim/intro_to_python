# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:28:13 2016

@author: dm
"""

# Return a number corresponding to the character sequences occuring in a string


s = "heynowbobhowu doingbob isthat bob?"

def countCharSeq(string, substring):
    string_size = len(string)
    substring_size = len(substring)
    count = 0
    for i in range(0,string_size-substring_size+1):
        if string[i:i+substring_size] == substring:
            count+=1
    print ("Number of times bob occurs is: " + str(count))
    return
countCharSeq(s,'bob')
