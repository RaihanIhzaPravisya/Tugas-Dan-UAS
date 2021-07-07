# -*- coding: utf-8 -*-
"""
Created on Wed Jun  11 09:40:20 2021

@author: Raihan Ihza Pravisya
"""

#Transaksi printer dengan diskon 15% jika total > 1,5jt
ulang="y"
while ulang=="y" or ulang=="Y":
    print("===========================")
    print(" Program ini dibuat oleh ")
    print(" Raihan Ihza Pravisya ")
    print(" Menghitung Transaksi Printer ")
    print("===========================")
    
    harga=660000
    diskon= 15/100
    jml=0
    while jml>=0:
        jml=int(input ("--> Jumlah printer yang dibeli:"))
        if jml>=0:
            total = harga*jml
    
            if total>1500000:
                totDiskon = total*diskon
                totBayar = total-totDiskon
                print("--> Total diskon    : Rp.",int(totDiskon))
                print("--> Total pembayaran: Rp.",int(totBayar))
            else:
                totDiskon = 0
                print("--> Total diskon    : Rp.",int(totDiskon))
                print("--> Total pembayaran: Rp.",int(total))
    
            ulang = input("--> Ingin Mengulang program ini? Iya/Tidak:")
            if ulang=="t" or ulang=="T":
                break
        else:
            pesan="(Nilai inputan harus lebih dari 0)"
            print(pesan)
            break