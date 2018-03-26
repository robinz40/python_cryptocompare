#!/usr/bin/env python3.6
#-*- coding: utf-8 -*-

import cryptocompare

print('---------------------------------------')
print('-------------Script crypto-------------')
print('---------------------------------------')

def choisir ():
    choice = int(input("1 - Lister les crypto-monnaies\n2 - Chercher la crypto-monnaie dont vous voulez connaitre le prix\nChoix :  "))

    if choice==1:
        list_crypto = cryptocompare.get_coin_list(format=True)
        for crypto in list_crypto:
            print(crypto)
    elif choice==2:
        cryptosearch=input("Entrer l'identifiant de la crypto-monnaie dont vous voulez connaitre le prix\nChoix : ")
        devise=input("Entrer la devise désirée (USD ou EUR)\nChoix : ")
        prix= cryptocompare.get_price(cryptosearch,curr=devise,full=True)
        print("Prix pour la monnaie "+ cryptosearch +" : "+ str(prix['RAW'][cryptosearch][devise]['PRICE']))
        print('---------------------------------------')
    else:
        print('---------------------------------------')
        print("Merci de rentrer seulement 1 ou 2")
        print('---------------------------------------')

while True:
	try:
		choisir()

	except:
		print("\nValeur incorrect, recommencez \n")



