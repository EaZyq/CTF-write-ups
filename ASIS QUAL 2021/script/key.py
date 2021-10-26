key2 = [0xbf,0x0b,0x0f,0xa2,0xa5,0x94,0x0e,0xd7,0xcb,0x85]
data = []
index = []

with open("stack1.txt") as file:
    for line in file:
        i = 32
        while (i > 17):
        	data.append(int(line[i : i + 2], 16))
        	i -= 2

for k in key2:
	indices = [i for i, x in enumerate(data) if x == k]
	index.append(hex(indices[0] ^ 0x77)[2:])

result = ''.join(index)
print(result)