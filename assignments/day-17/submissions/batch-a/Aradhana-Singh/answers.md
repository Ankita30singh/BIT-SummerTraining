# Day 17 Answers

## Question 1

### Traditional Machine Learning vs Deep Learning

**Traditional Machine Learning:**
In traditional machine learning, humans manually select the important features from the data before training the model.

**Example:** Predicting house prices using features like area, number of bedrooms, and location.

**Deep Learning:**
In deep learning, the model automatically learns useful features from raw data without requiring manual feature selection.

**Example:** Image recognition where a neural network automatically learns shapes, edges, and objects from images.

---

## Question 2

### 1. What is a Large Language Model (LLM)?

A Large Language Model (LLM) is an AI model trained on large amounts of text to understand and generate human-like language.

### 2. What is a Token?

A token is a small unit of text that an AI model processes. It can be a word, part of a word, punctuation, or a symbol.

### 3. What does a Context Window limit?

A context window limits how much text an AI model can remember and process at one time.

### Sentence Split (Word Approximation)

Artificial | intelligence | is | changing | the | world.

Total words (approximate tokens): **6**

A real tokenizer may split words differently because it often breaks words into smaller pieces instead of treating every word as a single token.

---

## Question 3

### Prompt 1

**Prompt:**
```
Explain machine learning.
```

**Summary of Response:**
The response explained what machine learning is and how computers learn from data.

---

### Prompt 2

**Prompt:**
```
Explain machine learning to a 10-year-old in two sentences using one cricket example.
```

**Summary of Response:**
The response used simple language and explained machine learning with a cricket example that was easy to understand.

---

### Which response was more useful?

The second response was more useful because it was simple, specific, easy to understand, and followed all the given instructions.

---

## Question 4

### Prompt 1

```
Task: Classify the following review as Positive, Negative, or Neutral.

Review:
"Service bahut slow thi, dobara nahi aaunga."

Output Format:
Label:
Reason:

Tone: Professional

Constraint: Explain the reason in exactly one sentence.
```

---

### Prompt 2

```
Task: Create a Hinglish Instagram caption for a home-cleaning service.

Output Format:
Caption:
Hashtags:

Tone: Friendly and Attractive

Constraint: Keep the caption under 20 words and include exactly three hashtags.
```

---

## Question 5

Before answering, I would first verify whether the person "Dr. Rakesh Chaturvedi Meelan" exists and whether the claimed inventions are real.

Reliable sources to verify the information:
1. Google Scholar – https://scholar.google.com
2. Government or official research institute websites (such as CSIR, DRDO, or university websites)

If I cannot verify the claim, I would say:
> "I could not find reliable evidence confirming this information, so I cannot confidently answer the question."

An AI may sound confident even when the information is incorrect, so confident wording is not proof of accuracy.

**Access Date:** 22 July 2026

---

## Question 6

The connection is:

```
Text → Embeddings → Vector Database → Relevant Results → LLM Answer
```

- Text is converted into embeddings.
- Embeddings are stored in a vector database.
- The vector database finds the most relevant information.
- The retrieved information is given to the LLM.
- The LLM generates an accurate answer using the retrieved content.

A training institute can use Retrieval-Augmented Generation (RAG) by storing its class notes in a vector database. When students ask questions, the system retrieves the relevant notes and the LLM answers using those notes instead of relying only on its training data.

---

## Question 7

### 1. AI Agent vs Chatbot

A chatbot mainly generates text responses, while an AI agent can use tools, make decisions, and perform tasks automatically.

### 2. What is a Tool?

A tool is an external resource or software that an AI agent uses to complete tasks, such as searching the web, accessing databases, or sending emails.

### 3. What is MCP?

MCP (Model Context Protocol) helps AI systems connect with external tools, applications, and data sources in a standard and secure way.

### Example Agent Task

**Task:** Book a flight.

**Steps:**
1. Understand the user's travel request.
2. Search available flights.
3. Compare prices.
4. Select the best option.
5. Confirm with the user.
6. Complete the booking.

---

## Question 8

### Responsible AI Checklist

- ✅ Verify important facts before using AI-generated information.
- ✅ Do not share personal or sensitive information with AI.
- ✅ Check for bias or unfair statements.
- ✅ Review the output manually before using it.
- ✅ Acknowledge reliable sources whenever required.
- ✅ Confirm that the output follows the requested format.

### Reflection

AI can make mistakes or generate incorrect information. Important decisions should always be verified using trusted sources and human judgment. I should not rely only on AI for medical, legal, financial, or other critical decisions.