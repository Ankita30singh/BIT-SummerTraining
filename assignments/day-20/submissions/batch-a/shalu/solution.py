import torch
from transformers import pipeline, set_seed
### Question 1: Select CPU or GPU

"""Create:

```python
device = 0 if torch.cuda.is_available() else -1
```

Print:

1. whether CUDA is available;
2. `GPU` when `device == 0`, otherwise `CPU`.

Add a comment explaining why the same program should still work when a GPU is unavailable."""
device = 0 if torch.cuda.is_available() else -1
print("CUDA Available:", torch.cuda.is_available())
print("Device:", "GPU" if device == 0 else "CPU")

# If a GPU is unavailable, the program automatically uses the CPU, so it can still run on any computer.

### Question 2: Create a Sentiment Pipeline

"""Create:

```python
sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=device,
)
```

Analyze and print the complete result for:

```text
This course is absolutely amazing!
The service was terrible and slow.
```"""
sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=device,
)
texts = [
    "This course is absolutely amazing!",
    "The service was terrible and slow.",
]

for text in texts:
    result = sentiment(text)
    print(text)
    print(result)

### Question 3: Analyze a Batch of Reviews

"""Use:

```python
reviews = [
    "Best decision ever!",
    "I want a refund.",
    "It was okay, nothing special.",
]
```

Pass the full list to the pipeline in one call.

For each review, print:

```text
<review> -> <label> | score <score rounded to 3 decimals>
```"""
reviews = [
    "Best decision ever!",
    "I want a refund.",
    "It was okay, nothing special.",
]

results = sentiment(reviews)

for review, result in zip(reviews, results):
    print(f"{review} -> {result['label']} | score {result['score']:.3f}")

### Question 4: Examine an Unclear Input

"""Analyze:

```text
Blah blah lorem ipsum.
```

Print its label and confidence score.

In comments, explain why a high confidence score does not prove that a meaningless or out-of-domain input was understood correctly."""
text = "Blah blah lorem ipsum."

result = sentiment(text)[0]

print("Label:", result["label"])
print("Confidence:", round(result["score"], 3))

# A high confidence score does not guarantee that the model understood meaningless or unfamiliar text correctly.
# The model still predicts based on patterns learned during training.

### Question 5: Create a Text-Generation Pipeline

"""Create:

```python
generator = pipeline(
    "text-generation",
    model="openai-community/gpt2",
    device=device,
)
```

Set the seed to `42` and generate from:

```text
Artificial Intelligence will
```

Use:

```python
max_new_tokens=25
do_sample=True
temperature=0.8
top_p=0.95
pad_token_id=generator.tokenizer.eos_token_id
```

Print the generated text."""
generator = pipeline(
    "text-generation",
    model="openai-community/gpt2",
    device=device,
)
set_seed(42)

output = generator(
    "Artificial Intelligence will",
    max_new_tokens=25,
    do_sample=True,
    temperature=0.8,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print(output[0]["generated_text"])

### Question 6: Generate From Several Prompts

"""Generate text from:

```python
prompts = [
    "In the future, students will",
    "The best way to learn coding is",
    "Gorakhpur is famous for",
]
```

Reset the seed to `42` before the loop. Print every prompt and generated result with clear separators.

Generated text may contain inaccurate information. Do not present it as verified fact."""
prompts = [
    "In the future, students will",
    "The best way to learn coding is",
    "Gorakhpur is famous for",
]
set_seed(42)

for prompt in prompts:
    print("-" * 50)
    print("Prompt:", prompt)

    result = generator(
        prompt,
        max_new_tokens=25,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
        pad_token_id=generator.tokenizer.eos_token_id,
    )

    print(result[0]["generated_text"])

### Question 7: Compare Temperature Settings

"""Using the same prompt and resetting the seed before each call, generate once with:

```text
temperature = 0.3
```

and once with:

```text
temperature = 1.2
```

Keep `do_sample=True`, `top_p=0.95`, and `max_new_tokens=25`.

Print both results and add comments describing which output appears more predictable and which appears more varied. Exact wording is not graded."""
prompt = "Artificial Intelligence will"

set_seed(42)

low_temp = generator(
    prompt,
    max_new_tokens=25,
    do_sample=True,
    temperature=0.3,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)

set_seed(42)

high_temp = generator(
    prompt,
    max_new_tokens=25,
    do_sample=True,
    temperature=1.2,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print("Temperature = 0.3")
print(low_temp[0]["generated_text"])

print("\nTemperature = 1.2")
print(high_temp[0]["generated_text"])

# Lower temperature generally produces more predictable text.
# Higher temperature usually produces more creative and varied text.

### Question 8: Compare Sampling With Greedy Generation

"""Generate from the same prompt using:

```text
do_sample = False
```

Do not pass `temperature` or `top_p` in this call.

Print the result and explain in comments why greedy generation is usually more repeatable than sampled generation."""
greedy = generator(
    prompt,
    max_new_tokens=25,
    do_sample=False,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print(greedy[0]["generated_text"])

# Greedy generation always selects the most likely next token, making it more repeatable than random sampling.
### Question 9: Write a Limitations Reflection

"""Add comments answering:

1. Why should generated facts be verified?
2. How could training-data bias affect an output?
3. Why can model downloads be difficult on a slow connection?
4. Why might CPU generation be slower than GPU generation?
5. Why should private information not be placed into an unapproved AI system?

Print one final sentence explaining that pre-trained model output still requires human review."""
#--------------------------------------------------
# 1. Generated facts should always be verified because AI can produce incorrect information.

# 2. Bias in the training data can influence the model's responses.

# 3. Downloading models may take a long time on a slow internet connection.

# 4. CPUs process deep learning models more slowly than GPUs because GPUs are optimized for parallel computation.

# 5. Private or sensitive information should never be shared with an unapproved AI system to protect privacy and security.
print("Pre-trained model output should always be reviewed by a human before being trusted.")