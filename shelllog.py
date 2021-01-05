#!/usr/bin/env python3

shell = input("Dosya konumunu giriniz: ") #CODED BY ATHENA
dosya = open(shell, "r")

f = open(shell)

aranan = ("@hotmail" or "@gmail" or "$kime" or "mail(" or "to_mail" )
for satir in f:
    if aranan in satir:
        print ("Bu shell loglu amına koyim")

dosya.close()
