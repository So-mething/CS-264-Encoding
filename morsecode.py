Morse_Code_Dictionary = {'a': '.-','b': '-...','c': '-.-.','d': '-..','e': '.','f': '..-.','g': '--.','h': '....','i': '..','j': '.---','k': '-.-','l': '.-..','m': '--','n': '-.','o': '---','p': '.--.','q': '--.-','r': '.-.','s': '...','t': '-','u': '..-','v':'...-','w': '.--','x': '-..-','y': '-.--','z': '--..', ' ': '/'} 

Reverse_Morse_Dictionary = {value: key for key, value in Morse_Code_Dictionary.items()}

def process_morse(message, action):
    if action == "decode":
        return morse_to_words(message)
    else:
        return words_to_morse(message)

def words_to_morse(message): 
    if not message:
        return "No plaintext provided."
        
    message = message.lower()
    morse_result = []

    for char in message:
        if char in Morse_Code_Dictionary:
            morse_result.append(Morse_Code_Dictionary[char])
        else:
            return "Error: For the time being, numbers and special characters are not allowed."
    
    return " ".join(morse_result)

def morse_to_words(morse_message): 
    if not morse_message:
        return ""

    morse_symbols = morse_message.strip().split() 
    decoded_result = []
        
    # i = 0
    # while i < len(morse_symbols):
    #     symbol = morse_symbols[i]
    for symbol in morse_symbols:
        if symbol == "/":
            decoded_result.append(" ")
        elif symbol in Reverse_Morse_Dictionary:
            decoded_result.append(Reverse_Morse_Dictionary[symbol])
        else:
            return "Error: Invalid Morse code detected. Please use dots/dashes, spaces between letters, and '/' between words."
            
    return "".join(decoded_result)
            # raise ValueError(f"The morse code '{symbol}' is invalid")

