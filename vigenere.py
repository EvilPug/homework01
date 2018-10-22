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
                n = n + 1

        ch = plaintext[0]
        if 'a' <= ch <= 'z':
            n = 0
            for abc in plaintext:
                lowshift = alphabet_low.index(keyword[n])
                newnumb = 97 + (ord(abc) + lowshift - 97) % 26
                ciphertext += chr(newnumb)
                n = n + 1
        elif 'A' <= ch <= 'Z':
            n = 0
            for abc in plaintext:
                highshift = alphabet_high.index(keyword[n])
                newnumb = 65 + (ord(abc) + highshift - 65) % 26
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
    alphabet_low = 'abcdefghigklmnopqrstuvwxyz'
    alphabet_high = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
    plaintext = ''

    if ciphertext != '':
        n = 0
        if len(ciphertext) != len(keyword):
            for i in range(len(ciphertext) - len(keyword)):
                keyword += keyword[n]
                n = n + 1

        ch = ciphertext[0]
        if 'a' <= ch <= 'z':
            n = 0
            for abc in ciphertext:
                lowshift = alphabet_low.index(keyword[n])
                newnumb = 97 + (ord(abc) - lowshift - 97) % 26
                plaintext += chr(newnumb)
                n = n + 1
        elif 'A' <= ch <= 'Z':
            n = 0
            for abc in ciphertext:
                highshift = alphabet_high.index(keyword[n])
                newnumb = 65 + (ord(abc) - highshift - 65) % 26
                plaintext += chr(newnumb)
                n = n + 1
        else:
            for abc in plaintext:
                newnumb = ord(abc)

    return plaintext
