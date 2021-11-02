a = 'rwhxi}eomr\\^`Y'
z = 'f]XdThbQd^TYL&\x13g'

a = a + z

result = []

for i,b in enumerate(a):
	c = ord(b)
	c -= 7
	c += i
	result.append(chr(c))

print(''.join(result))