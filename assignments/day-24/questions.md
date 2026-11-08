# Day 24 Assignment

## Topic: Prompting, Fine-Tuning, and Adaptation Strategy

Complete the assignment in one folder named `solution` containing experiments, comparison tables, and a research report.

This is a hard-level research assignment. You are expected to investigate when prompt engineering is enough and when model adaptation may be justified. The assignment has only one question.

Recommended libraries:

```bash
python3 -m pip install pandas scikit-learn torch transformers datasets
```

Fine-tuning is optional if your computer cannot support it. If you cannot fine-tune locally, you must still design the fine-tuning plan and run a strong baseline experiment.

## Question 1: Compare Prompting With Model Adaptation

Choose one task, such as sentiment classification, FAQ answering, summarization, intent classification, or extraction from structured text. Research and compare at least three ways to solve it:

1. zero-shot prompting or direct model use;
2. few-shot prompting or retrieval-assisted prompting;
3. fine-tuning, parameter-efficient fine-tuning, or a detailed adaptation plan if training is not feasible.

Your work must include:

1. a small evaluation dataset with at least 50 labelled examples or a documented public benchmark subset;
2. an explanation of the task, labels, success metric, and failure cost;
3. baseline results for at least two approaches you actually run;
4. an adaptation design for the third approach, including data requirements, compute needs, expected cost, and risk;
5. qualitative error analysis on at least 10 failed or difficult examples;
6. a comparison table covering accuracy or quality, cost, latency, maintainability, privacy, and reproducibility;
7. a recommendation for a real classroom or business scenario;
8. citations or links for at least three sources that informed your approach.

Your final report must answer this research question:

```text
For your chosen task, is prompting sufficient, or is model adaptation justified? Defend your answer with evidence, cost, and risk analysis.
```

## Submission

Submit your work in one folder:

```text
assignments/day-24/submissions/your-name/solution/
```

Include a `README.md` explaining how to run the experiments and where the dataset came from.
