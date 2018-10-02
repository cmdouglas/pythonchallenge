def say_what_you_see(s):
    last = s[0]
    count = 0
    r = []
    for c in s:
        if c == last:
            count += 1
        else:
            r.append(str(count))
            r.append(last)
            last = c
            count = 1
    r.append(str(count))
    r.append(last)
    
    return ''.join(r)
    
message = '1'

for i in range(30):
    message = say_what_you_see(message)
    
print(len(message))
