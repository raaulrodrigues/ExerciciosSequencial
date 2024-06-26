tamanhoArq = int(input('Insira o tamanho do arquivo em  MB: '))
velocidadeDown = int(input('Insira a velocidade em Mbps: '))

calc = tamanhoArq / (velocidadeDown/8)
calcMin = calc / 60
print('O tempo de download do arquivo em segundos é: ', calc)
print('O tempo de download do arquivo em minutos é: {:.2f}'.format(calcMin))

