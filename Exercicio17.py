import math

tamanhoParede = float(input('Digite o tamanho da parede: '))

tintaNecessaria = (tamanhoParede / 6)

latasNecessaria = math.ceil(tintaNecessaria / 18)
galoesNecessarios = math.ceil(tintaNecessaria / 3.6)

precoFinalLata = (latasNecessaria * 80)
precoFinalGalao = (latasNecessaria * 25)

lataMistura = int(tintaNecessaria / 18)
tintaResto = tintaNecessaria % 18
galoesMistura = math.ceil(tintaResto / 3.6)


precoMistura = (lataMistura * 80) + (galoesMistura * 25)






print(f"\nSituação 1: Você precisará de {latasNecessaria} latas de tinta.")
print(f"Situação 2: O preço total será de R$ {precoFinalLata:.2f}.")

print(f"\nSituação 3:\nQuantidade de latas necessárias: {lataMistura}")
print(f"Quantidade de galões necessários: {galoesMistura}")
print(f"Preço total: R$ {precoMistura:.2f}")


