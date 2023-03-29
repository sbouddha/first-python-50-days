import pandas as pd

nato_csv=r"C:\Without_Sync\Py\python-100-days\Day_26\nato_phonetic_alphabet.csv"

data = pd.read_csv(nato_csv)

#TODO: First create this CSV in a dictionary for letter to code
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO: Enter a word and create a phonetic code

word = input("Enter word : ").upper()

output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
