# CTF - Reverse Engineering

## picoCTF

### Easy

#### Transformation

- The flag is "encrypted" in this way: `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`, it combined each 2 one-byte characters in the flag, and get a two-byte character
- The result is stored in a file `enc`

    ```python
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
    ```

#### vault-door-training

- The flag is in the source code: `picoCTF{w4rm1ng_Up_w1tH_jAv4_be8d9806f18}`
