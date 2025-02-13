# Praktek GerbanG Digital
print(" =================== ")
a = 0b1100  # 12 dalam desimal
b = 0b1010  # 10 dalam desimal

print(bin(a & b))  # AND: 0b1000 -> Output: 0b1000
print(bin(a | b))  # OR:  0b1110 -> Output: 0b1110
print(bin(a ^ b))  # XOR: 0b0110 -> Output: 0b110
print(bin(~a))     # NOT: -0b1101 -> Output: -0b1101
print(bin(a << 2)) # Shift Kiri: 0b110000 -> Output: 0b110000
print(bin(a >> 2)) # Shift Kanan: 0b11 -> Output: 0b11
