import torch
from transformers import pipeline, set_seed


# Question 1: Select CPU or GPU


device = 0 if torch.cuda.is_available() else -1

print("Question 1")
print("CUDA Available:", torch.cuda.is_available())

if device == 0:
    print("Using: GPU")
else:
    print("Using: CPU")

# The program works on both CPU and GPU.
# If a GPU is unavailable, Hugging Face automatically runs
# the model on the CPU, making the program portable.


# Question 2: Create a Sentiment Pipeline


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

for text in texts:
    print(f"\nInput: {text}")
    print(sentiment(text))


# Question 3: Analyze a Batch of Reviews


reviews = [
    "Best decision ever!",
    "I want a refund.",
    "It was okay, nothing special.",
]

results = sentiment(reviews)

print("\nQuestion 3")

for review, result in zip(reviews, results):
    print(f"{review} -> {result['label']} | score {result['score']:.3f}")


# Question 4: Examine an Unclear Input


print("\nQuestion 4")

unclear = "Blah blah lorem ipsum."
result = sentiment(unclear)[0]

print("Input:", unclear)
print("Label:", result["label"])
print("Confidence Score:", round(result["score"], 3))

# A high confidence score does not guarantee correctness.
# The model may confidently classify meaningless or unfamiliar
# text because it always tries to predict the closest label
# learned during training.


# Question 5: Create a Text Generation Pipeline


generator = pipeline(
    "text-generation",
    model="openai-community/gpt2",
    device=device,
)

print("\nQuestion 5")

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


# Question 6: Generate From Several Prompts


prompts = [
    "In the future, students will",
    "The best way to learn coding is",
    "Gorakhpur is famous for",
]

print("\nQuestion 6")

set_seed(42)

for prompt in prompts:
    print("\n" + "=" * 50)
    print("Prompt:", prompt)

    output = generator(
        prompt,
        max_new_tokens=25,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
        pad_token_id=generator.tokenizer.eos_token_id,
    )

    print("Generated Text:")
    print(output[0]["generated_text"])

# Generated text is produced by the model and may contain
# inaccurate information. It should not be treated as verified fact.


# Question 7: Compare Temperature Settings


print("\nQuestion 7")

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

print("\nTemperature = 0.3")
print(low_temp[0]["generated_text"])

print("\nTemperature = 1.2")
print(high_temp[0]["generated_text"])

# Lower temperature usually produces more predictable,
# focused, and consistent output.
#
# Higher temperature usually produces more varied,
# creative, and sometimes less coherent output.


# Question 8: Compare Sampling With Greedy Generation


print("\nQuestion 8")

greedy = generator(
    prompt,
    max_new_tokens=25,
    do_sample=False,
    pad_token_id=generator.tokenizer.eos_token_id,
)

print(greedy[0]["generated_text"])

# Greedy generation always selects the most probable next token,
# making the output more repeatable than sampling, which introduces
# randomness by selecting from multiple possible tokens.


# Question 9: Reflection


# 1. Generated facts should always be verified because language
#    models can produce incorrect or outdated information.
#
# 2. Bias in the training data may influence responses and
#    produce unfair or unbalanced outputs.
#
# 3. Model downloads may be difficult on a slow connection
#    because model files can be hundreds of megabytes in size.
#
# 4. CPU generation is usually slower because CPUs have fewer
#    parallel processing cores than GPUs for deep learning tasks.
#
# 5. Private or sensitive information should never be entered
#    into an unapproved AI system because it may create privacy
#    or security risks.

print("\nPre-trained model output should always be reviewed and verified by a human before it is trusted or used.")