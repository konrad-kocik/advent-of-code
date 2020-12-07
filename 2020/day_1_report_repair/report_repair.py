with open('input.raw', 'r') as file:
    numbers = list(map(int, file.readlines()))

correct = [i * j * k for i in numbers for j in numbers for k in numbers if i + j + k == 2020]
print(correct[0])
