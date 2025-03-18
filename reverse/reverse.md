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

### Medium

#### GDB baby step {1,2,3,4}

- Use `gdb` commands

#### Picker

- Picker I
  - In the source code, the program process the user input in this way: `eval(user_input + '()')`
  - Ideally, we should input `getRandomNumber`, and the program will call this function `getRandomNumber()`
  - There's another function `win()` that prints out the flag: `0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x62 0x35 0x32 0x33 0x62 0x32 0x61 0x31 0x7d`
- Picker II
  - This time there is a filter:

    ```python
    def filter(user_input):
        if 'win' in user_input:
            return False
        return True
    ```

  - We cannot input `win`, instead, we use `globals()` to bypass this filter: `globals()['w' + 'in']`
- Picker III
  - We are only allowed to select from 4 functions in the `func_table`
  - Use `write_variable` to overwrite the value of `func_table`, making `win` the first function in this table, i.e., ensure the first 4 characters are `w`, `i`, `n`, and space

    ```shell
    $ nc saturn.picoctf.net 50765
    ==> 3
    Please enter variable name to write: func_table
    Please enter new value of variable: 'win t_table                     read_variable                   write_variable                  getRandomNumber                 '
    ==> 1
    # The content of the flag
    ```
  - Ensure the total length of the new `func_table` is `4 * 32`, otherwise, `check_table()` will fail
