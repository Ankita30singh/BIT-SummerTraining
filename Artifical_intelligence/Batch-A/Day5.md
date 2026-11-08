# Vectors kya hai ?

VECTOR = numbers ki ordered list

[3,4]   -> 2D vector

[3,4,5]. -> 3D Vector

[0.2, 0.9, ...., 0.1]. -> 768D vectors

# Vectors Data ko represent karta hai ?

ghar: [area, bedrooms, price] = [1200, 3, 50000]

student: [marks, attendance] = [85, 90]

words : [0.2, 0.9, 0.1...] = embeddings


# Dimension

2D -> graph p draw kar sakte hai

3D - still imagine kr sakte hai

768 - draw/imagine NAHI kar sakte hai , par math same hoti hai

" HIGH_DIMENSIONAL SPACE " - > bs zayada number


# Vecter Operations

Addition: [3,4] + [1,2] = [4,6]

Subtraction: [3,4] - [1,2] = [2,2]

Scalar Multiply: 2 * [3,4]  = [6,8]

# Magnitude / Norm -- LEngth

|v| -- vector ki LENGTH ( origin se kitna door )

[3,4]  = 5 ( Pythagoras!)


# Distance -- Vectors kitne door

Euclidean Distance = Straight line distance

A = [3,4]
B = [1,2]

sqrt(3-1)^2 + (4-2)^2
=  2.83

Manhattan Dostance = grid distance

A = [3,4]
B =[1,2]

|3-1| + |4-2|
2 + 2 = 4

# DOT Product

DOT Product = corresponding numbers multiply krk jodo

[3,4] . [1,2] = 3 x 1 + 4 x 2 = 11

Batata hai : do vecotrs kitne " same direction" mein hai

# Cosine Similarity

Cosine Similarity = angle similarity

cosine = (A . B) / (|A| x |B|)


cosine  similarity = 1 ( Same DIrection )


cosine similary = 0  ( Unrelated )

cosine similarity = -1 ( Opposite direction )

Example:

Document A :  AI is changing education.

Document B: Aritificial Intelligence is transforming learning.

# Cosine vs Euclidean - Kab Kya?

A = [1,1]
B = [10, 10]

Same direction
Different Size

Euclidean distance = large
Cosine = 1.0

Euclidean: distance zayada hai
Cosine: direction same hai


## Embeddings

# The Problem - shabdon ko Number kaise banayein ?

words ko numbers mein kaise convert karein ?

# One-Hot Encoding -- Purana Tarika + Problems

Vocabulary : [cat, dog, king, queen]

ONE-HOT:
cat= [1,0,0,0]
dog= [0,1,0,0]
king=[0,0,1,0]

# Embeddings kya hai ?

EMBEDDING = text  ko DENSE ( chota, bhara hua)  vector mein badalna

cat = [0.8, 0.2, 0.1 ...] ( 768 real numbers)

dog = [0.79, 0.25, 0.1...] ( cat ke PASS - dono animals!)

king = [0.1, 0.1,0.9....] ( door - alag concept)

# Meaning kaise aata hai ?

Distributional Hyppothesis

" You shall know a word by the company it keeps. "

The ____ barked loudly.

The ___ meowed.


# Famous Analogy -> King - man + women = queen

vector(king) - vector(man) + vector(women) = vector(queen)

Paris - France + Italy = Rome

# Dimensions  - 768, 1536

Embedding  dimension = vector mein kitne numbers

768D = 768 numbers

1536D = 1536 numbers

# Types of Embeddings

WORD embedding  --> ek shabd

SENTENCE embedding  --> poori sentence ( mordern, hum use krte hai )

DOCUMENT embedding --> poora docuemnt

IMAGE embedding --> CLIP ( image)


MULTIPMODEL  --> text + image ek hi space mein


# Embeddings kaise milte

EMBEDDING MODEL/API se  -- text bhejo , vector milta hai

# Applications

Sementic search --> meaning se dhoodhna , keyword s  nahi

Recommendation --> simillary Itrms ( Youtube, spotify)

Clustering.   - > similar cheezo ka group


Classiffication  ---> embeddings + simple model

Deduplication --> similar/duplicate content pakdna

RAG --> LLM ko relevant data dena

# Limitations

BIAS --> training data ke biases embeddings mein aate hai

DOMAIN --> medical/legal text pe general embeddings kamzor

BLACK BOX --> har dimension ka exact matlab nahi pata

CUTOFF --> naye shabd/context model ki training tak


## Vector DB

# Nearest Neighbour search karo

kaam: ek query vector ke sabse PASS wale vectors dhoodho ( top-k )

EXACT (KNN) -> sabse se compare krk perfect dhoodhna par dheema hai

APPROXIMATE (ANN) -> thoda approximate, par SUPER fast

# Vector Database kya hai ?

V.D  = embeddingsstore + FAST similarity search (ANN)

ADD (id, vector, text, metadata)

QUERY(vector, k) -> tok-k simillar (milliseconds mein)