Morse_Code_Dictionary = {'a': '.-','b': '-...','c': '-.-.','d': '-..','e': '.','f': '..-.','g': '--.','h': '....','i': '..','j': '.---','k': '-.--','l': '.-..','m': '--','n': '-.','o': '---','p': '.--.','q': '--.-','r': '.-.-','s': '...','t': '-','u': '..-','v':'...-','w': '.--','x': '-..-','y': '-.--','z': '--..', ' ': '/'} 

def words_to_morse(message): 
    morse = [] 

for char in message.lower(): 
    if char in Morse_Code_Dictionary: 
        morse_message.append(Morse_Code_Dictionary[char]) 
    else:
        pass 
        
return " ". join(morse_message)
