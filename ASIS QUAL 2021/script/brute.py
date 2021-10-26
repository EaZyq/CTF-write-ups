flag = [0xcdec, 0x52e4, 0x533e, 0x3be1]
rand = [444242706, 339433174, 1053149467, 1523027287, 1117968178,
        2092997650, 816324422, 1095556438, 747709558, 301071833,
        598496766, 1810696988, 953767466, 1765134604, 2028312134,
        1171168959, 1961149144, 425175821, 1299180724, 1105033260,
        282672453, 169003868, 412382634, 162192383, 492960224, 560096927, 
        1172437624, 128594585, 441632769, 1993060813, 966622640, 885875475]

table = []

with open("stack2.txt") as file2:
    for line in file2:
        i = 32
        while (i > 17):
            table.append(int(line[i : i + 2], 16))
            i -= 2


def a (var1, var2):
    global count
    iVar2 = rand[count] % 0x10000
    flag[var1] = (flag[var2] ^ iVar2) ^ flag[var1]
    count -= 1

def b (pos, var2, var3, var4, var5):
    i = 0x0000
    while (i <= 0xffff):
        if (i ^ (table[(i >> 8) + 0x110 * var2]) == flag[pos]):
            flag[pos] = i
            break;
        else:
            i += 1
    i = 0x0000
    while (i <= 0xffff):
        if ((table[(i % 0x100) + 0x110 * var3] << 8) ^ i == flag[pos]):
            flag[pos] = i
            break;
        else:
            i += 1
    i = 0x0000
    while (i <= 0xffff):
        if (i ^ (table[(i >> 8) + 0x110 * var4]) == flag[pos]):
            flag[pos] = i
            break;
        else:
            i += 1
    i = 0x0000
    while (i <= 0xffff):
        if ((table[(i % 0x100) + 0x110 * var5] << 8) ^ i == flag[pos]):
            flag[pos] = i
            break;
        else:
            i += 1


count = 31
b(0,4,5,6,7)
a(1,0)
b(1,0,1,2,3)
a(2,1)
b(2,6,7,8,9)
a(3,2)
b(3,2,3,4,5)
a(0,3)
b(0,8,9,0,1)
a(1,0)
b(1,4,5,6,7)
a(2,1)
b(2,0,1,2,3)
a(3,2)
b(3,6,7,8,9)
a(0,3)
a(3,0)
b(0,2,3,4,5)
a(0,1)
b(1,8,9,0,1)
a(1,2)
b(2,4,5,6,7)
a(2,3)
b(3,0,1,2,3)
a(3,0)
b(0,6,7,8,9)
a(0,1)
b(1,2,3,4,5)
a(1,2)
b(2,8,9,0,1)
a(2,3)
b(3,4,5,6,7)
b(0,0,1,2,3)
a(1,0)
b(1,6,7,8,9)
a(2,1)
b(2,2,3,4,5)
a(3,2)
b(3,8,9,0,1)
a(0,3)
b(0,4,5,6,7)
a(1,0)
b(1,0,1,2,3)
a(2,1)
b(2,6,7,8,9)
a(3,2)
b(3,2,3,4,5)
a(0,3)
a(3,0)
b(0,8,9,0,1)
a(0,1)
b(1,4,5,6,7)
a(1,2)
b(2,0,1,2,3)
a(2,3)
b(3,6,7,8,9)
a(3,0)
b(0,2,3,4,5)
a(0,1)
b(1,8,9,0,1)
a(1,2)
b(2,4,5,6,7)
a(2,3)
b(3,0,1,2,3)

result = []
for i in flag:
    result.append(chr(i >> 8))
    result.append(chr(i % 0x100))

print(''.join(result))
