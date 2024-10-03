# Checking whether a particular bit is on or off
# Bitwise AND (&) operator: To check if a particular bit is on or off, 
# you can use the & operator along with a mask. If the result is non-zero, the bit is on; otherwise, it's off.

# ex:To check if the 3rd bit (from the right) of num is on or off
num = 7  
bit_position = 2  # Checking the 3rd bit (0-based index)
is_on = (num & (1 << bit_position)) != 0
print(is_on)  # True if the bit is on, False if off

# Turning off a particular bit in a number:

# Bitwise AND (&) with NOT (~) operator: To turn off a particular bit, you use the & operator with a mask that has all bits set to 1 except the bit you want to turn off, which should be 0.
# To turn off the 3rd bit (from the right) of num
num = 15  # Example number in binary (10 in decimal)
bit_position = 2  # Turning off the 3rd bit
num = num & ~(1 << bit_position)
print(num)  # The bit should now be off

# Putting on a particular bit in a number:

# Bitwise OR (|) operator: To turn on a particular bit, you use the | operator with a mask that has only that bit set to 1.

# Example: To turn on the 3rd bit (from the right) of num:

num = 11  # Example number in binary (8 in decimal)
bit_position = 2  # Turning on the 3rd bit
num = num | (1 << bit_position)
print(num)  # The bit should now be on
