MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
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
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    text = ""
    for char in message:
        if char != " ":
            if char in MORSE_CODE_DICT:
                text += MORSE_CODE_DICT[char] + " "
            else:
                #when char is not in morse code dict, then we dont want to stop game,
                # but we will let you know which char is not in morse:
                print(f"that {char} not in dict ")
                continue
        else:
            #makes double " ", which helps us to decrypt
            text += " "
    return text


def decrypt(message):
    #change the order of keys and values, not values, morse code, is keys and now we can decrypt
    reversed_morse = {v: k for k, v in MORSE_CODE_DICT.items()}
    #split message per " " for easier loop
    text = message.split(" ")
    data = ""
    for char in text:
        if char != "":
            if char in reversed_morse:
                data += reversed_morse[char]
        else:
            data += " "
    return data.lower()


def play():
    #play function has its direction which function will trigger.
    #text is for encrypt, morse is for decrypt
    direction = input("What you wanna to convert? text or morse: ").lower()
    message = input("type your message: ").upper()
    if direction == "text":
        print(encrypt(message))
    elif direction == "morse":
        print(decrypt(message))


play()

#another guess,if y - repeat play function again and again, if n - converter stops
while input("again? y or n: ") == "y":
    play()

