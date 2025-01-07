from PIL import Image

scale = 8
size = 45 * scale


img = Image.new('1', (size, size), 1)

bit = Image.new('1', (scale, scale), 0)
"""
reqion = bit.crop((0, 0, 8, 8))

img.paste(bit, (0, 0, 8, 8))
"""
maxx = size
pmax = size - scale
rmax = scale
rpmax = 0
# positions of finder patterns 
finder_pattern = Image.new('1', (7 * scale, 7 * scale), 1)
position_y = Image.new('1', (7 * scale, 1 * scale), 0)
position_x = Image.new('1', (1 * scale, 5 * scale), 0)
innerbox = Image.new('1', (3 * scale, 3 * scale), 0)
finder_pattern.paste(position_y, (0 * scale, 0 * scale, 7 * scale, 1 * scale))
finder_pattern.paste(position_y, (0 * scale, 6 * scale, 7 * scale, 7 * scale))
finder_pattern.paste(position_x, (0 * scale, 1 * scale, 1 * scale, 6 * scale))
finder_pattern.paste(position_x, (6 * scale, 1 * scale, 7 * scale, 6 * scale))
finder_pattern.paste(innerbox, (2 * scale, 2 * scale, 5 * scale, 5 * scale))
# pasting finder patterns onto image
img.paste(finder_pattern, (0 * scale, 0 * scale, 7 * scale, 7 * scale))
img.paste(finder_pattern, (0 * scale, size - 7 * scale, 7 * scale, size))
img.paste(finder_pattern, (size - 7 * scale, 0 * scale, size, 7 * scale))
# finder patterns placed

# alignment patterns
alignment_pattern = Image.new('1', (5 * scale, 5 * scale), 0)
position_y = Image.new('1', (3 * scale, 1 * scale), 1)
position_x = Image.new('1', (1 * scale, 1 * scale), 1)
alignment_pattern.paste(position_y, (1 * scale, 1 * scale, 4 * scale, 2 * scale))
alignment_pattern.paste(position_y, (1 * scale, 3 * scale, 4 * scale, 4 * scale))
alignment_pattern.paste(position_x, (1 * scale, 2 * scale, 2 * scale, 3 * scale))
alignment_pattern.paste(position_x, (3 * scale, 2 * scale, 4 * scale, 3 * scale))
# pasting alignment patterns onto image
img.paste(alignment_pattern, (4 * scale, 20 * scale, 9 * scale, 25 * scale))
img.paste(alignment_pattern, (20 * scale, 4 * scale, 25 * scale, 9 * scale))
img.paste(alignment_pattern, (20 * scale, 20 * scale, 25 * scale, 25 * scale))
img.paste(alignment_pattern, (20 * scale, 36 * scale, 25 * scale, 41 * scale))
img.paste(alignment_pattern, (36 * scale, 20 * scale, 41 * scale, 25 * scale))
img.paste(alignment_pattern, (36 * scale, 36 * scale, 41 * scale, 41 * scale))
# alignment patterns placed

# adding finder and alignment patterns to occupied list
occupied = set()
alignment_patterns = [(4 * scale, 20 * scale), (20 * scale, 4 * scale), (20 * scale, 20 * scale), (20 * scale, 36 * scale), (36 * scale, 20 * scale), (36 * scale, 36 * scale)]
finder_patterns = [(0 * scale, 0 * scale), (0 * scale, size - 7 * scale), (size - 7 * scale, 0 * scale)]
# adding finder patterns to occupied list
for pat in finder_patterns:
    for i in range(pat[0], pat[0] + 7 * scale, scale):
        for j in range(pat[1], pat[1] + 7 * scale, scale):
            occupied.add((i, j))
# finder patterns in occupied list
# adding alignment patterns to occupied list
for pat in alignment_patterns:
    for i in range(pat[0], pat[0] + 5 * scale, scale):
        for j in range(pat[1], pat[1] + 5 * scale, scale):
            occupied.add((i, j))
# alignment patterns in occupied list

# adding separators to occupied list
#test = Image.new('1', (1 * scale, 1 * scale), 0) || test image
# adding horizontal separators to occupied list
horizontal_separators = [(0 * scale, 7 * scale), (size - 8 * scale, 7 * scale), (0 * scale, size - 8 * scale)]
for sep in horizontal_separators:
    for i in range(8):
        i *= scale
        occupied.add((sep[0] + i, sep[1]))
        #img.paste(test, ((sep[0] + i, sep[1], sep[0] + i + 1 * scale, sep[1] + 1 * scale))) || tests separators
# horizontal separators in occupied list
# adding vertical separators to occupied list
vertical_separators = [(7 * scale, 0 * scale), (7 * scale, size - 8 * scale), (size - 8 * scale, 0 * scale)]
for sep in vertical_separators:
    for i in range(8):
        i *= scale
        occupied.add((sep[0], sep[1] + i))
        #img.paste(test, ((sep[0], sep[1] + i, sep[0] + 1 * scale, sep[1] + i + 1 * scale))) || tests separators
    
black = Image.new('1', (1 * scale, 1 * scale), 0)
white = Image.new('1', (1 * scale, 1 * scale), 1)
toggle = True
# timing patterns
# vertical timing pattern
for i in range(8 * scale, size, scale):
    if (6 * scale, i) in occupied:
        toggle = False
        continue
    if toggle:
        img.paste(black, (6 * scale, i, 7 * scale, i + 1 * scale))
        toggle = False
    else:
        img.paste(white, (6 * scale, i, 7 * scale, i + 1 * scale))
        toggle = True
# horizontal timing pattern
toggle = True     
for i in range(8 * scale, size, scale):
    if (i, 6 * scale) in occupied:
        toggle = False
        continue
    if toggle:
        img.paste(black, (i, 6 * scale, i + 1 * scale, 7 * scale))
        toggle = False
    else:
        img.paste(white, (i, 6 * scale, i + 1 * scale, 7 * scale))
        toggle = True
# timing patterns placed

# adding dark spot
occupied.add((8 * scale, size - 8 * scale))
img.paste(black, (8 * scale, size - 8 * scale, 9 * scale, size - 7 * scale))
# dark spot placed

# adding data storage (most important part)
url = list('https://www.google.com') # placeholder link for development (meant to be dynamic with user input)
data_format = list('0100')
data_size = list(bin(len(url))[2:].zfill(8))
x = size - scale
y = size - scale

# adding data format
while data_format:
    c1 = data_format.pop(0)
    c2 = data_format.pop(0)
    left = (x - scale, y, x, y + scale)
    right = (x, y, x + scale, y + scale)
    # right
    if c1 == '1':
        img.paste(black, right)#(x, y, x + scale, y + scale))
    elif c1 == '0':
        img.paste(white, right)#(x, y, x + scale, y + scale))
    # left
    if c2 == '1':
        img.paste(black, left)#(x - scale, y, x, y + scale))
    elif c2 == '0':
        img.paste(white, left)#(x - scale, y, x, y + scale))
        
    y -= scale
# data format placed
# adding data size
while data_size:
    c1 = data_size.pop(0)
    c2 = data_size.pop(0)
    left = (x - scale, y, x, y + scale)
    right = (x, y, x + scale, y + scale)
    # right
    if c1 == '1':
        img.paste(black, right)#(x, y, x + scale, y + scale))
    elif c1 == '0':
        img.paste(white, right)#(x, y, x + scale, y + scale))
    # left
    if c2 == '1':
        img.paste(black, left)#(x - scale, y, x, y + scale))
    elif c2 == '0':
        img.paste(white, left)#(x - scale, y, x, y + scale))
        
    y -= scale
# data size placed
'''
for c in url:
    cha = bin(ord(c))[2:].zfill(8)
    while x >= 0:
        left = (x - scale, y)
        right = (x, y)
        if left not in occupied and right not in occupied:
            bin_char = cha.pop(0)
            if bin_char == '1':
                img.paste(black, (x - scale, y, x, y + scale))
            elif bin_char == '0':
                img.paste(white, (x - scale, y, x, y + scale))
'''
# adding format strips


'''
while rmax <= maxx and rpmax <= pmax:
    img.paste(bit, (rpmax, rpmax, rmax, rmax))
    rmax += 8
    rpmax += 8
'''

#finder_pattern.show()
#alignment_pattern.show()
img.show()
