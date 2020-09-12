import sys
output = []


def count(text: str):
    output = {}
    for i in text:
        if i not in output:
            output[i] = 1
        else:
            output[i] += 1
    return output


def check(dict1: dict, dict2: dict):
    for i in dict2.keys():
        if i not in dict1:
            return False
    for i in dict2.keys():
        if dict2[i] > dict1[i]:
            return False
    return True


main = count(input().lower())
for i in sys.stdin.readlines():
    data = i.lower().replace('\n', '')
    if check(main, count(data)):
        output.append(i)

print(len(output))
[print(i) for i in output]
