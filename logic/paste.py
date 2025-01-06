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
img.paste(alignment_pattern, (3 * scale, 19 * scale, 8 * scale, 24 * scale))
img.paste(alignment_pattern, (19 * scale, 3 * scale, 24 * scale, 8 * scale))
img.paste(alignment_pattern, (19 * scale, 19 * scale, 24 * scale, 24 * scale))
img.paste(alignment_pattern, (19 * scale, 35 * scale, 24 * scale, 40 * scale))
img.paste(alignment_pattern, (35 * scale, 19 * scale, 40 * scale, 24 * scale))
img.paste(alignment_pattern, (35 * scale, 35 * scale, 40 * scale, 40 * scale))
# alignment patterns placed

# adding finder and alignment patterns to occupied list
occupied = set()
alignment_patterns = [(3 * scale, 19 * scale), (19 * scale, 3 * scale), (19 * scale, 19 * scale), (19 * scale, 35 * scale), (35 * scale, 19 * scale), (35 * scale, 35 * scale)]
finder_patterns = [(0 * scale, 0 * scale), (0 * scale, size - 7 * scale), (size - 7 * scale, 0 * scale)]
# adding finder patterns to occupied list
for pat in finder_patterns:
    for i in range(pat[0], pat[0] + 7 * scale):
        for j in range(pat[1], pat[1] + 7 * scale):
            occupied.add((i, j))
# finder patterns in occupied list

# adding alignment patterns to occupied list
for pat in alignment_patterns:
    for i in range(pat[0], pat[0] + 5 * scale):
        for j in range(pat[1], pat[1] + 5 * scale):
            occupied.add((i, j))
# alignment patterns in occupied list
    

# timing patterns

'''
while rmax <= maxx and rpmax <= pmax:
    img.paste(bit, (rpmax, rpmax, rmax, rmax))
    rmax += 8
    rpmax += 8
'''

#finder_pattern.show()
#alignment_pattern.show()
img.show()
