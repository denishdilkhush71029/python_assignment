def char_frequency(sentence):
    freq = {}
    for char in sentence:
        if char.isalpha():
            char = char.lower()
            freq[char] = freq.get(char, 0) + 1
    return freq

text = input("Enter a sentence: ")
print(char_frequency(text))