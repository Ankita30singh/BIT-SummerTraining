import torch
from transformers import pipeline, set_seed

# ==========================================================
# Question 1: Select CPU or GPU
# ==========================================================

# Use GPU if CUDA is available, otherwise use CPU.
device = 0 if torch.cuda.is_available() else -1

print("========== Question 1 ==========")
print("CUDA Available:", torch.cuda.is_available())

if device == 0:
    print("Using: GPU")
else:
    print("Using: CPU")

# The program works on both GPU and CPU.
# If a GPU is unavailable, Transformers automatically runs on the CPU,
# making the code portable across different computers.

# ==========================================================
# Question 2: Create a Sentiment Pipeline
# ==========================================================

print("\n========== Question 2 ==========")

sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=device,
)

text1 = "This course is absolutely amazing!"
text2 = "The service was terrible and slow."

print(sentiment(text1))
print(sentiment(text2))

# ==========================================================
# Question 3: Analyze a Batch of Reviews
# ==========================================================

print("\n========== Question 3 ==========")

reviews = [
    "Best decision ever!",
    "I want a refund.",
    "It was okay, nothing special.",
]

results = sentiment(reviews)

for review, result in zip(reviews, results):
    print(f"{review} -> {result['label']} | score {result['score']:.3f}")

# ==========================================================
# Question 4: Examine an Unclear Input
# ==========================================================

print("\n========== Question 4 ==========")

unclear_text = "Blah blah lorem ipsum."

result = sentiment(unclear_text)[0]

print("Text:", unclear_text)
print("Label:", result["label"])
print("Confidence:", round(result["score"], 3))

# A high confidence score does NOT guarantee that the model
# truly understands meaningless or unfamiliar text.
# The model always predicts based on patterns learned during training,
# even for inputs that have little or no real meaning.

# ==========================================================
# Question 5: Create a Text-Generation Pipeline
# ==========================================================

print("\n========== Question 5 ==========")

generator = pipeline(
    "text-generation",
    model="openai-community/gpt2",
    device=device,
)

set_seed(42)

generated = generator(
    "Artificial Intelligence will",
    max_new_tokens=25,
    do_sample=True,
    temperature=0.8,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print(generated[0]["generated_text"])

# ==========================================================
# Question 6: Generate From Several Prompts
# ==========================================================

print("\n========== Question 6 ==========")

prompts = [
    "In the future, students will",
    "The best way to learn coding is",
    "Gorakhpur is famous for",
]

set_seed(42)

for prompt in prompts:
    print("-" * 60)
    print("Prompt:")
    print(prompt)

    output = generator(
        prompt,
        max_new_tokens=25,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
        pad_token_id=generator.tokenizer.eos_token_id,
    )

    print("\nGenerated Text:")
    print(output[0]["generated_text"])

# Generated text is produced by a language model and
# should not be treated as verified factual information.

# ==========================================================
# Question 7: Compare Temperature Settings
# ==========================================================

print("\n========== Question 7 ==========")

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

# Lower temperature generally produces more predictable,
# focused, and consistent text.
#
# Higher temperature usually creates more varied and creative
# outputs but may also produce less accurate or less coherent text.

# ==========================================================
# Question 8: Compare Sampling With Greedy Generation
# ==========================================================

print("\n========== Question 8 ==========")

greedy = generator(
    prompt,
    max_new_tokens=25,
    do_sample=False,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print(greedy[0]["generated_text"])

# Greedy generation always selects the most likely next token,
# making the output more repeatable.
#
# Sampled generation introduces randomness, so different runs
# can produce different outputs even from the same prompt.

# ==========================================================
# Question 9: Write a Limitations Reflection
# ==========================================================

print("\n========== Question 9 ==========")
print("Pre-trained model output should always be reviewed and verified by humans.")

# Why should generated facts be verified?
# Language models can generate incorrect, outdated,
# or completely fabricated information.

# How could training-data bias affect an output?
# If the training data contains bias, stereotypes,
# or uneven representation, the model may reflect those patterns.

# Why can model downloads be difficult on a slow connection?
# Pre-trained models are often hundreds of megabytes or several gigabytes,
# so downloading them may take a long time or fail on slow networks.

# Why might CPU generation be slower than GPU generation?
# GPUs perform many calculations in parallel, making deep-learning
# inference much faster than CPUs.

# Why should private information not be placed into an unapproved AI system?
# Sensitive or confidential information could be exposed or processed
# in ways that do not meet privacy or security requirements.
