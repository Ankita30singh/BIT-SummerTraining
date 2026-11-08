# Core MEchanics - Next Word PRediction

The sky is ----

# LLM Train kaise hota hai ?

1. Pre-Training - poora internet padho agla shabd guess karo

2. Fine Tuning - ache examples s polish krna ( helful jawab dena )

3. RLHF ( Reinforcement learning from human feedback)

# Large ka matlv

baby-GPT - 5 sentence

GPT-2 - 1.5M Parameters

GPT-4, CLaude - poora inter, arbon parameters

.. emergent abilities ..

# LLM kya kya kar sakta hai ?

Generate, Summarize, Trnslate, Q&A, Code, Extract, Reasoning, Roleplay

# LLM ki limitations
Hallucinations, Knowledeg cut off, No True Understanding, Context limit

# Popular LLMs - Open Vs CLosed

CLosed - GPT, Claude, Gemini
Open - llama, mistral, deepseek, qwen

Tools - Ollama, Odysseus


# Token Kya hai ?

TOKEN = text ka chota tukda ( aksar ek sabd, ya sabd ka hissa)

LLM words nahi - TOKENS phadta hai aur likhta hai

" I love ChatGPT! " -> ["I", "love", "Chat", "G", "P", "T!"]

# Tokens Kyun ?

Characters -> bahut choote
WORDS - > rare sabd handi nahi kr sakte

TOKENS  -> Best of both , efficient

# Text -> TOken -> Number

"Hello" -> Tokenize -> ["Hello"] - > [15496]

Text -> Tokens -> numbers - model calculation - wapas text

# Token Facts

~4 character = 1 token  | ~75 words = 100 tokens

English - kam token

Hindi/Bhojpuri/emoji  - zayada tokens

# Context Window kya hai ?

CONTEXT WINDOW - ek baar mein LLM jitna TOKENS dekh sakta hai (memory limit)

Tumhara message + AI ka jawav + purani baatein

# Window bhar jaaye to ?

agar windo wbhar gaya -> purani baatein bhool jata hai. ( truncation )

GPT 3.5 ~ 4000 tokens ( ~ 3 pages)

GPT-4 ~8000-128000 tokens

Claude ~2000000 tokens ( ~500 pages)


# Context window - matter kyu krta hai ?

COST - zayad token = zayad paise

Long Document - poora documnet window mein aana chahiye

Memory - lambi baat meirn pura bhool jata hai

RAG - isi limit ka smart solution
