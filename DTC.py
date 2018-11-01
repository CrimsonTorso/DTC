#!/user/bin/python3

import os
import externalTemp

responce = os.system("clear")
print('[!] Created By CrimsonTorso [!]')
print('''
	\n
	''')
print('Welcome to SE Template Creator!')
print('Please input a number from 1-5')
print('1 - Basic template')
print('2 - Semi basic template')
print('3 - Large template')
print('4 - About / Contact')
print('5 - Exit DTC')
templateNum = raw_input()

if templateNum == '1':
	externalTemp.temp1()
if templateNum == '2':
	externalTemp.temp2()
if templateNum == '3':
	externalTemp.temp3()
if templateNum == '4':
	responce = os.system("clear")
	print('''
DTC is a tool used for creating SE-based templates for storing and compiling massive amounts of data
on a specific target or victim. Please be aware that I am not responcible for what you do this for or with.
<3 ~ CrimsonTorso
		''')
elif templateNum == '5':
	responce = os.system("clear")
	print('Quitting!')