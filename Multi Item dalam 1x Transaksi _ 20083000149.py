# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 10:22:17 2021
@author: Raihan Ihza Pravisya
NIM    : 20083000149
"""

kode =['a','b','c','d','e','f','g','h','i','j']
menu =['Nasi Goreng','Lontong Goreng','Bakso Goreng','Rujak Goreng','Rujak Bakso Pecel','Teh Dingin/Hangat/panas','Kopi Dingin','Kopi Teh Panas','Coca Cola Dingin','Coca Cola Panas']
harga = [15000,14900,12900,13000,17000,2500,5000,6500,3500,5000]
mkn_dpsn    = []
mnn_dpsn    = []
jmkn_dpsn   = []
jmnn_dpsn   = []
H_mkn       = []
H_mnn       = []
JH_mkn      = []
JH_mnn      = []

ulang = "y"
while ulang=="y" or ulang=="Y":

    lain = "y"
    while lain== "y" or lain=="Y":
        
        
        print("")
        print("Selamat datang di..")
        print("Kantin Fakultas Tek. Informasi")
        print("==========================================")
        print("")
        print("Ketik y/Y untuk setuju, t/T untuk batal.. ")
        pesan_mkn = input("Pesan makan? ")
        if pesan_mkn=="y" or pesan_mkn=="Y":
            mkn = "y"
            while mkn=="y" or mkn=="Y":
                print("")
                print("Kantin Fakultas Tek. Informasi")
                print("==========================================")
                print(" MENU MAKANAN: ")
                print("==========================================")
                print(" a | Nasi Goreng              | Rp 15.000")
                print(" b | Lontong Goreng           | Rp 14.900")
                print(" c | Bakso Goreng             | Rp 12.900")
                print(" d | Rujak Goreng             | Rp 13.000")
                print(" e | Rujak Bakso Pecel        | Rp 17.000")
                print("==========================================")
                print(" MENU MINUMAN: ")
                print("==========================================")
                print(" f | Teh Dingin/Hangat/panas  | Rp 2.500")
                print(" g | Kopi Dingin              | Rp 5.000")
                print(" h | Kopi Teh Panas           | Rp 6.500")
                print(" i | Coca Cola Dingin         | Rp 3.500")
                print(" j | Coca Cola Panas          | Rp 5.000")
                print("==========================================")
                print("")
                pilihan_mkn  = input("Pilih kode Menu makanan: ")
                qty          = input("Berapa banyak yang akan di beli: ")
                jmkn_dpsn.append(qty)
                i = 0
                while i<len(menu):
                    if kode[i] == pilihan_mkn:
                        nm_mkn = menu[i]
                        hrg_mkn = harga[i]
                    i+=1
            
                totHarMkn = hrg_mkn * int(qty)
                totHar1 = totHarMkn
                
                mkn_dpsn.append(nm_mkn)
                H_mkn.append(hrg_mkn)
                JH_mnn.append(totHar1)
                
                print("")
                print("==========================================")
                print(">>> NAMA Menu        : " + nm_mkn)
                print(">>> HARGA            : " + str(hrg_mkn))
                print(">>> JUMLAH           : " + qty)
                print(("-------------------------------"))
                print(">>> TOTAL Harga      : " + str(totHar1))
                mkn = input("Pesan makanan lagi? ")
                if mkn=="t" or mkn=="T":
                    pass
                    
        elif pesan_mkn=="t" or pesan_mkn=="T":
            pass
        
        pesan_mnm = input("Pesan minum? ")
        if pesan_mnm=="y" or pesan_mnm=="Y":
            mnn = "y"
            while mnn=="y" or mnn=="Y":
                print("")
                print("Kantin Fakultas Tek. Informasi")
                print("==========================================")
                print(" MENU MAKANAN: ")
                print("==========================================")
                print(" a | Nasi Goreng              | Rp 15.000")
                print(" b | Lontong Goreng           | Rp 14.900")
                print(" c | Bakso Goreng             | Rp 12.900")
                print(" d | Rujak Goreng             | Rp 13.000")
                print(" e | Rujak Bakso              | Rp 17.000")
                print("==========================================")
                print(" MENU MINUMAN: ")
                print("==========================================")
                print(" f | Teh Dingin/Hangat/panas  | Rp 2.500")
                print(" g | Kopi Dingin              | Rp 5.000")
                print(" h | Kopi Teh Panas           | Rp 6.500")
                print(" i | Coca Cola Dingin         | Rp 3.500")
                print(" j | Coca Cola Panas          | Rp 5.000")
                print("==========================================")
                print("")
                pilihan_mnm  = input("Pilih kode Menu minuman: ")
                qty2         = input("Berapa banyak yang akan di beli: ")
                jmnn_dpsn.append(qty2)
                i = 0
                while i<len(menu):
                    if kode[i] == pilihan_mnm:
                        nm_mnn = menu[i]
                        hrg_mnn = harga[i]
                    i+=1
                
                totHarMnn = hrg_mnn * int(qty2)
                totHar2 = totHarMnn
                
                mnn_dpsn.append(nm_mnn)
                H_mnn.append(hrg_mnn)
                JH_mnn.append(totHar2)
                
                print("")
                print("==========================================")
                print(">>> NAMA Menu        : " + nm_mnn)
                print(">>> HARGA            : " + str(hrg_mnn))
                print(">>> JUMLAH           : " + qty2)
                print(("-------------------------------"))
                print(">>> TOTAL Harga      : " + str(totHar2))
                mnn = input("Pesan minuman lagi? ")
                if mnn=="t" or mnn=="T":
                    pass
            
        elif pesan_mnm=="t" or pesan_mnm=="T":
            pass
                
        Har1 = sum(H_mkn)
        Har2 = sum(H_mnn)
        
        selesai = input("Cetak tagihan pembayaran? ")
        if selesai=="y" or selesai=="Y":
            
            totHar = Har1 + Har2
            print("")
            print("Rincian Transaksi:")
            print("==========================================")
            print(">>> NAMA Menu         ")
            print("Makanan: ")
            print("---------------")
            for x in mkn_dpsn:
                print (x + "    || Jumlah: " + str(qty) +" || Harga tiap menu ==> " + str(hrg_mkn))
            print("minuman: ")
            print("---------------")
            for x in mnn_dpsn:
                print (x + "    || Jumlah: " + str(qty2) +" || Harga tiap menu ==> " + str(hrg_mnn))
            print(("****************************************"))
            print(">>> TOTAL Harga      : Rp " + str(totHar))
            
            print("==========================================")
            Bayar = input("=> Masukkan nominal pembayaran: Rp ")
            Kembalian = int(Bayar) - totHar
            
            print("")
            print("=> Kembalian: Rp " + str(Kembalian))
            print("==========================================")
            
        
        elif selesai=="t" or selesai=="T":
            pass
        
        lain = input("Ulangi pemesanan? ")
        if lain=="t" or lain=="T":
            print("")
            print("Terimakasih sudah berkunjung..")
            break
    break