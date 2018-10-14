def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for i in plaintext:
        numb = ord(i) + 3
        if ((ord(i) >= 97) and (ord(i) <= 122)):
            newnumb = 97 + (numb - 97) % 26
        elif ((ord(i) >= 65) and (ord(i) <= 90)):
            newnumb = 65 + (numb - 65) % 26
        else:
            newnumb = ord(i)
        ciphertext += chr(newnumb)
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for i in ciphertext:
        numb = ord(i) - 3
        if ((ord(i) >= 97) and (ord(i) <= 122)):
            newnumb = 97 + (numb - 97) % 26
        elif ((ord(i) >= 65) and (ord(i) <= 90)):
            newnumb = 65 + (numb - 65) % 26
        else:
            newnumb = ord(i)
        plaintext += chr(newnumb)
    return plaintext
