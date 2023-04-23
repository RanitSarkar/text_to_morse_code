den_Code = input("E for encode \n D for decode.. \n  ").upper()

morse_dict = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-', " ": " "}


def main_func():
    global den_Code
    user_word = input("enter the word.. ").upper()

    def encrypt(word):
        encoded_word = []
        for _ in str(word):
            encoded_character = morse_dict.get(f"{_}")
            encoded_word.append(encoded_character)
        return ' '.join(encoded_word)

    def decrypt(word):
        decoded_word = []
        for _ in str(word):
            decoded_character = inv_map.get(f"{_}")
            decoded_word.append(decoded_character)
            return ' '.join(decoded_word)

    if den_Code == "E":
        print(encrypt(user_word))
    else:
        inv_map = {v: k for k, v in morse_dict.items()}
        print(decrypt(user_word))


main_func()
