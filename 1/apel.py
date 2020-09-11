import sys
main = set(input())
output = []
for line in sys.stdin.readlines():
    if set(line.replace('\n', '')).issubset(main):
        output.append(line.replace('\n', ''))
print(len(output))
for i in output:
    print(i)
