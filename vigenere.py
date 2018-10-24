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
    alphabet_low = 'abcdefghigklmnopqrstuvwxyz'
    alphabet_high = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
    ciphertext = ''

    if plaintext != '':
        n = 0
        if len(plaintext) != len(keyword):
            for i in range(len(plaintext) - len(keyword)):
                keyword += keyword[n]
                n += 1
        n = 0
        keylist = list(keyword)
        for i in keyword:
            if plaintext[n].islower() is False:
                if keylist[n].islower() is True:
                    keylist[n] = keylist[n].upper()
            elif plaintext[n].islower() is True:
                if keylist[n].islower() is False:
                    keylist[n] = keylist[n].lower()
            n += 1
        keyword = ''.join(keylist)

        n = 0
        for abc in plaintext:
            if 'a' <= abc <= 'z':
                if 'a' <= keyword[n] <= 'z':
                    lowshift = alphabet_low.index(keyword[n])
                else:
                    highshift = alphabet_high.index(keyword[n])
                newnumb = 97 + (ord(abc) + lowshift - 97) % 26
                ciphertext += chr(newnumb)
                n += 1
            elif 'A' <= abc <= 'Z' and 'A' <= keyword[n] <= 'Z':
                if 'a' <= keyword[n] <= 'z':
                    lowshift = alphabet_low.index(keyword[n])
                else:
                    highshift = alphabet_high.index(keyword[n])
                newnumb = 65 + (ord(abc) + highshift - 65) % 26
                ciphertext += chr(newnumb)
                n += 1
            else:
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
    alphabet_low = 'abcdefghigklmnopqrstuvwxyz'
    alphabet_high = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
    plaintext = ''

    if ciphertext != '':
        n = 0
        if len(ciphertext) != len(keyword):
            for i in range(len(ciphertext) - len(keyword)):
                keyword += keyword[n]
                n += 1
        n = 0
        keylist = list(keyword)
        for i in keyword:
            if ciphertext[n].islower() is False:
                if keylist[n].islower() is True:
                    keylist[n] = keylist[n].upper()
            elif ciphertext[n].islower() is True:
                if keylist[n].islower() is False:
                    keylist[n] = keylist[n].lower()
            n += 1
        keyword = ''.join(keylist)

        n = 0
        for abc in ciphertext:
            if 'a' <= abc <= 'z':
                if 'a' <= keyword[n] <= 'z':
                    lowshift = alphabet_low.index(keyword[n])
                else:
                    highshift = alphabet_high.index(keyword[n])
                newnumb = 97 + (ord(abc) - lowshift - 97) % 26
                plaintext += chr(newnumb)
                n += 1
            elif 'A' <= abc <= 'Z' and 'A' <= keyword[n] <= 'Z':
                if 'a' <= keyword[n] <= 'z':
                    lowshift = alphabet_low.index(keyword[n])
                else:
                    highshift = alphabet_high.index(keyword[n])
                newnumb = 65 + (ord(abc) - highshift - 65) % 26
                plaintext += chr(newnumb)
                n += 1
            else:
                newnumb = ord(abc)
    return plaintext
