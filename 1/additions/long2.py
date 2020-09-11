import re
import sys
print(sum([any([x == 'далек' for x in re.findall(r'\w\w\w\w\w', i.lower())])
           for i in sys.stdin.readlines()]))