import torch
from transformers import pipeline, set_seed


# Question 1: Select CPU or GPU

device = 0 if torch.cuda.is_available() else -1

print("CUDA Available:", torch.cuda.is_available())

if device == 0:
    print("Running on: GPU")
else:
    print("Running on: CPU")


# The same program works without GPU because it automatically switches to CPU.
# This makes the code usable on different systems.



# Question 2: Create a Sentiment Pipeline

sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=device,
)


sentences = [
    "This course is absolutely amazing!",
    "The service was terrible and slow."
]


print("\nSentiment Analysis Results:")

for sentence in sentences:
    result = sentiment(sentence)
    print(sentence)
    print(result)



# Question 3: Analyze a Batch of Reviews

reviews = [
    "Best decision ever!",
    "I want a refund.",
    "It was okay, nothing special.",
]


batch_results = sentiment(reviews)

print("\nBatch Review Analysis:")

for review, result in zip(reviews, batch_results):
    print(
        f"{review} -> {result['label']} | score {result['score']:.3f}"
    )



# Question 4: Examine an Unclear Input

unclear_result = sentiment(
    "Blah blah lorem ipsum."
)


print("\nUnclear Input Result:")

print(
    unclear_result[0]["label"],
    "| score",
    round(unclear_result[0]["score"], 3)
)


# A high confidence score does not guarantee that the model understood
# meaningless or out-of-domain text correctly. It may still make a prediction
# based on patterns learned during training.



# Question 5: Create Text Generation Pipeline

generator = pipeline(
    "text-generation",
    model="openai-community/gpt2",
    device=device,
)


set_seed(42)

generated_text = generator(
    "Artificial Intelligence will",
    max_new_tokens=25,
    do_sample=True,
    temperature=0.8,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)


print("\nGenerated Text:")
print(generated_text[0]["generated_text"])



# Question 6: Generate From Several Prompts

prompts = [
    "In the future, students will",
    "The best way to learn coding is",
    "Gorakhpur is famous for",
]


print("\nMultiple Prompt Generation:")

set_seed(42)

for prompt in prompts:

    result = generator(
        prompt,
        max_new_tokens=25,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
        pad_token_id=generator.tokenizer.eos_token_id,
    )

    print("\n-----------------------")
    print("Prompt:", prompt)
    print("Generated:")
    print(result[0]["generated_text"])


# Generated text may contain incorrect information.
# It should be verified before treating it as a fact.



# Question 7: Compare Temperature Settings

prompt = "Artificial Intelligence will"


set_seed(42)

low_temperature = generator(
    prompt,
    max_new_tokens=25,
    do_sample=True,
    temperature=0.3,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)


set_seed(42)

high_temperature = generator(
    prompt,
    max_new_tokens=25,
    do_sample=True,
    temperature=1.2,
    top_p=0.95,
    pad_token_id=generator.tokenizer.eos_token_id,
)


print("\nTemperature 0.3 Output:")
print(low_temperature[0]["generated_text"])


print("\nTemperature 1.2 Output:")
print(high_temperature[0]["generated_text"])


# Lower temperature usually produces more predictable and focused text.
# Higher temperature produces more diverse and creative text.



# Question 8: Compare Sampling With Greedy Generation

greedy_result = generator(
    prompt,
    max_new_tokens=25,
    do_sample=False,
    pad_token_id=generator.tokenizer.eos_token_id,
)


print("\nGreedy Generation Output:")
print(greedy_result[0]["generated_text"])


# Greedy generation always selects the highest probability next token,
# so it is usually more repeatable than sampled generation.
# Sampling allows randomness and can create different outputs.



# Question 9: Limitations Reflection

# Generated facts should be verified because models can produce incorrect
# or outdated information that sounds believable.

# Training-data bias can affect outputs because the model may learn
# unfair patterns or stereotypes from its training data.

# Model downloads can be difficult on slow connections because models
# are large files that require significant bandwidth and storage.

# CPU generation can be slower than GPU generation because GPUs perform
# many mathematical operations in parallel.

# Private information should not be placed into unapproved AI systems
# because it may create privacy and security risks.


print(
    "\nPre-trained model output still requires human review before final use."
)