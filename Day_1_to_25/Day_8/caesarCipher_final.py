from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    res=""

    for i in range(len(text)):
        if text[i] in alphabet:
            if direction == "encode":
                res += chr(((ord(text[i]) + shift - 97) % 26) + 97)
            elif direction=="decode":
                res += chr(((ord(text[i]) - shift - 97) % 26) + 97)
        else:
            res+=text[i]

    print(f"The {direction}d text is: {res}.\n")


# TODO-1: Import and print the logo from art.py when the program starts.
print(logo)
# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a new function that calls itself if they type 'yes'.

print("Welcome to to cipher-inator!\n")
choice = "yes"

while choice == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text=text, shift=shift, direction=direction)

    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

print("Goodbye!")



# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Hint: Think about how you can use the modulus (%).

