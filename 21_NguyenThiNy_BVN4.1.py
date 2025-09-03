def caesar_cipher(text, k):
    ketqua = ""
    for ch in text:
        if ch.isalpha():
            # dùng 'A' nếu là chữ hoa, 'a' nếu là chữ thường
            base = 'A' if ch.isupper() else 'a'
            # dịch chuyển ký tự
            vitri = (ord(ch) - ord(base) + k) % 26
            ketqua += chr(ord(base) + vitri)
        else:
            ketqua += ch
    return ketqua

# chương trình chính
plaintext = "NguyenThiNy"
k = 21
ciphertext = caesar_cipher(plaintext, k)

print("Plaintext :", plaintext)
print("k =", k)
print("Ciphertext:", ciphertext)
