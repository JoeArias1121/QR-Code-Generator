from PIL import Image

img = Image.new('1', (360, 360), 1)

bit = Image.new('1', (8, 8), 0)
"""
reqion = bit.crop((0, 0, 8, 8))

img.paste(bit, (0, 0, 8, 8))
"""
maxx = 360
pmax = 352
rmax = 8
rpmax = 0


while rmax <= maxx and rpmax <= pmax:
    img.paste(bit, (rpmax, rpmax, rmax, rmax))
    rmax += 8
    rpmax += 8



img.show()