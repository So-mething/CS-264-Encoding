Morse_Code_Dictionary = {'a': '.-','b': '-...','c': '-.-.','d': '-..','e': '.','f': '..-.','g': '--.','h': '....','i': '..','j': '.---','k': '-.-','l': '.-..','m': '--','n': '-.','o': '---','p': '.--.','q': '--.-','r': '.-.','s': '...','t': '-','u': '..-','v':'...-','w': '.--','x': '-..-','y': '-.--','z': '--..', ' ': '/'} 

Reverse_Morse_Dictionary = {value: key for key, value in Morse_Code_Dictionary.items()}

def words_to_morse(message): 
    if not message:
        raise ValueError("The input cannot be empty.")
        
    message = message.lower()
    morse_result = []

    for i in range(len(message)):
        char = message[i] 
        if char in Morse_Code_Dictionary:
            morse_result.append(Morse_Code_Dictionary[char])
        else:
            raise ValueError(f"The character '{char}' is invalid")
    
    return " ".join(morse_result)

def morse_to_words(morse_message): 
    if not morse_message:
        raise ValueError("The input cannot be empty")

    morse_symbols = morse_message.strip().split() 
    decoded_result = []
        
    i = 0
    while i < len(morse_symbols):
        symbol = morse_symbols[i]
        
        if symbol == "/":
            decoded_result.append(" ")
        elif symbol in Reverse_Morse_Dictionary:
            decoded_result.append(Reverse_Morse_Dictionary[symbol])
        else:
            raise ValueError(f"The morse code '{symbol}' is invalid")
        i += 1 

Morse_Code_Dictionary = {'a': '.-','b': '-...','c': '-.-.','d': '-..','e': '.','f': '..-.','g': '--.','h': '....','i': '..','j': '.---','k': '-.-','l': '.-..','m': '--','n': '-.','o': '---','p': '.--.','q': '--.-','r': '.-.','s': '...','t': '-','u': '..-','v':'...-','w': '.--','x': '-..-','y': '-.--','z': '--..', ' ': '/'} 

Reverse_Morse_Dictionary = {value: key for key, value in Morse_Code_Dictionary.items()}

def words_to_morse(message): 
    if not message:
        raise ValueError("The input cannot be empty.")
        
    message = message.lower()
    morse_result = []

    for i in range(len(message)):
        char = message[i] 
        if char in Morse_Code_Dictionary:
            morse_result.append(Morse_Code_Dictionary[char])
        else:
            raise ValueError(f"The character '{char}' is invalid")
    
    return " ".join(morse_result)

def morse_to_words(morse_message): 
    if not morse_message:
        raise ValueError("The input cannot be empty")

    morse_symbols = morse_message.strip().split() 
    decoded_result = []
        
    i = 0
    while i < len(morse_symbols):
        symbol = morse_symbols[i]
        
        if symbol == "/":
            decoded_result.append(" ")
        elif symbol in Reverse_Morse_Dictionary:
            decoded_result.append(Reverse_Morse_Dictionary[symbol])
        else:
            raise ValueError(f"The morse code '{symbol}' is invalid")
        i += 1 
        
    return "".join(decoded_result)

