a = "UMDCTF{BluSt0lXdrXg}"
s = "wh3nTheDr4gsHPis1048"
print(a[17])
print(a[14])
print(a)
flag = a[:14] + chr(51) + a[15:17] + s[9] + a[18:]
print(flag)










