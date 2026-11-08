import random
from collections import Counter

# ==========================================================
# Training Text
# ==========================================================

text = """
Machine learning is a part of artificial intelligence.
Artificial intelligence is changing the world.
Learning from data is the heart of machine learning.
The world is changing fast because of artificial intelligence.
Data is the fuel of machine learning and artificial intelligence.
""".lower()

# ==========================================================
# Question 1: Prepare the Words
# ==========================================================

text = text.replace(".", "")
words = text.split()

print("Question 1")
print("Number of words:", len(words))
print("First ten words:", words[:10])
print("Number of unique words:", len(set(words)))

# ==========================================================
# Question 2: Build the Transition Chain
# ==========================================================

chains = {}

for i in range(len(words) - 1):
    chains.setdefault(words[i], []).append(words[i + 1])

print("\nQuestion 2")
print("Transition Dictionary:")
print(chains)

# One word can have several possible next words because
# the same word may appear multiple times in different
# places within the training text.

# ==========================================================
# Question 3: Inspect Learned Transitions
# ==========================================================

print("\nQuestion 3")

for word in ["artificial", "is", "machine"]:
    print(f"Next words for '{word}':", chains.get(word, []))

# ==========================================================
# Question 4: Create a Safe Generator
# ==========================================================

def generate(start_word, max_new_words=15):
    start_word = start_word.lower()

    if start_word not in chains:
        return f"No continuation found for '{start_word}'"

    result = [start_word]
    current = start_word

    for _ in range(max_new_words):
        next_words = chains.get(current)

        if not next_words:
            break

        next_word = random.choice(next_words)
        result.append(next_word)
        current = next_word

    return " ".join(result)

print("\nQuestion 4")
print(generate("artificial"))

# ==========================================================
# Question 5: Make Random Output Reproducible
# ==========================================================

print("\nQuestion 5")

random.seed(42)
output1 = generate("artificial")

random.seed(42)
output2 = generate("artificial")

print("Output 1:")
print(output1)

print("\nOutput 2:")
print(output2)

print("\nAre both outputs equal?", output1 == output2)

# A random seed ensures that the same sequence of random
# choices is generated every time, making debugging and
# result comparison easier.

# ==========================================================
# Question 6: Compare Starting Words
# ==========================================================

print("\nQuestion 6")

for word in ["machine", "data", "world"]:
    print(f"\nStarting with '{word}':")
    print(generate(word))

# ==========================================================
# Question 7: Find the Most Likely Next Word
# ==========================================================

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

# ==========================================================
# Question 8: Handle an Unknown Start Word
# ==========================================================

print("\nQuestion 8")

print(generate("robot"))

print("Program executed successfully without raising an exception.")

# ==========================================================
# Question 9: Explain the Limitations
# ==========================================================

# 1. This generator can only use word transitions that
#    appear in the training text. It cannot invent new
#    knowledge or understand meaning.

# 2. The output can become repetitive or grammatically
#    incorrect because it only predicts one word at a
#    time without understanding the whole sentence.

# 3. This one-word transition model is very different
#    from a transformer. Transformers use attention,
#    understand long-range context, and learn complex
#    language patterns, whereas this model simply chooses
#    the next word from previously observed transitions.

print("\nQuestion 9")
print("This classroom generator is not a real GPT model.")