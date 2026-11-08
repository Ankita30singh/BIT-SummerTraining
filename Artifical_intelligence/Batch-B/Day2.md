Pre-Trained Models

Train from scrat -> Costly, time

Use Pre-Trained Models -> 2, 3 line code



RNN/LSTM  model

I -> love -> Machine -> Learning


The students who studied machine learning for many months finally passed

# Attention

Ex:
The animal did not cross the road because it was tired.

# Self Attention

I deposited money in the bank.

I sat near the river bank.


I love AI


# Transformer words kaise samjhata hai. ?
["I", "Love", "AI"]  -> [numbers/vectors]

Text -> Tokens -> Embeddings -> Transformer Layers -> Output


# Postional Encoding

Example:
Dog bites man.
Man bites dog.

Word meaning + Word Postion = Better Understanding

# Query, Key, Value -> Simple analogy

Q - Query
K - Key
V - Value


Q -  Main kya doodh raha hoon ?
K - Mere Pass kis typ eki information hai ?
V - Actual information kya hai ?

Example:

The cat sat on the mat because it was tired.

Q - it kis object/person ko refer kr rha hai ?
K - cat, mat , tired
V- cat infomration gets more weight

# Attention Score ka simple formula

Attention( Q, K, V) = softmax(QK(power) T / sqrtd) V

High Score - zaya attention
low score - kam attention

# Multi-Head Attention kya hai ?

Ex:
The student solved the problem because he understood the concept.

Head 1. grammar relation
Head 2. Subject-object relation
Head 3. Meaning / Context
Head 4. Pronoun Reference

# Transformer block k andar kya hota hai

Input Embeddings
    |
Multi-Head  Self attention
    |
Feed Forward Network
    |
Output Representation

~~~ Advanced Version ~~~

Embedings + Postional Encoding
    |
Multi-head Attention
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
2. It capture long-range relationships
3. It can train faster using parallel computation
4. It scales well with more data, more compute and bigger models