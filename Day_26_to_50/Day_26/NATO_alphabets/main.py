# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd

file_df = pd.read_csv('nato_phonetic_alphabet.csv')
print(file_df.to_dict())

new_dict = {row.letter:row.code for (index,row) in file_df.iterrows() }
# print(new_dict)
run = True
while run:
    try:
        user_word = input("Enter the word: ").upper()
        result = [new_dict[letter] for letter in user_word]
        print(result)
        run = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")