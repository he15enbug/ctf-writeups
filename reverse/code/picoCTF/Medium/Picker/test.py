
def fx():
    print(1)

def test_eval():
    eval('globals()[\'f\' + \'x\']' + '()')

test_eval()