LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    plaintext = 'Tvoje mama smrdi'
    key = 'OSELPRDEL'
    def_mode = 'encrypt'

    ret_msg = ''

    if def_mode == 'encrypt':
        ret_msg = translate_message(key, plaintext, 'encrypt')
    elif def_mode == 'decrypt':
        ret_msg = translate_message(key, plaintext, 'decrypt')

    print(ret_msg)


def translate_message(key, message, mode):
    translated = []  # stores the encrypted/decrypted message string

    key_index = 0
    key = key.upper()

    for symbol in message:  # loop through each character in message
        num = LETTERS.find(symbol.upper())
        if num != -1:  # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[key_index])  # add if encrypting
            elif mode == 'decrypt':
                num -= LETTERS.find(key[key_index])  # subtract if decrypting

            num %= len(LETTERS)  # handle the potential wrap-around

            # add the encrypted/decrypted symbol to the end of translated.
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            key_index += 1  # move to the next letter in the key
            if key_index == len(key):
                key_index = 0
        else:
        # The symbol was not in LETTERS, so add it to translated as is.
            translated.append(symbol)

    return ''.join(translated)


if __name__ == '__main__':
    main()