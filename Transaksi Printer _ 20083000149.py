# -*- coding: utf-8 -*-
"""
Created on Wed Jun  11 10:33:40 2021

@author: Raihan Ihza Pravisya
"""

#Transaksi printer
ulang="y"
while ulang=="y" or ulang=="Y":
    print ("===========================")
    print (" Program ini dibuat oleh ")
    print (" Raihan Ihza Pravisya ")
    print (" Menghitung Transaksi Printer ")
    print ("===========================")
    
    harga=660000
    jml=0
    while jml>=0:
        jml=int(input ("--> Jumlah printer yang dibeli:"))
        if jml>=0:
            total = harga*jml
            print("--> Total pembayaran: Rp.", total)
    
            ulang = input("--> Ingin Mengulang program ini? Iya/Tidak:")
            if ulang=="t" or ulang=="T":
                break
        else:
            pesan="(Nilai inputan harus lebih dari 0)"
            print(pesan)
            break
