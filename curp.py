# -*- coding: utf-8 -*-
# elitehuitzil@gmail.com

import re

CURPVALID = (r"^[A-Z]{1}[AEIOUX]{1}[A-Z]{2}((\d{2}((0[13578]|1[02])(0[1-9]|[12][0-9]|3[01])|(0[13-9]|1[0-2])(0[1-9]|[12][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8])))|([02468][048]|[13579][26])0229)[HM]{1}(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[B-DF-HJ-NP-TV-Z]{3}[0-9A-Z]{1}[0-9]$")

def curp_validate(curp):
	if curp:
		CURP_REGEX = re.compile(CURPVALID)
		if not CURP_REGEX.match(curp):
			#raise ValidationError(_('''it seems like CURP is not valid.'''))
			print('''it seems like CURP is not valid.''')
		else:
			def gender(gender):
				return {
					'H': "Hombre",
					'M': "Mujer"
					}[gender]

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

			year_birth = curp[4:6]
			month_birth = curp[6:8]
			day_birth = curp[8:10]
			gender = gender(curp[10])
			birthplace = birthplace(curp[11:13])
			birthday = str(day_birth + month_birth + year_birth)
			return curp, birthday, gender, birthplace
		

curp = 'TEGE840410HPLHLL02'
print (curp_validate(curp))
