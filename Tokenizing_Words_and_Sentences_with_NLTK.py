from nltk.tokenize import sent_tokenize, word_tokenize

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

print(sent_tokenize(text))
print(word_tokenize(text))
