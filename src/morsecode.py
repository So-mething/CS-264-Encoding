Morse_Code_Dictionary = {'a': '.-','b': '-...','c': '-.-.','d': '-..','e': '.','f': '..-.','g': '--.','h': '....','i': '..','j': '.---','k': '-.-','l': '.-..','m': '--','n': '-.','o': '---','p': '.--.','q': '--.-','r': '.-.','s': '...','t': '-','u': '..-','v':'...-','w': '.--','x': '-..-','y': '-.--','z': '--..', ' ': '/'} 

Reverse_Morse_Dictionary = {value: key for key, value in Morse_Code_Dictionary.items()}

def morse_to_words(morse_message): 
    decoded_message = []
    words = morse_message.strip().split(" / ")

    for word in words:
        letters = word.split()
        decoded_word = ""

        for letter in letters: 
            if letter in Reverse_Morse_Dictionary:
               decoded_word += Reverse_Morse_Dictionary[letter] 
            else: 
                return "Invalid Morse Code" 

        decoded_message.append(decoded_word)

    return " ".join(decoded_message)

   
def words_to_morse(message): 
    morse_message = [] 

    for char in message.lower(): 
        if char in Morse_Code_Dictionary: 
            morse_message.append(Morse_Code_Dictionary[char])       
    return " ". join(morse_message)
