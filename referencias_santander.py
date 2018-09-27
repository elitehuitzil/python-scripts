# -*- coding: utf-8 -*-
###############################################################################
#
#   coder: elitehuitzil@gmail.com
#   
#       BANCO SANTANDER MÉXICO
#       ALGORITMO No. 22 Módulo 22 numérico Año Base 2009
#
#   Parámetros requeridos para el cálculo:
#   Tipo de Referencia : Numérica (N)
#   Longitud Mínima de la Referencia : 20
#   Longitud Máxima de la Referencia : 40
#   Longitud Dígito Verificador : 02
#   Divisor : 10
#   Factor Fijo : 1
#   Constante : 2
#
###############################################################################

import datetime
# referencia interna, puede ser folio de factura, matricula, numerod e cliente, etc.
referencia = '123016102016'
# el monto que debe paga el cliente.
importe = '4918.00'
# la fecha límite de pago para el cliente
fecha_vencimiento = '11-06-2017'

# estos datos son propios del algoritmo 22 de Santander.
ano = 2009
divisor = 10
divisor2 = 97
factorfijo = 1
constante = 2

# algoritmo...
fecha_condensada = 0
importe_condensado = 0

date = datetime.datetime.strptime(fecha_vencimiento, "%d-%m-%Y")
dia_vencimiento = date.day
mes_vencimiento = date.month
ano_vencimiento = date.year
ano_condensado = (ano_vencimiento - ano) * 372
mes_condensado = (mes_vencimiento - 1) * 31
dia_condensado = dia_vencimiento - 1
fecha_condensada = dia_condensado + mes_condensado + ano_condensado

importe = importe.replace(".", "")
digitos = importe[::-1]
suma = 0
regla = [7, 3, 1]
inter = 0
for numero in digitos:
    numero = int(numero)
    suma += numero * regla[inter]
    if inter == 2:
        inter = 0
    else:
        inter += 1
importe_condensado = suma - (divisor * (suma / divisor))

referencia_str = (str(referencia) + str(fecha_condensada) + str(importe_condensado) + str(constante))
regla_dv = [11, 13, 17, 19, 23]
referencia = referencia_str[::-1]
suma = 0
inter2 = 0
for numero in referencia:
    numero = int(numero)
    suma += numero * regla_dv[inter2]
    if inter2 == 4:
        inter2 = 0
    else:
        inter2 += 1
digito_verificador = (suma - (divisor2 * (suma / divisor2))) + factorfijo

if len(str(digito_verificador)) == 1:
            digito_verificador = '0' + str(digito_verificador)

referencia_bancaria = referencia_str + str(digito_verificador)

# formato XXXX XXXX XXXX XXXX XXXX
def encrypt(string, length):
    return ' '.join(string[i:i + length] for i in xrange(0, len(string), length))

# print :)
print "referencia = %s" % encrypt(referencia_bancaria, 4)
