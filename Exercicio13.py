altura = float(input('Digite sua altura: '))

pesoIdealH = ((72.7 * altura) - 58)
pesoIdealM = ((62.1 * altura) - 44.7)

print('Seu peso ideal se for homem é de: {:.2f}'.format(pesoIdealH))
print('Seu peso ideal se for mulher é de: {:.2f}'.format(pesoIdealM))