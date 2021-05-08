#!/bin/python3
#Script para calculo do imc
#by <stringuetta@gmail.com>

import os

# Limpa a tela de acordo com o Sistema operacional
if os.name == 'nt':
	os.system('cls') or None
else:
	os.system('clear') or None

# Inicio Programa Calculo IMC
print ('Calculo de IMC')
print ('Legenda:')
print ('menor que 18.5 - magreza')
print ('entre 18.5 e 24.9 - normal')
print ('entre 25.0 e 29.9 - sobrepeso')
print ('entre 30.0 a 39.9 - obesidade')
print ('maior que 40.0 - obesidade grave\n')

nome = input('Digite o seu nome: ')
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
calculo = peso / (altura * altura)

if calculo <= 18.5:
	print (nome,'seu IMC e de {:.2f}'.format(calculo),'magreza')
elif calculo >= 18.5 and calculo < 24.9:
	print (nome,'seu IMC e de {:.2f}'.format(calculo),'normal')
elif calculo >= 25.0 and calculo < 29.9:
	print (nome,'seu IMC e de {:.2f}'.format(calculo),'sobrepeso')
elif calculo >= 30.0 and calculo < 39.9:
	print (nome,'seu IMC e de {:.2f}'.format(calculo),'obesidade')
elif calculo > 40.0:
	print (nome,'seu IMC e de {:.2f}'.format(calculo),'obesidade grave')
else:
	print ('Valor nao encontrado')
	



