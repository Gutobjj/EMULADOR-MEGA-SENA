import random

def mega_sena(q):
    return [sorted(random.sample(range(1, 61), 6)) for _ in range(q)]

quant = int(input('Quantidade de palpites: '))

for palpite in mega_sena(quant):
    print(' '.join([f'{num:02}' for num in palpite]))
