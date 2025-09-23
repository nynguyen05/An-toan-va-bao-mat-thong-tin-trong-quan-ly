# Mã hóa thay thế bằng phép cộng trong Z26

def caesar_encrypt(text, k):
    result = ""
    for ch in text:
        if ch.isupper():
            p = ord(ch) - ord('A')
            c = (p + k) % 26
            result += chr(c + ord('A'))
        elif ch.islower():
            p = ord(ch) - ord('a')
            c = (p + k) % 26
            result += chr(c + ord('a'))
        else: 
            result += ch
    return result


plaintext = "NguyenThiNy"
k = 21

ciphertext = caesar_encrypt(plaintext, k)
print("Plaintext :", plaintext)
print("k =", k)
print("Ciphertext:", ciphertext)

