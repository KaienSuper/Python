def encrypt_caesar(msg, shift=None):
    result = ""
    for w in msg:
        if shift == None:
            result += chr(ord(w)+3)
        else:
            result += chr(ord(w) + shift)
    return result
def decrypt_caesar(msg, shift=None):
    result = ""
    for w in msg:
        if shift == None:
            result += chr(ord(w) - 3)
        else:
            result += chr(ord(w) - shift)
    return result
msg = "Да здравствует салат Цезарь!"
msg = encrypt_caesar(msg)
print(msg)
msg = decrypt_caesar(msg)
print(msg)