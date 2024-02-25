characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
              'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4',
              '5', '6', '7', '8', '9', '0', '!', '@', '#', '$',
              '%', '^', '&', '*', '(', ')', '-', '_', '+', '=',
              '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'",
              '<', '>', ',', '.', '?', '/', '`', '~', ' ',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(message, key):
    encrypted_message = ''
    for character in message:
        index = characters.index(character) + int(key[0])

        if index > len(characters):
            index = index - len(characters)

        encrypted_message += characters[index]
    #print(encrypted_message)
    encrypted_message2 = ''
    for character in encrypted_message:
        index = characters.index(character) + int(key[1:3])

        if index > len(characters):
            index = index - len(characters)
        encrypted_message2 += characters[index]
    #print(encrypted_message2)
    return encrypted_message2

def decrypt(message, key):
    decrypted_message = ''
    for character in message:
        charnum = characters.index(character)

        if int(key[0]) > charnum:
            charnum += 95

        decrypted_message += characters[charnum - int(key[0])]
    #print(decrypted_message)
    decrypted_message2 = ''
    for character in decrypted_message:
        charnum = characters.index(character)

        if int(key[0]) > charnum:
            charnum += 95

        decrypted_message2 += characters[charnum - int(key[1:3])]
    return decrypted_message2

def main():
    option = input("Would you like to encrypt or decrypt? ")

    if option.lower() == "encrypt":
        text = input("What text would you like to encrypt? ")
        key = input("What key would you like to use (3-digit numbers only)? ")
        enc = encrypt(text, key)
        print(enc)
    elif option.lower() == "decrypt":
        text = input("What text would you like to decrypt? ")
        key = input("What key would you like to use (3-digit numbers only)? ")
        dec = decrypt(text, key)
        print(dec)
    else:
        main()

    #print(decrypt(enc, "625"))

if __name__ == '__main__':
    main()