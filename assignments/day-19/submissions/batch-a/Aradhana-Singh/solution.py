# ## Topic: Build a Baby GPT With Word Transitions

# This is a small word-transition generator, not a real GPT model. It demonstrates how a program can learn which words followed other words in a sample.

import random
from collections import Counter

# Use this training text:
text = """
Machine learning is a part of artificial intelligence.
Artificial intelligence is changing the world.
Learning from data is the heart of machine learning.
The world is changing fast because of artificial intelligence.
Data is the fuel of machine learning and artificial intelligence.
""".lower()

# ### Question 1: Prepare the Words
# Remove full stops from `text`, split it into a list named `words`, and print:
# 1. the number of words;
# 2. the first ten words;
# 3. the number of unique words.
text = text.replace(".", "")
words = text.split()

print("Number of words:", len(words))
print("First ten words:", words[:10])
print("Number of unique words:", len(set(words)))


# ### Question 2: Build the Transition Chain
# Create an empty dictionary named `chains`.
chains = {}
# For every word except the last word, store the following word in a list:
for i in range(len(words)-1):
    chains.setdefault(words[i], []).append(words[i + 1])

# Print the complete dictionary.
print("Transition Dictionary:")
print(chains)

# In a comment, explain why one word can have several possible next words.
# One word can have several possible next words because the same word may appear multiple times in different sentences with different following words.


# ### Question 3: Inspect Learned Transitions
# Print the possible next words for:
print("Possible next words:")
print("artificial ->", chains.get("artificial", []))
print("is ->", chains.get("is", []))
print("machine ->", chains.get("machine", []))


# ### Question 4: Create a Safe Generator
# Write: The function must:
# 1. convert `start_word` to lowercase;
# 2. return `No continuation found for '<word>'` if it is not in `chains`;
# 3. begin the result with the start word;
# 4. repeatedly choose a next word using `random.choice`;
# 5. stop after at most `max_new_words` new words;
# 6. stop early if the current word has no continuation;
# 7. return one joined string.
def generate(start_word, max_new_words=15):
    start_word = start_word.lower()
    if start_word not in chains:
        return f"No continuation found for '{start_word}'"
    result = [start_word]
    current = start_word
    for _ in range(max_new_words):
        next_words = chains.get(current, [])
        if not next_words:
            break
        current = random.choice(next_words)
        result.append(current)
    return " ".join(result)

# Generate and print text starting with `artificial`.
print("Generated Text:")
print(generate("artificial"))


# ### Question 5: Make Random Output Reproducible
# Generate one result. Reset the same seed to `42`, generate again, and print whether the two results are equal.
random.seed(42)
output1 = generate("artificial")
random.seed(42)
output2 = generate("artificial")

print("First Output:")
print(output1)

print("Second Output:")
print(output2)

print("Outputs are equal:", output1 == output2)
# In a comment, explain how a seed helps debugging and comparison.
# Using the same random seed produces the same random output every time, which helps in debugging and testing.


# ### Question 6: Compare Starting Words
# Generate text from:
# machine
# data
# world
# Print a clear label before every result. The generated wording does not need to match another student's wording.
print("Starting word: machine")
print(generate("machine"))

print("Starting word: data")
print(generate("data"))

print("Starting word: world")
print(generate("world"))


# ### Question 7: Find the Most Likely Next Word
def most_likely_next(word):
    next_words = chains.get(word.lower(), [])
    if not next_words:
        return None
    counter = Counter(next_words)
    return counter.most_common(1)[0]

print("Most Likely Next Words:")
print("artificial ->", most_likely_next("artificial"))
print("machine ->", most_likely_next("machine"))
print("unknown ->", most_likely_next("robot"))


# ### Question 8: Handle an Unknown Start Word
# Print the returned message and confirm that the program does not raise an exception.
print("Unknown Start Word:")
print(generate("robot"))
print("The program handled the unknown word without raising an exception.")


# ### Question 9: Explain the Limitations
# 1. Why can the generator only use patterns found in its training text?
# The generator only uses patterns that appear in the training text, so it cannot create completely new knowledge.

# 2. Why can the output become repetitive or grammatically incorrect?
# The output may become repetitive or grammatically incorrect because it predicts only the next word without understanding the complete sentence.

# 3. How is this one-word transition model different from a transformer?
# This one-word transition model looks only at the current word, while a transformer considers relationships between many words at once using self-attention and understands a much larger context.

# Also print one sentence stating that this classroom generator is not a real GPT model.
print("This classroom generator is not a real GPT model.")