import pandas

data = pandas.read_csv("C:\\Users\\Welcome\\OneDrive\\Desktop\\Python\\Mini Project\\NATO Alphabet Project\\nato_phonetic_alphabet.csv")


phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dic)

word = input("Enter a word: ").upper()

output = [phonetic_dic[letter] for letter in word]
print(output)



