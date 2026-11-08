# Day 18 Answers

## Question 1

### Training a Language Model from Scratch

Training a language model from scratch requires a very large amount of text data, powerful computers (such as GPUs or TPUs), and a long training time. It is expensive and usually done by large organizations.

### Using a Pre-trained Model

A pre-trained model has already learned language patterns from a large dataset. It can be fine-tuned or directly used for many tasks with much less data, lower computing cost, and shorter training time.

| Feature | Training from Scratch | Pre-trained Model |
|---------|-----------------------|-------------------|
| Data Requirement | Very large dataset | Small task-specific dataset |
| Computing Cost | Very high | Much lower |
| Training Time | Weeks or months | Minutes to hours |
| Advantage | Full control over training | Faster and more cost-effective |

**Reason to choose a pre-trained model:** It saves time, reduces costs, and provides good performance for many tasks.

---

## Question 2

Sequence:

I → love → machine → learning

### RNN/LSTM Processing

An RNN or LSTM processes one word at a time.

1. Read **I**.
2. Update its hidden state.
3. Read **love** while remembering information from **I**.
4. Read **machine** using previous information.
5. Read **learning** using all earlier context.

Each word depends on the hidden state from the previous step.

### Transformer Processing

A transformer processes all words at the same time. During training, every token can attend to the other tokens, allowing it to understand relationships in parallel instead of one word after another.

---

## Question 3

Process:

Text
   ↓
Tokens
   ↓
Embeddings
   ↓
Transformer Layers
   ↓
Output

### Explanation

- **Text:** The original sentence.
- **Tokens:** The sentence is split into smaller pieces called tokens.
- **Embeddings:** Each token is converted into a vector that represents its meaning.
- **Transformer Layers:** The model uses attention and neural networks to understand relationships between tokens.
- **Output:** The model generates a prediction, answer, or next word.

Example sentence:

I love AI

Simple token list:

["I", "love", "AI"]

Embeddings are vectors containing numerical representations that capture the meaning and context of each token. The actual values are learned during training.

---

## Question 4

Sentences:

Dog bites man.
Man bites dog.

Although both sentences contain the same words, their meanings are different because the word order changes who is performing the action.

Transformers use **positional encoding** to remember the position of each word. This helps the model understand that changing the order changes the meaning.

---

## Question 5

Sentence:

The animal did not cross the road because it was tired.

The word **it** most likely refers to **the animal**.

The surrounding words provide context. Since being tired is something that describes an animal rather than a road, attention helps the model connect **it** with **animal** instead of another word.

---

## Question 6

Sentence:

The cat sat on the mat because it was tired.

### Query

**What am I looking for?**

The word **it** looks for the noun it refers to.

### Key

**What information is available?**

Words like **cat**, **mat**, and other tokens provide information that may match the query.

### Value

**What information should be passed forward?**

The most relevant information from the matching word is passed to help understand the sentence.

The word **cat** should receive more attention than **mat** because being tired is a characteristic of a living animal, not an object like a mat.

---

## Question 7

Formula:

Attention(Q, K, V) = softmax(QKᵀ / √d) V

- A **high attention score** means two tokens are strongly related.
- A **low attention score** means the relationship between the tokens is weak.
- **Softmax** converts the scores into probabilities so they are easy to compare and sum to 1.
- The scores are applied to the **values** so that the model gives more importance to relevant information and less importance to unrelated information.

---

## Question 8

Sentence:

The student solved the problem because he understood the concept.

Different attention heads may focus on different relationships.

### Head 1 – Grammar

Identifies that **student** is the subject and **solved** is the verb.

### Head 2 – Subject-Object Relationship

Connects **student** with **problem** to understand who solved what.

### Head 3 – Meaning

Recognizes that understanding the concept explains why the problem was solved.

### Head 4 – Pronoun Reference

Connects **he** with **student** instead of **problem**.

Using several attention heads allows the model to learn different types of relationships at the same time, leading to a better understanding than using only one head.

---

## Question 9

+--------------------------------------+
| Embeddings + Positional Encoding     |
+--------------------------------------+
                 |
                 v
+--------------------------------------+
| Multi-Head Self-Attention            |
+--------------------------------------+
                 |
                 v
+--------------------------------------+
| Add & Norm                           |
+--------------------------------------+
                 |
                 v
+--------------------------------------+
| Feed-Forward Network                 |
+--------------------------------------+
                 |
                 v
+--------------------------------------+
| Add & Norm                           |
+--------------------------------------+
                 |
                 v
+--------------------------------------+
| Output to the Next Layer             |
+--------------------------------------+

**Attention:** The attention layer helps each token focus on the most relevant words in the sentence so that it understands context and relationships.

**Feed-Forward Network:** The feed-forward network processes each token's representation to learn more complex patterns before passing the information to the next layer.

---

## Question 10

### 1. Considering many words together

Transformers examine relationships between many words at the same time, allowing them to better understand the overall context.

### 2. Capturing long-range relationships

They can connect words that are far apart in a sentence, improving understanding of meaning and references.

### 3. Parallel Training

Unlike RNNs, transformers process tokens simultaneously, making training much faster on modern hardware.

### 4. Scaling

Transformer models generally improve as they are trained with more data, more computing power, and more model parameters, enabling powerful large language models.

### Limitation

Large transformer models require significant computing resources, memory, and energy, making them expensive to train and run.
