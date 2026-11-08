#day19
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

words = text.replace(".", "").split()

print("Number of words:", len(words))

print("First ten words:")
print(words[:10])

print("Number of unique words:", len(set(words)))



# Question 2: Build the Transition Chain

chains = {}

for i in range(len(words) - 1):
    chains.setdefault(words[i], []).append(words[i + 1])


print("\nComplete Transition Dictionary:")
print(chains)


# One word can have several possible next words because the same word
# can appear in different sentences with different following words.



# Question 3: Inspect Learned Transitions

print("\nPossible next words:")

print("artificial:", chains.get("artificial", []))

print("is:", chains.get("is", []))

print("machine:", chains.get("machine", []))



# Question 4: Create a Safe Generator

def generate(start_word, max_new_words=15):

    start_word = start_word.lower()

    if start_word not in chains:
        return f"No continuation found for '{start_word}'"

    result = [start_word]

    current_word = start_word

    for _ in range(max_new_words):

        next_words = chains.get(current_word, [])

        if not next_words:
            break

        next_word = random.choice(next_words)

        result.append(next_word)

        current_word = next_word


    return " ".join(result)



print("\nGenerated text starting with artificial:")

print(generate("artificial"))



# Question 5: Make Random Output Reproducible

random.seed(42)

result1 = generate("artificial")

random.seed(42)

result2 = generate("artificial")


print("\nFirst Result:")
print(result1)

print("\nSecond Result:")
print(result2)

print("\nAre both results equal?", result1 == result2)


# A seed makes random output repeatable. It helps in debugging,
# testing, and comparing results because the same random choices occur.



# Question 6: Compare Starting Words

random.seed(42)

print("\nGenerated from machine:")
print(generate("machine"))


print("\nGenerated from data:")
print(generate("data"))


print("\nGenerated from world:")
print(generate("world"))



# Question 7: Find the Most Likely Next Word

def most_likely_next(word):

    word = word.lower()

    if word not in chains:
        return None

    counts = Counter(chains[word])

    return counts.most_common(1)[0]



print("\nMost likely next words:")

print("artificial:", most_likely_next("artificial"))

print("machine:", most_likely_next("machine"))

print("unknown:", most_likely_next("unknown"))



# Question 8: Handle Unknown Start Word

print("\nUnknown word test:")

print(generate("robot"))

print("Program handled unknown word without an exception.")



# Question 9: Explain Limitations

# This generator can only use patterns found in its training text because
# it only learns word-to-word relationships from the given data.

# The output can become repetitive or grammatically incorrect because
# it does not understand meaning, grammar, or long-term context.

# This one-word transition model only predicts the next word based on the
# previous word, while a transformer uses attention to understand
# relationships between many words and the complete context.

print("\nThis classroom generator is not a real GPT model.")