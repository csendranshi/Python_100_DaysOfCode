alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text,shift):
    encoded=""

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    for i in range (len(text)):
        encoded+=chr(((ord(text[i])+shift-97)%26)+97)

    print(f"Encrypted text is: {encoded}.")


# DE-Cryption

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):
    decoded=""
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
    for i in range(len(text)):
        decoded += chr(((ord(text[i]) - shift - 97) % 26) + 97)

    print(f"The Decrypted text is {decoded}.")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# if direction=='encode':
#     encrypt(text=text, shift=shift)
# elif direction=='decode':
#     decrypt(text=text,shift=shift)
# else:
#     print("Please enter a valid direction.")

# COMBINED

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(text, shift, direction):
    res=""

    for i in range(len(text)):
        if direction == "encode":
            res += chr(((ord(text[i]) + shift - 97) % 26) + 97)
        elif direction=="decode":
            res += chr(((ord(text[i]) - shift - 97) % 26) + 97)

    print(f"The {direction}d text is: {res}.")

caesar(text,shift,direction)