# Day 21 Assignment

## Topic: Research-Grade Retrieval-Augmented Generation Evaluation

Complete the assignment in one folder named `solution` containing code, data notes, and a short report.

This is a hard-level research assignment. You are expected to read documentation, compare methods, run experiments, and explain your decisions. The assignment has only one question.

Recommended libraries:

```bash
python3 -m pip install pandas scikit-learn sentence-transformers faiss-cpu rank-bm25
```

You may use different libraries if you explain why.

## Question 1: Build and Evaluate a Small RAG System

Create a retrieval-augmented generation research prototype for a knowledge base of at least 20 documents. The documents may come from public documentation, research paper abstracts, course notes, or another clearly cited source. Do not use private or copyrighted material unless you have permission.

Your work must include:

1. a document collection with source notes and clean chunking rules;
2. at least two retrieval methods, such as BM25, TF-IDF, sentence-transformer embeddings, or FAISS vector search;
3. at least 12 test questions whose answers are present in the document collection;
4. retrieval metrics, including top-1 accuracy, top-3 accuracy, and a short error analysis;
5. generated or drafted final answers with citations to the retrieved chunks;
6. a comparison table explaining which retrieval method worked better and why;
7. one ablation experiment, such as changing chunk size, embedding model, query wording, or number of retrieved chunks;
8. a limitations section covering hallucination risk, missing documents, weak citations, and evaluation bias.

Your final report must answer this research question:

```text
Which retrieval design gives the most reliable grounded answers for your chosen document collection, and what evidence supports your conclusion?
```

## Submission

Submit your work in one folder:

```text
assignments/day-21/submissions/your-name/solution/
```

Include a `README.md` explaining how to run your code and reproduce your results.
