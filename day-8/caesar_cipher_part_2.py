alphabet = ['a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 
            'y', 'z', 'a', 'b', 
            'c', 'd', 'e', 'f', 
            'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 
            'u', 'v', 
            'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

def decrypt(coded_text, shift_amount):
    decoded = ""
    for letter in coded_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        decoded += alphabet[new_position]
    print(f"Decrypted: {decoded}")
 

if direction == 'encrypt':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(coded_text=text, shift_amount=shift)
else:
    print("Ok")