a = [input().split() for i in range(int(input()))]
chet = {'I': 0, 'II': 0, 'III': 0, 'IV': 0}
output = ''
for i in a:
    if '0' in i:
        print(f'({i[0]}, {i[1]})')
        continue
    if int(i[0]) > 0 and int(i[1]) > 0:
        chet['I'] += 1
    elif int(i[0]) < 0 and int(i[1]) > 0:
        chet['II'] += 1
    elif int(i[0]) < 0 and int(i[1]) < 0:
        chet['III'] += 1
    elif int(i[0]) > 0 and int(i[1]) < 0:
        chet['IV'] += 1

for i, num in chet.items():
    output += f'{i}: {num}, '

print(output[:-2] + '.')
