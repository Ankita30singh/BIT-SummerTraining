import random
from collections import Counter

text = """
Machine learning is a part of artificial intelligence.
Artificial intelligence is changing the world.
Learning from data is the heart of machine learning.
The world is changing fast because of artificial intelligence.
Data is the fuel of machine learning and artificial intelligence.
""".lower()


# Question 1: Prepare the Words


text = text.replace(".", "")
words = text.split()

print("Total Words:", len(words))
print("First 10 Words:", words[:10])
print("Unique Words:", len(set(words)))

# Question 2: Build the Transition Chain


chains = {}

for i in range(len(words) - 1):
    chains.setdefault(words[i], []).append(words[i + 1])

print("\nTransition Chain:")
print(chains)

# One word can have several possible next words because
# the same word appears in different sentences.

# Question 3: Inspect Learned Transitions


print("\nNext words for 'artificial':", chains.get("artificial", []))
print("Next words for 'is':", chains.get("is", []))
print("Next words for 'machine':", chains.get("machine", []))


# Question 4: Create a Safe Generator


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

print("\nGenerated Text:")
print(generate("artificial"))
# Question 5: Random Seed


random.seed(42)
text1 = generate("artificial")

random.seed(42)
text2 = generate("artificial")

print("\nFirst Output:")
print(text1)

print("\nSecond Output:")
print(text2)

print("\nAre both outputs equal?", text1 == text2)

# Seed makes random output repeatable, which helps in debugging
# and comparing program results.

# Question 6: Compare Starting Words


print("\nStarting Word: machine")
print(generate("machine"))

print("\nStarting Word: data")
print(generate("data"))

print("\nStarting Word: world")
print(generate("world"))


# Question 7: Most Likely Next Word


def most_likely_next(word):
    word = word.lower()

    if word not in chains:
        return None

    counter = Counter(chains[word])
    return counter.most_common(1)[0]

print("\nMost Likely Next Word:")
print("artificial ->", most_likely_next("artificial"))
print("machine ->", most_likely_next("machine"))
print("robot ->", most_likely_next("robot"))


# Question 8: Unknown Start Word


print("\nUnknown Word Test:")
print(generate("robot"))

print("Program executed successfully without any exception.")

# Question 9: Limitations


# 1. The generator can only use patterns that exist in the
#    training text because it does not have any extra knowledge.
#
# 2. The output may become repetitive or grammatically incorrect
#    because it only looks at one previous word.
#
# 3. This model is different from a transformer because it only
#    predicts using one-word transitions, while transformers
#    understand the context of many words together.

print("\nThis classroom generator is not a real GPT model.")