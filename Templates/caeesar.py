alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode not in ("encode", "decode"): 
        raise ValueError("Choose 'encode' or 'decode'")
        
    if not isinstance(shift_amount, int):
        raise TypeError("The shift amount must be an integer")
        
    shift_amount = shift_amount % len(alphabet)

    if encode_or_decode == "decode":
        shift_amount *= -1

    if not isinstance(original_text, str):
        raise TypeError("The original text must be a string")

    original_text = original_text.lower()
    output_text = ""

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    # print(f"Here is the {encode_or_decode}d result: {output_text}")
    return output_text


