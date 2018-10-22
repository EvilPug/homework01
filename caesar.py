def encrypt_caesar(plaintext, shift):
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON", 3)
    'SBWKRQ'
    >>> encrypt_caesar("python", 3)
    'sbwkrq'
    >>> encrypt_caesar("Python3.6", 3)
    'Sbwkrq3.6'
    >>> encrypt_caesar("", 3)
    ''
    """
    ciphertext = ''
    for i in plaintext:
        numb = ord(i) + shift
        if 'a' <= i <= 'z':
            newnumb = 97 + (numb - 97) % 26
        elif 'A' <= i <= 'Z':
            newnumb = 65 + (numb - 65) % 26
        else:
            newnumb = ord(i)
        ciphertext += chr(newnumb)
    return ciphertext


def decrypt_caesar(ciphertext, shift):
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ", 3)
    'PYTHON'
    >>> decrypt_caesar("sbwkrq", 3)
    'python'
    >>> decrypt_caesar("Sbwkrq3.6", 3)
    'Python3.6'
    >>> decrypt_caesar("", 3)
    ''
    """
    plaintext = ''
    for i in ciphertext:
        numb = ord(i) - shift
        if 'a' <= i <= 'z':
            newnumb = 97 + (numb - 97) % 26
        elif 'A' <= i <= 'Z':
            newnumb = 65 + (numb - 65) % 26
        else:
            newnumb = ord(i)
        plaintext += chr(newnumb)
    return plaintext
