from PIL import Image

image = Image.open('data/oxygen.png')
y = 50
x = 0
step = 7

r = g = b = a = 0;
message = []

while (r == g and g == b):
    r, g, b, a = image.getpixel((x, y))
    message.append(chr(r))
    x += step

print(''.join(message))
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]s

print(''.join(chr(code) for code in [105, 110, 116, 101, 103, 114, 105, 116, 121]) )