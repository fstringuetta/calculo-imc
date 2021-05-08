#!/bin/python3
#Script para calculo do imc
#by <stringuetta@gmail.com>

import os
from termcolor import colored

# Limpa a tela de acordo com o Sistema operacional
if os.name == 'nt':
	os.system('cls') or None
else:
	os.system('clear') or None

# Inicio Programa Calculo IMC
print (colored('Calculo de IMC','red'))
print (colored('Legenda:','green'))
print (colored('Menor que 18.5 - Magreza','cyan'))
print (colored('Entre 18.5 e 24.9 - Normal','cyan'))
print (colored('Entre 25.0 e 29.9 - Sobrepeso','cyan'))
print (colored('Entre 30.0 a 39.9 - Obesidade','cyan'))
print (colored('Maior que 40.0 - Obesidade Grave\n','cyan'))

nome = input('Digite o seu nome: ')
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
calculo = peso / (altura * altura)

if calculo <= 18.5:
	print (nome,'seu IMC e de {:.2f}'.format(calculo),'\033[0;33mMagreza\033[m')
elif calculo >= 18.5 and calculo < 24.9:
	print (nome,'seu IMC e de {:.2f}'.format(calculo),'\033[0;33mNormal\033[m')
elif calculo >= 25.0 and calculo < 29.9:
	print (nome,'seu IMC e de {:.2f}'.format(calculo),'\033[0;33mSobrepeso\033[m')
elif calculo >= 30.0 and calculo < 39.9:
	print (nome,'seu IMC e de {:.2f}'.format(calculo),'\033[0;33mObesidade\033[m')
elif calculo > 40.0:
	print (nome,'seu IMC e de {:.2f}'.format(calculo),'\033[0;33mObesidade Grave\033[m')
else:
	print ('Valor nao encontrado')
