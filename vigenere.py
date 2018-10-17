def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    alphabet_low = list('abcdefghigklmnopqrstuvwxyz')
    alphabet_high = list('ABCDEFGHIGKLMNOPQRSTUVWXYZ')
    plainlist = list(plaintext)
    keylist = list(keyword)
    ciphertext = ''

    if plaintext != '':
        n = 0
        if len(plaintext) != len(keyword):
            for i in range(len(plaintext) - len(keyword)):
                keylist += keylist[n]
                n = n + 1
        first = (ord(plainlist[0]))
        if ((first >= 97) and (first <= 122)):
            n = 0
            for abc in plaintext:
                newnumb = 97 + (ord(abc) + alphabet_low.index(keylist[n]) - 97) % 26
                ciphertext += chr(newnumb)
                n = n + 1
        elif ((first >= 65) and (first <= 90)):
            n = 0
            for abc in plaintext:
                newnumb = 65 + (ord(abc) + alphabet_high.index(keylist[n]) - 65) % 26
                ciphertext += chr(newnumb)
                n = n + 1
        else:
            for abc in plaintext:
                newnumb = ord(abc)
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    alphabet_low = list('abcdefghigklmnopqrstuvwxyz')
    alphabet_high = list('ABCDEFGHIGKLMNOPQRSTUVWXYZ')
    cipherlist = list(ciphertext)
    keylist = list(keyword)
    plaintext = ''

    if ciphertext != '':
        n = 0
        if len(ciphertext) != len(keyword):
            for i in range(len(ciphertext) - len(keyword)):
                keylist += keylist[n]
                n = n + 1
        first = (ord(cipherlist[0]))
        if ((first >= 97) and (first <= 122)):
            n = 0
            for abc in ciphertext:
                newnumb = 97 + (ord(abc) - alphabet_low.index(keylist[n]) - 97) % 26
                plaintext += chr(newnumb)
                n = n + 1
        elif ((first >= 65) and (first <= 90)):
            n = 0
            for abc in ciphertext:
                newnumb = 65 + (ord(abc) - alphabet_high.index(keylist[n]) - 65) % 26
                plaintext += chr(newnumb)
                n = n + 1
        else:
            for abc in plaintext:
                newnumb = ord(abc)

    return plaintext
