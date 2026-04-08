alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def vigenere(original_text, key_word, encode_or_decode): # I need to get better at using functions
    key_word = key_word.replace(" ", "")
    if not key_word:
        return "The key cannot be empty."
    
    if not key_word.isalpha():
        return "The key must contain only letters."
    
    if encode_or_decode not in ["encode", "decode"]:
        return "The mode must be 'encode' or 'decode'."

    original_text = original_text.lower()
    key_word = key_word.lower()

    output_text = "" # This is to just put whatever the encryption is gonna put out.
    key_length = len(key_word) # Gets and assigns the length of the key so we can loop through the key word if it's smaller than the plaintext
    key_index = 0
    
    for i in range(len(original_text)): # The loop that iterates i through a range of 0 to X, with X being the actual length of the plaintext
        char = original_text[i] # Checks the character at each position in the original text, since strings are basically lists themselves.
        
        if char not in alphabet: # If it's not in the alphabet, we just put it in anyways. Pretty sure that's how whitespace is also transferred but wtv idrk
            output_text += char
            continue 

        else:
            key_char = key_word[key_index % key_length] # Assigns a character from the actual key to the variable "key_char". The index is basically "i modulo length of the key" so we can cycle through them later
            shift_amount = alphabet.index(key_char) 

            # The shift amount is determined by the index of the character found from key_char. It takes the character and looks at where it is in the alphabet.
            # The "+1" is there because the index would otherwise go 0-25, meaning if you had a key letter of "A" it just wouldn't move. This is not how the cipher works, so this way you still move
            # EX: Ptext = A; Key = A; Encryption = B (A itself is the first letter, so you move it by 1)

            if encode_or_decode == "decode": # This is to move backwards when decoding.
                shift_amount *= -1
                
            shifted_position = alphabet.index(char) + shift_amount # Yeah you can probably tell what this does
            shifted_position %= len(alphabet) # This is so we don't go out of bounds with the actual list and go to like idk an index of 42 or smth
            output_text += alphabet[shifted_position] # Adds whatever letter in the alphabet is in the position of the "shifted_position" value to the actual output
            key_index += 1 
            
    # print(f"Here is the {encode_or_decode}d result: {output_text}") # Self explanatory
    return output_text

should_continue = True # This is set to true so that if you go through the process and then want to stop, you can then stop. Will likely get removed when implemented into the JS
