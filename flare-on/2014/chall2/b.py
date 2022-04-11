a = str("c97c49c49c68cz4Fc84c116cz68c97cz74cz44cz4Fcz54cz6Ac97cz76cz61cz35cz63cz72c97cz70cz41c84cz66cz6Cc97cz72cz65cz44c65cz53c72c111c110c68c79c84c99cz6Fcz6D")

a = a.split("c")[1:]
print(a)
result = ""
for i in a:
    if i[0] == "z":
        result += chr(int(i[1:], 16))
    else:
        result += chr(int(i))

print(result)
