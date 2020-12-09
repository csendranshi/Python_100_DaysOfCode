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

file_df =  pd.read_csv('nato_phonetic_alphabet.csv')
print(file_df.to_dict())
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
new_dict = {row.letter:row.code for (index,row) in file_df.iterrows() }
# print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Enter the word: ").upper()
result = [new_dict[letter] for letter in user_word]
print(result)
