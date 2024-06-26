pesoPeixe = float(input('Insira o peso do peixe: '))

if pesoPeixe > 50:
    pesoExtra = pesoPeixe - 50
    print('O peso extra é de: ', pesoExtra, 'quilos')
    taxa = pesoExtra * 4
    print('Você terá que pagar uma taxa de: ', taxa, 'reais.')
else:
    print('Não terá que pagar nenhuma taxa.')
