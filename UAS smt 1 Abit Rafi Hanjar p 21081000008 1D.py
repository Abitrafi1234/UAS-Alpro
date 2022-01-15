# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 09:02:43 2022

@author: fns
"""
#judul
print('program mengurutkan bilangan dari yang terkecil ke yang terbesar')
#input angka
def pengulangan():
    print ('masukkan 3 bilangan yang diinginkan!')
    a=int(input('bilangan1 = '))
    b=int(input('bilangan2 = '))
    c=int(input('bilangan3 = '))
#menentukan bilangan terkecil ke terbesar
    print()
    print('hasil pengurutannya adalah :')

    if a<b and a<c:
        if b<c:
            print( a, b, c)
        else:
            print(a, c, b)
    elif b<a and b<c:
        if a<c:
            print(b, a, c)
        else:
            print(b, c, a)
    else:
        if a<b:
            print(c, a, b)
        else:
            print(c, b, a)

#input untuk menentukan pengulangan
    print('')
    print('ingin coba lagi? (y/n)')
    x=input()
    if x=='y':
        return pengulangan()
    if x=='n':
        print('terima kasih telah menggunakan program ini.')
pengulangan()