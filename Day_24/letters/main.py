# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
mail_draft = open("Input/Letters/starting_letter.docx")
draft = mail_draft.read()
# Replace the [name] placeholder with the actual name.
names_file = open("Input/Names/invited_names.txt")
Names = names_file.readlines()

for name in Names:
    send_file = open(f"Output/ReadyToSend/Invite_{name.strip()}.docx",'w')
    draft.replace('[name]',name.strip())
    send_file.write(draft)

# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp