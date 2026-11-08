import random
from collections import Counter


# Training Text


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

print("Question 1")
print("Number of words:", len(words))
print("First ten words:", words[:10])
print("Number of unique words:", len(set(words)))


# Question 2: Build the Transition Chain


chains = {}

for i in range(len(words) - 1):
    chains.setdefault(words[i], []).append(words[i + 1])

print("\nQuestion 2")
print("Transition Dictionary:")
print(chains)

# One word can have several possible next words because
# the same word may appear in different places in the training text,
# followed by different words.


# Question 3: Inspect Learned Transitions


print("\nQuestion 3")
print("Next words for 'artificial':", chains.get("artificial", []))
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

        next_word = random.choice(next_words)
        result.append(next_word)
        current = next_word

    return " ".join(result)


print("\nQuestion 4")
print(generate("artificial"))


# Question 5: Make Random Output Reproducible


random.seed(42)
result1 = generate("artificial")

random.seed(42)
result2 = generate("artificial")

print("\nQuestion 5")
print("First Result:")
print(result1)

print("\nSecond Result:")
print(result2)

print("\nAre both results equal?", result1 == result2)

# Using the same random seed produces the same random sequence,
# making debugging, testing, and result comparison easier.


# Question 6: Compare Starting Words


print("\nQuestion 6")

print("\nStart Word: machine")
print(generate("machine"))

print("\nStart Word: data")
print(generate("data"))

print("\nStart Word: world")
print(generate("world"))


# Question 7: Find the Most Likely Next Word


def most_likely_next(word):
    word = word.lower()

    if word not in chains:
        return None

    counter = Counter(chains[word])
    return counter.most_common(1)[0]


print("\nQuestion 7")
print("artificial:", most_likely_next("artificial"))
print("machine:", most_likely_next("machine"))
print("unknown:", most_likely_next("unknown"))


# Question 8: Handle an Unknown Start Word


print("\nQuestion 8")

unknown_result = generate("robot")

print(unknown_result)
print("Program executed successfully without raising an exception.")


# Question 9: Explain the Limitations


print("\nQuestion 9")
print("This classroom generator is not a real GPT model.")

# 1. The generator can only use word transitions that already
#    exist in the training text. It cannot invent new knowledge.
#
# 2. The output may become repetitive or grammatically incorrect
#    because it only looks at one previous word instead of the
#    full sentence context.
#
# 3. A one-word transition model simply chooses the next word
#    based on previous observations. A transformer uses attention
#    mechanisms to understand relationships between many words
#    across the entire context, making it much more powerful.