import re

with open('data/03.txt') as f:
    s = f.read()
    pattern = r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
    print(''.join(re.findall(pattern, s)))