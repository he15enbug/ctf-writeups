import os

def dec():
    flag = ''
    mod = (1 << 8)
    with open('./enc', 'r', encoding="utf-8") as f:
        char_read = f.read()
        for ch in char_read:
            sum = ord(ch)
            b2 = (sum % mod)
            b1 = ((sum - b2) >> 8)
            flag = flag + chr(b1) + chr(b2)
    return flag

print(dec())
