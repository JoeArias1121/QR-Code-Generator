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

postion_pattern = Image.new('1', (64, 64), 1)
position_y = Image.new('1', (56, 8), 0)
position_x = Image.new('1', (8, 40), 0)
innerbox = Image.new('1', (24, 24), 0)
postion_pattern.paste(position_y, (0, 0, 56, 8))
postion_pattern.paste(position_y, (0, 48, 56, 56))
postion_pattern.paste(position_x, (0, 8, 8, 48))
postion_pattern.paste(position_x, (48, 8, 56, 48))
postion_pattern.paste(innerbox, (16, 16, 40, 40))

'''
while rmax <= maxx and rpmax <= pmax:
    img.paste(bit, (rpmax, rpmax, rmax, rmax))
    rmax += 8
    rpmax += 8
'''

postion_pattern.show()
#img.show()