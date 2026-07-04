from art import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
invalid_caracter = ['', ' ', ';',':','&','é','_','!', 'ç', 'à', '=', '-', '<', '>', '/', ',','*']


def get_user_inputs():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    return direction, text, shift

def ask_restart():
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if restart == "yes":
        return True
    else:
        return False

def encrypt(original_text, shift_amount):
    encrytp_text = ""
    index_real_word = []
    encoded_index = []

    for letter in original_text:
        if letter in alphabet:
            index_real_word.append(alphabet.index(letter))
        if letter in invalid_caracter:
            index_real_word.append(letter)

    for item in index_real_word:
        if isinstance(item, int):
            new_index = item + shift_amount
            encoded_index.append(new_index)
        else:
            encoded_index.append(item)

    for index in encoded_index:
        if isinstance(index, int):
            encrytp_text += alphabet[index]
        else:
            encrytp_text += index

    print(f"Here's the encoded result: {encrytp_text}")


def decode(original_text, shift_amount):
    decode_text = ""
    encoded_index = []
    index_real_word= []

    for letter in original_text:
        if letter in alphabet:
            encoded_index.append(alphabet.index(letter))
        if letter in invalid_caracter:
            encoded_index.append(letter)

    for item in encoded_index:
        if isinstance(item, int):
            new_index = item - shift_amount
            index_real_word.append(new_index)
        else:
            index_real_word.append(item)

    for index in index_real_word:
        if isinstance(index, int):
            decode_text += alphabet[index]
        else:
            decode_text += index

    print(f"Here's the decoded result: {decode_text}")


def orchestration():
    print (art)
    direction, text, shift = get_user_inputs()

    if direction == "encode":
        encrypt(text, shift)

    if direction == "decode":
        decode(text, shift)

    restart = ask_restart()

    if restart is True:
        orchestration()




orchestration()


