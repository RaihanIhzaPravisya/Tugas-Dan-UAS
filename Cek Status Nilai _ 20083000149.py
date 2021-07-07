# -*- coding: utf-8 -*-
"""
Created on Wed Jun  10 07:29:34 2021

@author: Raihan Ihza Pravisya
"""

#cek status nilai
ulang = "y"
while ulang=="y" or ulang=="Y":
    print ("=========================")
    print (" Program Ini dibuat oleh ")
    print ("  Raihan Ihza Pravisya   ")
    print ("    CEK STATUS NILAI     ")
    print ("=========================")
    
    n=1
    while int(n)>=0 and int(n)<=100:
        n=input("--> Masukkan Nilai:")
        #cek batasan inputan usia 0-100
        if int(n)>=0 and int(n)<=100:
            if int(n)>80: sts="Baik Sekali"
            elif int(n)>=65: sts="Baik"
            elif int(n)>=55: sts="Cukup"
            elif int(n)>=40: sts="Kurang"
            else: sts="Kurang Sekali"
            print("--> Status nilai anda:",sts)
            
            ulang = input("--> Ingin Mengulang program? Iya/Tidak:")
            if ulang=="t" or ulang=="T":
                break
        else:
            pesan="(Nilai inputan 0-100)"
            print(pesan)
            break