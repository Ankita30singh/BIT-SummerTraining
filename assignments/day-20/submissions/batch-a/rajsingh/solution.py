import torch
from transformers import pipeline, set_seed

# Question 1: Select CPU or GPU


device = 0 if torch.cuda.is_available() else -1

print("CUDA Available:", torch.cuda.is_available())

if device == 0:
    print("Device: GPU")
else:
    print("Device: CPU")

# The same program works on CPU if a GPU is not available.


# Question 2: Create Sentiment Pipeline


sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=device,
)

print("\nQuestion 2")

texts = [
    "This course is absolutely amazing!",
    "The service was terrible and slow.",
]

results = sentiment(texts)

for text, result in zip(texts, results):
    print(text)
    print(result)


# Question 3: Analyze Batch of Reviews


print("\nQuestion 3")

reviews = [
    "Best decision ever!",
    "I want a refund.",
    "It was okay, nothing special.",
]

batch = sentiment(reviews)

for review, result in zip(reviews, batch):
    print(f"{review} -> {result['label']} | score {result['score']:.3f}")

# Question 4: Unclear Input


print("\nQuestion 4")

result = sentiment("Blah blah lorem ipsum.")[0]

print("Label:", result["label"])
print("Score:", round(result["score"], 3))

# A high confidence score does not always mean the model
# understood meaningless or unknown text correctly.

# Question 5: Text Generation Pipeline


generator = pipeline(
    "text-generation",
    model="openai-community/gpt2",
    device=device,
)

set_seed(42)

print("\nQuestion 5")

output = generator(
    "Artificial Intelligence will",
    max_new_tokens=25,
    do_sample=True,
    temperature=0.8,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print(output[0]["generated_text"])

# Question 6: Multiple Prompts


print("\nQuestion 6")

prompts = [
    "In the future, students will",
    "The best way to learn coding is",
    "Gorakhpur is famous for",
]

set_seed(42)

for prompt in prompts:
    print("-" * 50)
    print("Prompt:", prompt)

    text = generator(
        prompt,
        max_new_tokens=25,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
        pad_token_id=generator.tokenizer.eos_token_id,
    )

    print(text[0]["generated_text"])

# Generated text may contain incorrect information.
# Do not treat it as verified fact.


# Question 7: Temperature Comparison


print("\nQuestion 7")

prompt = "Artificial Intelligence will"

set_seed(42)

low = generator(
    prompt,
    max_new_tokens=25,
    do_sample=True,
    temperature=0.3,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)

set_seed(42)

high = generator(
    prompt,
    max_new_tokens=25,
    do_sample=True,
    temperature=1.2,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print("\nTemperature = 0.3")
print(low[0]["generated_text"])

print("\nTemperature = 1.2")
print(high[0]["generated_text"])

# Lower temperature gives more predictable output.
# Higher temperature gives more creative and varied output.

# Question 8: Greedy Generation


print("\nQuestion 8")

greedy = generator(
    prompt,
    max_new_tokens=25,
    do_sample=False,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print(greedy[0]["generated_text"])

# Greedy generation always chooses the most likely next token,
# so it is more repeatable than random sampling.

# Question 9: Reflection


# 1. Generated facts should always be verified because the model
#    can produce incorrect or outdated information.
#
# 2. Bias in training data can affect the model's responses.
#
# 3. Large model files take time to download on a slow internet connection.
#
# 4. CPU generation is slower because it performs fewer operations
#    in parallel compared to a GPU.
#
# 5. Private information should not be shared with an unapproved
#    AI system because it may risk privacy and security.

print("\nPre-trained model output should always be reviewed by a human before use.")