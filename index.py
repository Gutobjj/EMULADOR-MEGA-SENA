numbers = [10, 27, 40, 46, 49, 58, 2, 10, 34, 37, 43, 50, 3, 4, 29, 36, 45, 55, 14, 32, 33, 36, 41, 52, 20, 30, 36, 38, 47, 53, 1, 5, 11, 16, 20, 56, 2, 18, 31, 42, 51, 56, 5, 11, 22, 24, 51, 53, 3, 6, 10, 17, 34, 37, 5, 10, 12, 18, 25, 33, 3, 35, 38, 40, 57, 58, 17, 20, 22, 35, 41, 42, 12, 15, 23, 32, 33, 46]

counts = {}

# conta as ocorrências de cada número
for number in numbers:
    if number not in counts:
        counts[number] = 1
    else:
        counts[number] += 1

# imprime os números que aparecem mais de 2 vezes
for number, count in counts.items():
    if count >= 2:
        print(number)
