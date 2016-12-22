#alpha = "abcdefghijklmnopqrstuvwxyz.,! '"

### Function 3 ###

def makeKey(alphabet):
    import random
    keylist = []
    str_form = ""
    for x in alphabet:
        keylist.append(x)
    datshuffle = random.shuffle(keylist)
    for i in keylist:
        str_form = str_form + i
    return str_form

### Function 1 ###

def encryptMsg (plaintext,key,alphabet):
    plaintext = plaintext.lower()
    empty_str = ""
    cipher_list = []
    cipher_str = ""
    for i in plaintext:
        if i in alpha:
            empty_str += i
    for letter in empty_str:
        indicies = alpha.find(letter)
        cipher_list.append(key[indicies])

    for value in cipher_list:
        cipher_str += value
    return cipher_str

### Function 2 ###

def decryptMsg(ciphertext,key,alphabet):
    empty_str2 = ""
    coded_list = []
    coded_str = ""
    for index in ciphertext:
        indicies2 = key.find(index)
        coded_list.append(alpha[indicies2])
    for value in coded_list:
        coded_str += value
    return coded_str
