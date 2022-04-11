with open("flare-on.png", "rb") as f:
    f.seek(0x19c4)
    a = f.read()
    with open("out.php", "wb") as w:
        w.write(bytearray(a))
