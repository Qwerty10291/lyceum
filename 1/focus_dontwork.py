from PIL import Image
for l in range(1, 10):
    im = Image.open(f'image{l}.png')
    top, right, bottom, left = 10000, 0, 0, 10000
    pixels = im.load()
    mr, mg, mb = pixels[0, 0]
    x, y = im.size
    for i in range(x):
        for j in range(y):
            if pixels[i, j] != pixels[0, 0]:
                if left > i:
                    left = i
                if right < i:
                    right = i
                if top > j:
                    top = j
                if bottom < j:
                    bottom = j
