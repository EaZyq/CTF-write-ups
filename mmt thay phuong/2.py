from pwn import *
import struct

r = remote('112.137.129.129', 27002)

payload = p32(0x0)
payload += p32(0x8)
mssv = b"20020122"
payload += mssv
r.send(payload)

r.recv(8)
while(1):
    a = r.recv()
    print(a)
    n = int(bytearray.fromhex(a[8:12].hex())[::-1].hex(), 16)
    m = int(bytearray.fromhex(a[12:16].hex())[::-1].hex(), 16)
    x = int(bytearray.fromhex(a[16:20].hex())[::-1].hex(), 16)
    p = 0
    print(hex(n))
    print(hex(m))
    print(hex(x))
    for i in range(0, n + 1):
        A = int(bytearray.fromhex(a[20+i*4:24+i*4].hex())[::-1].hex(), 16)
        p += A * (pow(x, i))
    result = p % m 
    print(hex(result))
    payload = p32(0x2)
    payload += p32(0x4)
    payload += p32(result)
    r.send(payload)




















