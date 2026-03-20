largura = float(input('Digite a largura de uma parede (m): '))
altura = float(input('Digite a altura de uma parede (m): '))
área = largura * altura
print(f'A área de sua parede é {área:.2f}m²')
litros = área/2
print(f'Serão necessários {litros}L de tinta para pintá-la.')
