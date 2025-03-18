import os

def door_1():
    passwd = []
    for i in range(32):
        passwd.append('')
    passwd[0] = 'd'
    passwd[29] = '9'
    passwd[4] = 'r'
    passwd[2] = '5'
    passwd[23] = 'r'
    passwd[3] = 'c'
    passwd[17] = '4'
    passwd[1] = '3'
    passwd[7] = 'b'
    passwd[10] = '_'
    passwd[5] = '4'
    passwd[9] = '3'
    passwd[11] = 't'
    passwd[15] = 'c'
    passwd[8] = 'l'
    passwd[12] = 'H'
    passwd[20] = 'c'
    passwd[14] = '_'
    passwd[6] = 'm'
    passwd[24] = '5'
    passwd[18] = 'r'
    passwd[13] = '3'
    passwd[19] = '4'
    passwd[21] = 'T'
    passwd[16] = 'H'
    passwd[27] = '5'
    passwd[30] = '2'
    passwd[25] = '_'
    passwd[22] = '3'
    passwd[28] = '0'
    passwd[26] = '7'
    passwd[31] = 'e'
    
    flag1 = ''.join(passwd)

    print(flag1)


def door_3():
    res = list('jU5t_a_sna_3lpm12g94c_u_4_m7ra41')
    passwd = []
    for i in range(32):
        passwd.append('')
    for i in range(0, 8):
        passwd[i] = res[i]
    for i in range(8, 16):
        passwd[i] = res[23 - i]
    for i in range(16, 32, 2):
        passwd[i] = res[46 - i]
    for i in range(17, 32, 2):
        passwd[i] = res[i]

    print(''.join(passwd))

def door_4():
    their_bytes = [
        106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
        0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
        0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o70 , 0o146
    ]
    passwd = []
    for b in their_bytes:
        passwd.append(chr(b))
    print(''.join(passwd) + ''.join(['4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b']))

door_1()
door_3()
door_4()