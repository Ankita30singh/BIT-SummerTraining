# Day 18 Answers

## Question 1

### Training from Scratch vs Pre-trained Model

| Training from Scratch | Pre-trained Model |
|------------------------|-------------------|
| Requires a very large dataset. | Uses an already trained model. |
| Very high computing cost. | Much lower computing cost. |
| Takes weeks or months to train. | Can be fine-tuned in a short time. |

**Reason to choose a pre-trained model:**  
It saves time, reduces cost, and provides good performance without training a model from the beginning.

---

## Question 2

### RNN/LSTM Processing

For the sequence:

```
I → love → machine → learning
```

An RNN or LSTM reads one word at a time.

1. Read "I"
2. Read "love"
3. Read "machine"
4. Read "learning"

Each step depends on the previous hidden state, so the sequence is processed one by one.

### Transformer Processing

A transformer can look at all the words at the same time. During training, it learns the relationships between every pair of words in parallel, making training much faster than RNNs or LSTMs.

---

## Question 3

### Text → Tokens → Embeddings → Transformer Layers → Output

- **Text:** Original sentence entered by the user.
- **Tokens:** The text is split into smaller units.
- **Embeddings:** Each token is converted into a vector that represents its meaning.
- **Transformer Layers:** The model learns relationships between the tokens using attention.
- **Output:** The model generates the final prediction or response.

Example:

Sentence:

```
I love AI
```

Tokens:

```
["I", "love", "AI"]
```

Embeddings are numerical vectors that represent the meaning of each token. Similar words have similar vector representations.

---

## Question 4

### Positional Encoding

Sentence 1:

```
Dog bites man.
```

Sentence 2:

```
Man bites dog.
```

Both sentences contain the same words, but their meanings are different because the word order changes.

Positional encoding tells the transformer the position of each word, allowing it to understand the correct meaning of the sentence.

---

## Question 5

Sentence:

```
The animal did not cross the road because it was tired.
```

The word **"it"** most likely refers to **the animal**.

The surrounding words provide context that helps the model understand that the animal was tired, not the road.

Attention allows the transformer to focus on the most relevant words when identifying what a pronoun refers to.

---

## Question 6

Sentence:

```
The cat sat on the mat because it was tired.
```

### Query
**What am I looking for?**

The model tries to find what the word **"it"** refers to.

### Key
**What information is available?**

The sentence contains words like **cat**, **sat**, **mat**, and **tired**.

### Value
**What information should be passed forward?**

The model passes the information from the word that best matches the query.

The word **cat** should receive more attention than **mat** because living things can be tired, while a mat cannot.

---

## Question 7

### Attention Formula

```
Attention(Q, K, V) = softmax(QKᵀ / √d) V
```

- A **high attention score** means two words are strongly related.
- A **low attention score** means the words have little relationship.
- **Softmax** converts the scores into probabilities that add up to 1.
- The scores are multiplied with the **Values** so that more important information contributes more to the final output.

---

## Question 8

Sentence:

```
The student solved the problem because he understood the concept.
```

Different attention heads may focus on different relationships:

1. Grammar (subject and verb relationship)
2. Subject-object relationship
3. Meaning of the sentence
4. Pronoun reference ("he" refers to "student")

Multiple attention heads are useful because each head learns different types of relationships, helping the model understand the sentence more accurately.

---

## Question 9

### Transformer Block Diagram

```text
+------------------------------+
| Embeddings + Positional      |
| Encoding                     |
+------------------------------+
              |
              v
+------------------------------+
| Multi-Head Self-Attention    |
+------------------------------+
              |
              v
+------------------------------+
| Add & Norm                   |
+------------------------------+
              |
              v
+------------------------------+
| Feed-Forward Network         |
+------------------------------+
              |
              v
+------------------------------+
| Add & Norm                   |
+------------------------------+
              |
              v
+------------------------------+
| Output to the Next Layer     |
+------------------------------+
```

**Attention:**  
The attention layer finds important relationships between different words in the sentence.

**Feed-Forward Network:**  
The feed-forward network processes the attention output further and learns more complex patterns before sending it to the next layer.

---

## Question 10

### Why Transformers Enabled Modern LLMs

1. **Considering many words together:**  
   Transformers can process all words in a sentence simultaneously.

2. **Capturing long-range relationships:**  
   They can connect words that are far apart in a sentence.

3. **Parallel training:**  
   Since all words are processed together, training is much faster than sequential models like RNNs.

4. **Scaling:**  
   Transformers improve their performance when trained with larger datasets, more computing power, and more model parameters.

**Limitation:**  
Large transformer models require significant memory, computing resources, and energy, making them expensive to train and deploy.