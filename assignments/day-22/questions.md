# Day 22 Assignment

## Topic: Transformer Attention From Paper to Experiment

Complete the assignment in one folder named `solution` containing code, diagrams, and a research report.

This is a hard-level research assignment. You are expected to study transformer attention carefully and connect the theory to a working experiment. The assignment has only one question.

Recommended libraries:

```bash
python3 -m pip install numpy pandas matplotlib torch transformers
```

## Question 1: Explain, Implement, and Analyze Self-Attention

Research the self-attention mechanism used in transformer models. Then create a technical report and working notebook or Python script that explains attention mathematically and demonstrates it experimentally.

Your work must include:

1. a clear explanation of Query, Key, Value, scaled dot-product attention, softmax, and multi-head attention;
2. a from-scratch NumPy or PyTorch implementation of single-head scaled dot-product attention on a small toy sentence;
3. printed or plotted attention weights for at least three tokens;
4. an experiment using a pre-trained transformer model to inspect attention or hidden-state behavior on at least five carefully chosen sentences;
5. one ambiguity test, such as pronoun reference, negation, long-distance dependency, or word-order change;
6. a comparison between your toy implementation and the pre-trained model experiment;
7. a discussion of what attention visualizations can and cannot prove;
8. citations or links for at least three reliable sources you studied.

Your final report must answer this research question:

```text
How does self-attention help a transformer use context, and where can attention-based explanations become misleading?
```

## Submission

Submit your work in one folder:

```text
assignments/day-22/submissions/your-name/solution/
```

Include a `README.md` explaining how to run your code and reproduce your plots or tables.
