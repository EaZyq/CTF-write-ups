str1 = "9xLmMiI2znmPam'D_A_1:RQ;Il"
str2 = '\*7:%i".R<'
str1 += str2
i = 31
pos = 0
result = []

while (i < 112 and pos <= 35):
	j = 32
	if (i == 111):
		i = 31
		pos += 2
	else:
		i += 1
	while (j < 111 and pos <= 35):
		temp1 = chr((2 * i - j + 153) % 93 + 33)
		temp2 = chr((j - i + 93) % 93 + 33)
		if (temp1 == str1[pos] and temp2 == str1[pos + 1]):
			check1 = 158 - i
			check2 = 158 - j
			if (47<check1<128 and 47<check2<128):
				result.append(chr(check1))
				result.append(chr(check2))
		j += 1

print(''.join(result) + "}")

