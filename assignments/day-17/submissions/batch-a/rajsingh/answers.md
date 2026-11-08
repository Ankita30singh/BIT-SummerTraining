# Day 17 Answers

Completed during maintainer review of an empty submission, at the instructor's request.

## Question 1

Traditional machine learning often uses features chosen by people: a house-price model might use floor area and room count. Deep learning uses several learned layers to derive representations from raw inputs; an image classifier can learn edges and object patterns from pixels.

## Question 2

A large language model learns patterns in large text datasets to predict and generate tokens. A token is a unit such as a word, word fragment, or punctuation mark. The context window limits the tokens available to one model invocation, including its input and generated output.

Classroom word split: `Artificial | intelligence | is | changing | the | world.` Real tokenizers can separate punctuation or divide words into smaller pieces.

## Question 3

Prompt: `Explain machine learning.` Response summary: machine learning learns patterns from examples to make predictions. The broad wording leaves the audience, length, and example unspecified.

Prompt: `Explain machine learning to a 10-year-old in two sentences using one cricket example.` Illustrative response: A computer can learn from old cricket scores to guess how many runs a team may make. It improves by studying examples, but its next guess can still be wrong.

The specific prompt is more useful for the requested audience because it controls the example and length. These are maintainer-written illustrations, not a claim that the student conducted an external experiment.

## Question 4

1. Classify `Service bahut slow thi, dobara nahi aaunga.` as positive, negative, or neutral. Return `Label: <label>` followed by one short explanatory sentence in plain English. Use a neutral analytical tone and base the answer only on the supplied review.
2. Write one friendly Hinglish Instagram caption for a home-cleaning service. Return only the caption, at most 20 words, with a short booking invitation. Avoid guarantees, invented prices, and more than two hashtags.

## Question 5

First verify the person's identity, scientific affiliation, and whether credible records attribute the inventions to that person. Search institutional researcher records and original patent records or peer-reviewed publications. If those checks do not establish the claim, say: `I cannot verify this person or these inventions from reliable evidence.` Confident wording is not evidence; generated text can contain invented names and claims. No external search or source verification is claimed here.

## Question 6

Text is converted into embedding vectors that encode learned similarities. A vector database indexes these vectors so a query can retrieve relevant source passages. The language model then uses those passages to draft an answer. An institute could index its class notes, retrieve matching sections for a student's question, and return an answer with note references, or admit when the notes do not contain the answer.

## Question 7

A text-only chatbot returns a response. An agent can choose and invoke tools, inspect their results, and continue toward a task. A tool is a defined operation, such as searching notes or reading a calendar. MCP provides a common protocol through which an AI application can discover and call connected tools and access data, subject to the host's permissions.

Example: an agent preparing a study plan reads the syllabus, checks the student's available time, proposes study blocks, and creates calendar events after the required authorization.

## Question 8

- Verify factual claims against reliable evidence.
- Keep private information out of unapproved services.
- Check for biased assumptions and unequal treatment.
- Have a person review consequential outputs.
- Acknowledge the sources and AI assistance used.
- Confirm the requested format, length, and constraints.
- Check code and calculations before relying on them.

I should not rely on an AI answer alone for a consequential decision. An answer without verifiable evidence needs further checking. Human expertise and original sources remain necessary when accuracy matters.
