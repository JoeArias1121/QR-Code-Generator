'''
black squares are 1s and white squares are 0s
'''
n1 = 1
n2 = 3
char1 = 'W'
char2 = 'b'
print(ord(char1))
print(bin(ord(char1)))
print(bin(ord(char1))[2:].zfill(8))

url = 'https://www.google.com'

for c in url:
    print("Character: {cha}, binary form: {bin}".format(cha = c, bin = bin(ord(c))[2:].zfill(8)))

print(type(bin(ord(char1))[2:].zfill(8)))