# LLM Train Kaise hote hai ?

1. PRE-Training -> Poore internet s phadhna, agla shabd predict karna
2. Fine-Tuning -> Ache Examples s polish (helpful Jawab dena)
3. RLHF -> instant Feedback se seekhna kaunda jawab acha hai  ( Reinforcement Learning From Human Feedback)

# Large ka matlab - Scale ka kamal
Data + Network - > Itna data s train hojana ki reasoning, translation, coding -> emergent Abilities

# LLM kya kya kr sakta hai

Generate, Summarize, Translate, Q&A, COde, Extract, Reasoning, Roleplay

# LLM ki limitations
Hallucination, Knowledge CUtoff, , NO True Understanding, Context Limit

# Popular LLM + Open and CLosed

CLosed -> GPT, CLuade, Gemini

Open -> Llama, Mistral, GPT-2

## Olama, Odysseus

# Token Kya hai ?

TOKEN = text ka choota tukda

LLM shabd nahi - Tokens padhta hai aur likhta hai

1 token = the

" I love CHATGPT!" -> ["I","love","Chat", "G", "PT", "!"]

# Tokens Kyun ?

Characters -> Bahut chota, dheema

WORDS -> rare shabd , new words

TOKENS -> BEst of both: koi bhi shabd, efficient

Text -> TOkens - >numbers -> model calculation -> wapas text


# Token Facts - HIndi > ENglish
~ 4 characters = 1 token | ~75 words = 100 tokens

English -> effcient ( kam tokens)

Hindi/Bhojpuri/Emoji -> zayada tokken -> Tokenizer English Optimized

# Context WIndow kya hai ?

CONTEXT WINDOW = ek baar mein LLM jitne TOKENS dekh sakta hai

tumhara mesage + AI ka jawab hota  + Purani Baate

# Window se bahar jaaye too ? + Sizes

Window bahar gaya - Purani baatein bhool jata hai ( truncation)

GPT 3.5  ~ 4000 tokens ( ~ 3 pages)
 GPT 4 ~ 8000-128000. tokens
CLaude ~ 200,000 tokems ( ~500 pages)

# Why ( Tokens + Context Window) Matter ?

COST - zayada token - zaya paisa

Long Document -> poora document window mein aana chahiye

Memory - >? lambi baat mein puran bhool jana

RAG - isi limit ka smart solution