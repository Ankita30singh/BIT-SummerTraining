# Day 17 Answers

## Question 1

### Traditional Machine Learning

Traditional machine learning usually requires a person to choose the important features from the data before training the model. The model learns using these manually selected features.

**Example:** A spam email detector that uses manually selected features like the number of links, email length, and certain keywords.

### Deep Learning

Deep learning uses neural networks that can automatically learn useful features directly from raw data, reducing the need for manual feature selection.

**Example:** A face recognition system that learns facial features directly from images.

---

## Question 2

### 1. What is a Large Language Model (LLM)?

A Large Language Model (LLM) is an AI model trained on a large amount of text so it can understand and generate human-like language.

### 2. What is a token?

A token is a small piece of text that an AI model processes. It can be a word, part of a word, punctuation, or another symbol.

### 3. What does a context window limit?

A context window limits how much text the model can consider at one time while generating a response.

### Sentence split into words (simple approximation of tokens)

Sentence:

> Artificial intelligence is changing the world.

Words:

- Artificial
- intelligence
- is
- changing
- the
- world.

A real tokenizer may split words into smaller parts or separate punctuation differently depending on how the AI model is designed.

---

## Question 3

### Prompt 1

**Prompt:**

Explain machine learning.

**Summary of the response:**
The response gave a general explanation of machine learning, describing how computers learn patterns from data and make predictions.

### Prompt 2

**Prompt:**

Explain machine learning to a 10-year-old in two sentences using one cricket example.

**Summary of the response:**
The response explained machine learning in very simple language and used a cricket example, making it easy for a child to understand.

### Which response was more useful and why?

The second response was more useful because it clearly specified the audience, response length, and example, resulting in a simpler and more focused explanation.

---

## Question 4

### Prompt1

Task: Classify the following review as Positive, Negative, or Neutral.

Review:
"Service bahut slow thi, dobara nahi aaunga."

Output Format:

- Sentiment:
- Explanation:

Tone: Professional.

Constraint: Use only one sentiment label and explain the reason in exactly one sentence.

### Prompt2

Task: Create a short Hinglish Instagram caption for a home-cleaning service.

Output Format:
Caption:
Hashtags:

Tone: Friendly and promotional.

Constraints:

- Maximum 25 words.
- Include one emoji.
- Include exactly two relevant hashtags.

## Question 5

Before answering, I would first verify whether **Dr. Rakesh Chaturvedi Meelan** is a real scientist and whether the claimed inventions are supported by reliable evidence.

### Reliable sources to search

1. Google Scholar  
   https://scholar.google.com/

2. Google Patents  
   https://patents.google.com/

**Access Date:** 16 July 2026

If I could not verify the claim, I would respond:

> "I could not find reliable evidence confirming this person's identity or the claimed inventions. Therefore, I cannot verify the information."

Confident wording from an AI is not proof because AI can generate information that sounds correct even when it is inaccurate or unsupported by reliable sources.

## Question 6

The process works like this:
**Text → Embeddings → Vector Database → Relevant Results → LLM Answer**

- The text is converted into numerical embeddings.
- The embeddings are stored in a vector database.
- A user's question is also converted into an embedding.
- The vector database finds the most similar information.
- The LLM uses the retrieved information to generate an accurate answer.

A training institute can use Retrieval-Augmented Generation (RAG) by storing its class notes in a vector database. When students ask questions, the system retrieves the most relevant notes and provides answers based on those notes instead of relying only on the model's general knowledge.

---

## Question 7

### 1. Difference between an AI agent and a chatbot

A chatbot mainly generates text responses, while an AI agent can plan tasks, make decisions, and use external tools to complete actions.

### 2. What is a tool?

A tool is an external service or application that an AI agent can use, such as a calculator, search engine, database, calendar, or email service.

### 3. How MCP helps

Model Context Protocol (MCP) provides a standard way for AI systems to connect with different tools and data sources, making integration easier and more consistent.

### Example Agent Task

**Task:** Schedule a meeting.

**Steps:**

1. Read the user's request.
2. Check participants' calendars.
3. Find an available time.
4. Create the meeting event.
5. Send invitations.
6. Confirm the meeting details to the user.

---

## Question 8

### Responsible AI Checklist

- ✅ Verify important facts using reliable sources.
- ✅ Protect personal and private information.
- ✅ Check for bias or unfair statements.
- ✅ Review the AI-generated content before using it.
- ✅ Acknowledge or cite sources when required.
- ✅ Ensure the output follows the requested format and instructions.
- ✅ Check grammar, spelling, and clarity.
- ✅ Confirm that the information is current and accurate.

### Reflection

I should not rely only on an AI answer for important decisions involving health, law, finance, or safety. AI can sometimes produce incorrect or outdated information that needs verification. I should always use human judgment and trusted sources before accepting important information.
