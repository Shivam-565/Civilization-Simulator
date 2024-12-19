alpha = "abcdefghijklmnopqrstuvwxyz"

def enc(text, key):
    if key <= 20 and key > 0:
        cipher = ""
        for i in text:
            if i in alpha:
                if alpha.index(i) + key <= 26:
                    cipher += alpha[alpha.index(i) + key]
                else:
                    cipher += alpha[(alpha.index(i) + key) % 26]
            else:
                cipher += i
                
        return cipher
    else:
        print("Key should be within range 0-20")

def dec(cipher, key):
    if key <= 20 and key > 0:
        plaintext = ""

        for i in cipher:
            if i in alpha:
                if alpha.index(i) - key >= 0:
                    plaintext += alpha[alpha.index(i) - key]
                else:
                    plaintext += alpha[(alpha.index(i) - key) % 26]
            else:
                plaintext += i

        return plaintext
    else:
        print("Key should be within range 0-20")
