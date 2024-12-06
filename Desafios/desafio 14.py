# Faça um programa que leia, uma temperatura em Graus Celcius e converta para Farenheit

celsius = float(input('Informe a Temperatura em ºC:'))
fahrenheit = celsius*9/5 + 32

print('A temperatura de {}ºC, corresponde a {}ºF'.format(celsius, fahrenheit))