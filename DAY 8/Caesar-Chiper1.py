alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift) :
    encrypted_text = ''
    for char in text :
        if char in alphabet:
            position = alphabet.index(char)
            new_position  = (position+shift) %26
            encrypted_char = alphabet[new_position]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
        
    return encrypted_text

def decrypt(text, shift ):
    decrypted_text = ''
    for char in text :
        if char in alphabet:
            position = alphabet.index(char)
            new_position  = (position+shift) %26
            decrypted_char = alphabet[new_position]
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
            
            
if direction == 'encode':
    result = encrypt(text, shift)
    print("Pesan ter-enkripsi : ", result)
elif direction == 'decode' :
    result = decrypt(text, shift)
    print("pesan terdekripsi: ", result)
else:
    print("Pesan tidak valid")

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 