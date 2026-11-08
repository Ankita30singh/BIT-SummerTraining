# Day 17 Answers

## Question 1

### Traditional Machine Learning vs Deep Learning

**Traditional Machine Learning:**
Traditional machine learning usually requires people to select the important features from the data before training the model. The model then learns using those selected features.

**Example:**
A spam email detector where features such as the number of links, special characters, or certain keywords are manually selected.

**Deep Learning:**
Deep learning automatically learns useful features directly from raw data using neural networks. It requires less manual feature engineering.

**Example:**
A face recognition system that learns facial features directly from images without manually selecting them.

---

## Question 2

### 1. What is a Large Language Model (LLM)?

A Large Language Model (LLM) is an AI model trained on a large amount of text to understand and generate human-like language.

### 2. What is a token?

A token is a small unit of text that an AI model processes. A token may be a word, part of a word, punctuation, or a symbol.

### 3. What does a context window limit?

A context window limits how much text the model can consider at one time while generating a response.

### Sentence Split (Approximate Tokens)

Sentence:

Artificial intelligence is changing the world.

Approximate tokens:

- Artificial
- intelligence
- is
- changing
- the
- world

A real tokenizer may split words differently because it breaks text into smaller pieces based on its own encoding rules.

---

## Question 3

### Prompt 1

**Prompt:**

Explain machine learning.

**Response Summary:**

The response gave a general explanation of machine learning, including its definition and how computers learn from data.

### Prompt 2

**Prompt:**

Explain machine learning to a 10-year-old in two sentences using one cricket example.

**Response Summary:**

The response explained machine learning in very simple language using a cricket example, making it easy to understand.

### Which response was more useful?

The second response was more useful because it matched the audience, used simple language, followed the requested length, and included a relevant example.

---

## Question 4

### Prompt 1

**Task:** Classify a review

```
Classify the following review as Positive, Negative, or Neutral. Explain your answer in exactly one sentence. Use a professional tone and return the answer in the format:

Sentiment:
Explanation:

Review:
"Service bahut slow thi, dobara nahi aaunga."
```

### Prompt 2

**Task:** Instagram Caption

```
Create a short Hinglish Instagram caption for a home-cleaning service. Keep the tone friendly and attractive. The caption should be under 20 words and include exactly two relevant hashtags.
```

---

## Question 5

Before answering, I would verify whether Dr. Rakesh Chaturvedi Meelan is a real scientist and whether the claimed inventions actually exist.

### Reliable sources

1. Google Scholar (https://scholar.google.com/)
2. Official government or university websites

If I could not verify the claim, I would say:

"I could not find reliable evidence confirming this person's inventions. Therefore, I cannot confidently provide an answer."

Confident wording from an AI is not proof because AI can generate incorrect or unverified information that sounds convincing.

**Access Date:** 27 July 2026

---

## Question 6

The process works like this:

**Text → Embeddings → Vector Database → Relevant Results → LLM Answer**

- Text is converted into embeddings (numerical vectors).
- The embeddings are stored in a vector database.
- When a user asks a question, the database finds the most similar information.
- The relevant information is sent to the LLM.
- The LLM generates an accurate answer using the retrieved information.

### Example

A training institute can store its class notes in a vector database. When students ask questions, the system retrieves the most relevant notes and provides answers based on the institute's own material instead of relying only on general knowledge.

---

## Question 7

### 1. AI Agent vs Chatbot

A chatbot mainly answers questions by generating text.

An AI agent can use tools, perform multiple actions, make decisions, and complete tasks automatically.

### 2. What is a tool?

A tool is an external resource that an AI agent uses, such as a calculator, search engine, database, or API.

### 3. How MCP helps

Model Context Protocol (MCP) provides a standard way for AI systems to connect with tools, databases, and external services safely and efficiently.

### Example Agent Task

**Task:** Book a meeting.

Steps:

1. Read the user's request.
2. Check the calendar.
3. Find an available time.
4. Schedule the meeting.
5. Send invitations.
6. Confirm the booking to the user.

---

## Question 8

### Responsible AI Checklist

- Verify important facts before using AI-generated information.
- Never share private or sensitive personal information with AI tools.
- Check the output for possible bias or unfair statements.
- Review and edit the content before submitting or publishing it.
- Acknowledge or cite reliable sources whenever required.
- Ensure the output follows the requested format and instructions.
- Correct any grammatical or factual mistakes.
- Use trusted sources to confirm important information.

### Reflection

AI can sometimes generate incorrect or outdated information. I should not rely only on AI for important decisions involving health, law, finance, or academic facts. Human review and fact-checking are necessary before trusting or submitting AI-generated content.