#2
word = input()
vowels = 'aeiouy'
vowel_list = []
consonant_list = []
for k in range(len(word)):
    if word[k] in vowels or word[k] in vowels.upper():
        for i in range(k, len(word)):
            vowel_list.append(word[k:i+1])
    else:
        for j in range(k, len(word)):
            consonant_list.append(word[k:j+1])
print({el: vowel_list.count(el) for el in vowel_list}, {elem: consonant_list.count(elem) for elem in consonant_list}, sep="\n")

