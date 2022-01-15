# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 21:10:24 2022

@author: fns
"""
#judul
print("PROGRAM BILANGAN TERBESAR DARI 3 BUAH BILANGAN YANG DIINPUTKAN") 
#Siapkan Variabel 
def pengulangan():
    A= int(input("Masukan bilangan pertama = ")) 
    B= int(input("Masukan bilangan kedua   = ")) 
    C= int(input("Masukan bilangan ketiga  = "))  
#Menentukan bilangan terbesar
    if A > B and A > C: print(A, ':Adalah terbesar dari 3 bilangan yang diinputkan') 
    elif B > A and B > C: print(B, ':Adalah terbesar dari 3 bilangan yang diinputkan') 
    else: print(C, ':Adalah terbesar dari 3 bilangan yang diinputkan')


#Membuat inputan pengulangan
    print('')
    print('ingin coba lagi? (y/n)')
    x=input()
    if x=='y':
        return pengulangan()
    if x=='n':
        print('Terimakasih!') 
pengulangan()