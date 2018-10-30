from PIL import Image, ImageDraw

image = Image.open('data/cave.jpg')
draw = ImageDraw.Draw(image)

xsize, ysize = image.size

points = [
    (x, y) for x in range(xsize) for y in range(ysize)
    if ((x % 2 == 0 and y % 2 == 1) or (x % 2 == 1 and y % 2 == 0))
]

#print(points[:20])

draw.point(points, 'white')
image.show()
        