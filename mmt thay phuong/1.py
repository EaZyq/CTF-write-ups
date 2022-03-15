from pwn import *
import struct

r = remote('112.137.129.129', 27001)

payload = p32(0x0)
payload += p32(0x8)
mssv = b"20020122"
payload += mssv
r.send(payload)

r.recv(8)
while(1):
    x = r.recv()
    print(x)
    a = x[8:12].hex()
    b = x[12:16].hex()
    a = bytearray.fromhex(a)[::-1].hex()
    b = bytearray.fromhex(b)[::-1].hex()
    result = int(a, 16) + int(b, 16)
    payload = p32(0x2)
    payload += p32(0x4)
    payload += p32(result)
    r.send(payload)
    

