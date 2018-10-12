# -*- coding: utf-8 -*
-
# elitehuitzil@gmail.com
# Give a tip: paypal.me/tzil
# Cómprame un refresco: paypal.me/tzil

import re

#	CURP ejemplo: SIHC400128HDFLLR0

#	Expresión regular de la CURP
CURPVALID = (r"^[A-Z]{1}[AEIOUX]{1}[A-Z]{2}((\d{2}((0[13578]|1[02])(0[1-9]|[12][0-9]|3[01])|(0[13-9]|1[0-2])(0[1-9]|[12][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8])))|([02468][048]|[13579][26])0229)[HM]{1}(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[B-DF-HJ-NP-TV-Z]{3}[0-9A-Z]{1}[0-9]$")

def curp_validate(curp):
	if curp:
		CURP_REGEX = re.compile(CURPVALID)
		if not CURP_REGEX.match(curp):
			#	Si no está con el formato correcto.
			print('''El formato de la CURP no es válido.''')
		else:
			#	Contesta si es hombre o mujer largo.
			def gender(gender):
				return {
					'H': "Hombre",
					'M': "Mujer"
					}[gender]
			
			#	Contesta el lugar de nacimiento largo.
			def birthplace(birthplace):
				return {
				'AS' :	'Aguascalientes',
				'BC' :	'Baja California',
				'BS' :	'Baja California Sur',
				'CC' :	'Campeche',
				'CL' :	'Coahuila',
				'CM' :	'Colima',
				'CS' :	'Chiapas',
				'CH' :	'Chihuahua',
				'DF' :	'Distrito Federal',
				'DG' :	'Durango',
				'GT' :	'Guanajuato',
				'GR' :	'Guerrero',
				'HG' :	'Hidalgo',
				'JC' :	'Jalisco',
				'MC' :	'México',
				'MN' :	'Michoacán',
				'MS' :	'Morelos',
				'NT' :	'Nayarit',
				'NL' :	'Nuevo León',
				'OC' :	'Oaxaca',
				'PL' :	'Puebla',
				'QT' :	'Querétaro',
				'QR' :	'Quintana Roo',
				'SP' :	'San Luis Potosí',
				'SL' :	'Sinaloa',
				'SR' :	'Sonora',
				'TC' :	'Tabasco',
				'TS' :	'Tamaulipas',
				'TL' :	'Tlaxcala',
				'VZ' :	'Veracruz',
				'YN' :	'Yucatán',
				'ZS' :	'Zacatecas',
				'NE' :	'Nacido Extranjero'
			    }[birthplace]

			#	Se obtiene año de nacimiento.
			year_birth = curp[4:6]
			#	Se obtiene mes de nacimiento.
			month_birth = curp[6:8]
			#	Se obtiene día de nacimiento.
			day_birth = curp[8:10]
			#	Se obtiene género.
			gender = gender(curp[10])
			#	Se obtiene lugar de nacimiento.
			birthplace = birthplace(curp[11:13])
			#	Opcional, dando formato a la fecha de nacimiento.
			birthday = str(day_birth + month_birth + year_birth)
			#	Fin, regresa como lo necesitemos.
			return curp, birthday, gender, birthplace

# Intercativo
curp = input("Escribe la CURP que deseas checar: ")

print (curp_validate(curp))


# elitehuitzil@gmail.com
# Give a tip: paypal.me/tzil
# Cómprame un refresco: paypal.me/tzil
