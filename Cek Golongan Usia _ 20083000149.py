# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 21:10:44 2021

@author: tadak
"""

#cek golongan usia
ulang = "y"
while ulang=="y" or ulang=="Y":
    print ("=========================")
    print ("Program Ini dibuat Oleh")
    print ("Raihan Ihza Pravisya")
    print ("CEK GOLONGAN USIA ")
    print ("=========================")
    
    n=1
    while int(n)>0 and int(n)<=100:
        n = input("--> Masukkan Usia: ")
        #cek batasan inputan usia 0-100
        if int(n)>0 and int(n)<=100:
            if int(n)>=60: sts="lansia"
            elif int(n)>=35: sts="dewasa"
            elif int(n)>=18: sts="pemuda"
            elif int(n)>=15: sts="remaja"
            else: sts="anak"
            print (sts)

            ulang = input("--> Ingin Mengulang program? Iya/Tidak:")
            if ulang=="t" or ulang=="T":
                break
        else:
            pesan="(Masukkan angka usia 0-100 saja)"
            print(pesan)
            break