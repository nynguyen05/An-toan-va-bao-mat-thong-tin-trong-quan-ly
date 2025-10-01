# RSA Mã hóa/Giải mã - Ngắn gọn

p, q, e = 17, 23, 5
n = p * q
phi = (p-1)*(q-1)

# Hàm tìm khóa bí mật d
def modinv(a, m):
    x0, x1 = 0, 1
    m0 = m
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q*x0, x0
    return x1 + m0 if x1 < 0 else x1

d = modinv(e, phi)
message = "NguyenThiNy"

# Mã hóa thông điệp
cipher = [pow(ord(c), e, n) for c in message]

# Giải mã thông điệp
decrypted = ''.join([chr(pow(c, d, n)) for c in cipher])

# In kết quả
print("Khóa bí mật d:", d)
print("Thông điệp sau mã hóa:", cipher)
print("Thông điệp sau giải mã:", decrypted)