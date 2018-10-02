import re
import requests

nothing = '12345'

pattern = r'the next nothing is ([\d]+)'

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

while True:
    response = requests.get(url+nothing)
    body = response.content.decode('utf-8')
    print(body)
    matches = re.findall(pattern, body)
    if matches:
        nothing = matches[0]
    elif body == "Yes. Divide by two and keep going.":
        nothing = str(int(nothing)/2)
    else:
        break
