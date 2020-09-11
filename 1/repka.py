data = input().split(' -> ')
inputs = [input() for i in range(int(input()))]
for i in inputs:
    index = data.index(i)
    if index == 0:
        print(f'{data[index]} -> {data[index + 1]}')
        continue
    if index == len(data) - 1:
        print(f'{data[index - 1]} -> {data[index]}')
        continue
    print(f'{data[index - 1]} -> {data[index]} -> {data[index + 1]}')