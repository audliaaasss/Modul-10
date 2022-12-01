# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 14:26:44 2022

@author: Audi Aulia
"""

mylist = [28, 8, 2, 4, 82, 31, 100, 81, 75, 66]
mysearch = int(input("Masukkan angka yang dicari : "))

def sorting (List, search):
    counter = 0
    while counter != len(mylist):
        if mylist[counter] == search:
            result = counter
        counter += 1
    return result

output = sorting(mylist, mysearch)+1
if mysearch not in mylist:
    print(mylist)
    print("Elemen tidak ditemukan pada list")
else:
    print("Sesudah di Sorting : ", mylist)
    print("Elemen ditemukan pada posisi ke - ", output)