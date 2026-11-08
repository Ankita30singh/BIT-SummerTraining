Pre-Trained Models  -

cost, time

# Transformer se pehle problem kya thi ?

I love machine learning

The student who studied machine learning for many months finally passed


# Transformer ka core idea: Attention

The animal did not cross the road beciuse it was tired.


# Self-Attention kya hota hai ?

I deposited money in the bank

I sat near the river bank

# transformer words kao kaise samajhta hai ?

Text -> Tokens -> Embeddings -> Transformer Layers -> Output

Example:

I Love AI

["I","love","AI"] -> number/vectors

# Postional Encoding Kyu chahiye ?

Example:
Dog bites man.
Man bites dog.

Word meaning + word Position = Better Understanding

# Query, Key, Value

Q, K, V

Q - Mai kya dhoodh rha hun ?
K - Mere pass kis type ki information hai ?
V - Actual Information kya hai ?


Sentence: The cat sat on the mat because it was tired.

Q- it kis object/person ko refer kar raha hai?
k - cat, mat, tired
V - Cat infomation gets mpore weight

# Attention Score ka formula

high score - Zayada attention
low score - kam attention

# Multi-Head attention Kya hai ?

Ex:
The student solved the problem becuase he understood the concept

Head 1- Grammar relation
Head 2 - Subject object relatoon
head 3 - meaning/ context
head 4 - pronoun reference

# Transformer Block k andar kya hota hai ?

~~~ Simple Diagram ~~~
Input Embeddings
    |
Multi-Head Self-Attention
    |
Feed Forward Network
    |
Output Representation

~~~ Advanced Version ~~~

Embeddinga + Postional Encoding
    |
Multi-Head Attention
    |
Add & Norm
    |
Feed Forward Network
    |
Add & Norm
    |
Next Layer


# Transformer ne LLMs ko possible kyu bnaya ?

1. It can look at many words together
2. It capture long-range relationship.
3. It can train faster using parallel computation
4. It scales well with more data, more compute and bigger models
