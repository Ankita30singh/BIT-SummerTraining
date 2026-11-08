# Day 18 Answers

Completed during maintainer review of an empty submission, at the instructor's request.

## Question 1

Training from scratch requires a large dataset, substantial computing resources, and a long training period. A pre-trained model reuses parameters already learned from earlier training, reducing the data and compute needed for a new application. It is useful when resources are limited, although its suitability and limitations must still be evaluated.

## Question 2

An RNN or LSTM processes `I -> love -> machine -> learning` one step at a time, carrying a hidden state forward. Transformer training can compute many token relationships in parallel through attention. Autoregressive generation still produces new tokens sequentially.

## Question 3

`Text -> Tokens -> Embeddings -> Transformer layers -> Output`

`I love AI` might become the illustrative token list `[I, love, AI]`; the real split depends on the tokenizer. Each token ID maps to a learned vector. Transformer layers combine these representations with context, and an output head produces predictions such as next-token probabilities. No invented vector values are needed to explain this process.

## Question 4

In `Dog bites man`, the dog is the subject; in `Man bites dog`, the man is the subject. Token identity alone cannot represent that change. Positional encodings or other positional mechanisms supply information about order or relative position so attention can distinguish these relationships.

## Question 5

In `The animal did not cross the road because it was tired`, `it` most plausibly refers to the animal. The surrounding meaning of tiredness and crossing supports that reading. Attention allows token representations to use information from other relevant tokens, though an attention weight alone is not proof of a correct interpretation.

## Question 6

A Query represents what a token is looking for, a Key represents information that other positions can match, and a Value represents the information passed onward. When interpreting `it` in `The cat sat on the mat because it was tired`, the cat is the plausible tired subject. Relevant attention heads may therefore emphasize `cat` over `mat`, but the actual weights depend on the model and layer.

## Question 7

`Attention(Q, K, V) = softmax(QKᵀ / √d) V`

The query-key similarities are scaled by the square root of the key dimension. A high normalized score gives a position more influence on the resulting representation; a low score gives it less. Softmax converts the scores into nonnegative weights summing to one. Applying those weights to the values combines the information to pass forward.

## Question 8

For `The student solved the problem because he understood the concept`, different heads can potentially track grammatical agreement, the student-to-problem subject-object relation, the connection between understanding and solving, and the pronoun `he` referring to `student`. Multiple heads provide several learned representation subspaces. These are possible relationships, not fixed assignments guaranteed for particular heads.

## Question 9

```text
Embeddings + Positional Encoding
              |
              +--------------------+
              v                    |
    Multi-Head Self-Attention       |
              |                    |
              v                    |
          Add & Norm <-------------+
              |
              +--------------------+
              v                    |
      Feed-Forward Network         |
              |                    |
              v                    |
          Add & Norm <-------------+
              |
      Output to the next layer
```

Attention mixes information across relevant token positions. The feed-forward network applies a learned nonlinear transformation to each position. The residual paths preserve information and support optimization; normalization helps stabilize the representations.

## Question 10

Transformers can relate many tokens within the available context and connect distant words through attention. Parallel processing during training makes good use of accelerators. Increasing training data, compute, and model parameters can improve capability when the training setup is suitable. Large models still have substantial memory and computing costs, and their outputs can be wrong.
