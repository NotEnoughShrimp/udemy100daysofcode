import caesar_art
alphabet = ['a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 
            'y', 'z']
def caesar(cipher_direction, plain_text, shift_amount):
    output = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        output += alphabet[new_position]
    print(f"The {cipher_direction}d message is: {output}")

print(caesar_art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if shift > len(alphabet):
    shift %= 26

caesar(cipher_direction=direction, plain_text=text, shift_amount=shift)