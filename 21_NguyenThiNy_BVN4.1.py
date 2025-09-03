def caesar_cipher(text, k):
    result = ""
    for char in text:
        if char.isalpha():  
            shift = 65 if char.isupper() else 97  
            result += chr((ord(char) - shift + k) % 26 + shift)
        else:
            result += char  
    return result

if __name__ == "__main__":
    plaintext = "NguyenThiNy"
    k = 21
    ciphertext = caesar_cipher(plaintext, k)
    print("Plaintext :", plaintext)
    print("k =", k)
    print("Ciphertext:", ciphertext)
