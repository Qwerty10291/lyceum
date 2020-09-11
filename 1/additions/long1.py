import sys
print(sum([sum([int(l[0:4] == 'далек') for l in i.lower().split()]) for i in sys.stdin.readlines()]))
