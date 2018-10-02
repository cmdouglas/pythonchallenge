from collections import Counter

with open('data/02.txt') as f:
    s = f.read();
    ctr = Counter(s)
    print(''.join([c for c in s if ctr[c] < 10]))