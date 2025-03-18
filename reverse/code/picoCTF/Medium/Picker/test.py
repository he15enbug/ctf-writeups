
def fx():
    print(1)

def test_eval():
    eval('globals()[\'f\' + \'x\']' + '()')

test_eval()

func_table = \
'''\
print_table                     \
read_variable                   \
write_variable                  \
getRandomNumber                 \
'''

def test_write_variable():
    var_name = input('Please enter variable name to write: ')
    value = input('Please enter new value of variable: ')
    exec('global '+var_name+'; '+var_name+' = '+value)

    print(func_table)

test_write_variable()
