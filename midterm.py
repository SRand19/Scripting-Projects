import string

filename = input("Enter the requested files name: ")

with open(filename, 'r') as f_in:
    text = f_in.read()

num_lines = text.count('\n') + 1
num_words = len(text.split())
num_chars = len(text)

print(f"Number of lines: {num_lines}")
print(f"Number of words: {num_words}")
print(f"Number of characters: {num_chars}")

translator = str.maketrans('', '', string.punctuation + string.digits)
clean_text = text.translate(translator)

word_freq = {}
for word in clean_text.split():
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

sorted_word_freq = sorted(word_freq.items(), key = lambda x: x[0])

pair_freq = {}
words = clean_text.split()
for i in range(len(words)-1):
    pair = f"{words[i]} {words[i+1]}"
    if pair in pair_freq:
        pair_freq[pair] += 1
    else:
        pair_freq[pair] = 1

sorted_pair_freq = sorted(pair_freq.items(), key=lambda x: x[0])

output = "Results from " + filename

with open(output, 'w') as f_out:
    f_out.write(f"Number of lines: {num_lines}")
    f_out.write(f"Number of words: {num_words}")
    f_out.write(f"Number of characters: {num_chars}\n")
    f_out.write("\nList of unique words and theri frequencies:\n")
    for word, freq in sorted_word_freq:
        f_out.write(f"{pair} ({freq})\n")

    f_out.write(f"\nList of 2 word pairs and their frequencies:\n")
    for pair, freq in sorted_word_freq:
        if freq >= 2:
            f_out.write(f"{pair} ({freq})\n")

    total_words = len(words)
    avg_word_length = sum(len(word) for word in words) / total_words
    unique_words = len(word_freq)
    avg_unique_word_length = sum(len(word) for word in word_freq) / unique_words
    num_frequent_pairs = sum(1 for freq in pair_freq.values() if freq >= 2)

    f_out.write(f"\nFinal results:\n")
    f_out.write(f"Total number of words: {total_words}\n")
    f_out.write(f"Average length of a word: {avg_word_length:.2f}\n")
    f_out.write(f"Number of unique words: {unique_words}\n")
    f_out.write(f"Average number of letters in unique words: {avg_unique_word_length:.2f}\n")
    f_out.write(f"Number of word pairs that appear more than once: {num_frequent_pairs:.2f}\n")
    

