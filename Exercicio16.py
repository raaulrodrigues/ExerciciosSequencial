import math

tamanhoParede = float(input('Digite o tamanho da parede: '))

tintaNecessaria = (tamanhoParede / 3)

latasNecessaria = math.ceil(tintaNecessaria / 18)

precoFinal = (latasNecessaria * 80)

print(f"Você precisará de {latasNecessaria} latas de tinta.")
print(f"O preço total será de R$ {precoFinal:.2f}.")