# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 14:11:02 2022

@author: fns
"""

#judul
print('Prgram menjumlahkan 2 array dengan kapasitas yang sama ')
a = 30
b = 60

print('[nilai awal]')
print(f'a = {a}, b = {b}\n')

#hanya menggunakan penjumlahan dan pengurangan 
a = a + b
b = a - b
a = a - b
print('[nilai akhir]')
print(f'c = {a},{b}\n')