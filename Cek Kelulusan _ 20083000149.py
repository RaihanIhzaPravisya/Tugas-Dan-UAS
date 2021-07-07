# -*- coding: utf-8 -*-
"""
Created on Wed Jun  11 07:24:00 2021

@author: Raihan Ihza Pravisya
"""

#Cek kelulusan, jika nilai > 80 maka lulus
ulang = "y"
while ulang=="y" or ulang=="Y":
    
    print("=============================")
    print  (" Program Ini dibuat Oleh ")
    print   (" Raihan Ihza Pravisya ")
    print("        Cek Kelulusan        ")
    print("=============================")
    
    n=0
    while n<=100:
        n = int(input("--> Masukkan nilai :"))
        if int(n<=100):
            if int(n)>60:
                sts = "Lulus"
            else:
                sts = "Tidak Lulus"
            print ("--> Status anda:",sts)
    
            ulang = input("Ingin Mengulangi program? Iya/Tidak:")
            if ulang=="t" or ulang=="T":
                break
        else:
            pesan="(Nilai inputan harus kurang dari 100)"
            print(pesan)
            break
