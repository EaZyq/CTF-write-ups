a = "bngcg`debd"
b = ""
for i in a:
    b += chr(ord(i) ^ 0x56)
print(b)
