alphabet_en_lower_case = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
alphabet_en_upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_ru_lower_case = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_ru_upper_case = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def update_cipher_text(cipher_text, shift, letter, alphabet):
    position = alphabet.find(letter)
    new_position = position + shift
    cipher_text += alphabet[new_position]
    return cipher_text


def update_decrypted_text(decrypted_text, shift, letter, alphabet):
    position = alphabet.find(letter)
    new_position = position - shift
    decrypted_text += alphabet[new_position]
    return decrypted_text


def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet_en_upper_case:
            cipher_text = update_cipher_text(cipher_text, shift, letter, alphabet_en_upper_case)
        elif letter in alphabet_en_lower_case:
            cipher_text = update_cipher_text(cipher_text, shift, letter, alphabet_en_lower_case)
        elif letter in alphabet_ru_upper_case:
            cipher_text = update_cipher_text(cipher_text, shift, letter, alphabet_ru_upper_case)
        elif letter in alphabet_ru_lower_case:
            cipher_text = update_cipher_text(cipher_text, shift, letter, alphabet_ru_lower_case)
        else:
            cipher_text += letter
    return cipher_text


def decipher(text, shift):
    decrypted_text = ""
    for letter in text:
        if letter in alphabet_en_upper_case:
            decrypted_text = update_decrypted_text(decrypted_text, shift, letter, alphabet_en_upper_case)
        elif letter in alphabet_en_lower_case:
            decrypted_text = update_decrypted_text(decrypted_text, shift, letter, alphabet_en_lower_case)
        elif letter in alphabet_ru_upper_case:
            decrypted_text = update_decrypted_text(decrypted_text, shift, letter, alphabet_ru_upper_case)
        elif letter in alphabet_ru_lower_case:
            decrypted_text = update_decrypted_text(decrypted_text, shift, letter, alphabet_ru_lower_case)
        else:
            decrypted_text += letter
    return decrypted_text


def result(number):
    if number == 1:
        return print("Cipher text : ", encrypt(message, interval))
    elif number == 2:
        return print("Decrypted text : ", decipher(message, interval))


while True:
    choice = int(input("What do you want to do? Encrypt - 1, decipher - 2, finish - 0  : "))
    if choice != 0:
        message = input("Enter your message: ")
        while True:
            try:
                interval = int(input("Enter an interval: "))
                break
            except Exception:
                print("Check if the data is correct")
        result(choice)
    else:
        break



