import math
fb = math.fabs
dotes = [[int(l) for l in input().split()] for i in range(int(input()))]
tdotes = []

for i in dotes:
    if fb(i[0]) > fb(i[1]):
        tdotes.append(i)
top, left, right, bottom = -1000000, 100000000, -10000000, 10000000
for i in dotes:
    if i[1] > top:
        dt = i
        top = i[1]
    if i[0] < left:
        dl = i
        left = i[0]
    if i[0] > right:
        dr = i
        right = i[0]
    if i[1] < bottom:
        db = i
        bottom = i[1]
for i in tdotes:
    print(f'({i[0]}, {i[1]})')
print(f'left: ({dl[0]}, {dl[1]})\nright: ({dr[0]}, {dr[1]})\ntop: ({dt[0]}, {dt[1]})\n' +
      f'bottom: ({db[0]}, {db[1]})')
