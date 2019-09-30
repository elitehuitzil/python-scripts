# -*- coding: utf-8 -*-
# elitehuitzil@gmail.com
# Give a tip: paypal.me/tzil
# Cómprame un refresco: paypal.me/tzil

# todas las denominaciones de los billetes
bills = [1000, 500, 200, 100, 50, 20] 
# todas las denominaciones de las monedas
coins = [10, 5, 2, 1, .5, .2, .1]
# es posible modicar las denominaciones para funcione en tu país

def changing(change):
	if(change <= 0.0):
		return
	for b in bills:
		ese = ""
		bill_count, change = divmod(change, b)
		if bill_count != 0:
		    if bill_count > 1:
		        ese = "s"
		    msg = "{} billete{} de ${}"
		    print(msg.format(int(bill_count), ese, b))
		if(change < bills[-1]):
			for c in coins:
			    ese = ""
			    coin_count, change = divmod(change, c)
			    if coin_count != 0:
			        if coin_count > 1:
			        	ese = "s"
			        msg = "{} moneda{} de ${}"
			        print(msg.format(int(coin_count), ese, c))

print('Escribe la cantidad:')
amount_input = float(input())
amount = float("{0:.2f}".format(amount_input))
print('La cantidad ingresada es $', amount)
print('en billetes y monedas:')
changing(amount)