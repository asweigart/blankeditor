from PIL import Image

im = Image.open('c:\\temp\\oxygen.png')

x = 0
while True:
    r, g, b, a = im.getpixel((x, 45))

    if not (r == g == b):
        break

    print(chr(r), end='')

    x += 7