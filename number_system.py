
'''Converting a decimal number to all other number systems'''
decimal=25
print(bin(decimal))
print(oct(decimal))
print(hex(decimal))

'''Converting a binary number to all other number systems'''
binary='0b1111'
print(int(binary,2))
decimal=int(binary,2)
print(oct(decimal))
print(hex(decimal))

'''Converting a octal number to all other number systems'''
octal='0o32'
dec=int(octal,8)
print(dec)
print(bin(dec))
print(hex(dec))

'''Converting a hexadecimal number to all other number systems'''
hexadecimal='0x22'
dec=int(hexadecimal,16)
print(dec)
print(bin(dec))
print(oct(dec))

