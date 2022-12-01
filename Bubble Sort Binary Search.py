# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:20:05 2022

@author: Audi Aulia
"""

def change (A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    
def bubbleSort (A, n):
    for i in range (n - 1):
        if A[i] > A[i + 1]:
            change (A, i, i + 1)
    if n - 1 > 1:
        bubbleSort(A, n - 1)
        
A = [8, 3, 0, -10, 6, 1, -2]
bubbleSort(A, len(A))
print("List yang sudah disorting : ")
print(A)