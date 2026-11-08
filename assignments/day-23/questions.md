# Day 23 Assignment

## Topic: Responsible AI Bias, Privacy, and Risk Audit

Complete the assignment in one folder named `solution` containing analysis code, evidence, and an audit report.

This is a hard-level research assignment. You are expected to choose a public dataset or model behavior to audit, compute evidence, and write a careful risk assessment. The assignment has only one question.

Recommended libraries:

```bash
python3 -m pip install pandas numpy scikit-learn matplotlib seaborn
```

## Question 1: Conduct a Responsible AI Audit

Choose one public dataset, public model, or AI workflow and perform a responsible AI audit. Your audit must examine fairness, privacy, transparency, and deployment risk. You may audit a classification dataset, a text-generation workflow, a recommendation example, or a course-approved AI system.

Your work must include:

1. a short description of the system or dataset and who may be affected by it;
2. a data sheet or model card summary using your own words;
3. at least three measurable audit checks, such as missing-value patterns, label imbalance, group performance differences, toxicity examples, prompt sensitivity, or privacy leakage risk;
4. at least two visualizations or tables that support your findings;
5. a section distinguishing evidence-based findings from assumptions;
6. a discussion of privacy concerns, including what data should not be collected or submitted to an AI system;
7. a mitigation plan with at least five concrete actions;
8. a final risk rating: low, medium, high, or critical, with justification.

Your final report must answer this research question:

```text
What are the most important responsible AI risks in your chosen system, and what evidence-based mitigations should be applied before deployment?
```

## Submission

Submit your work in one folder:

```text
assignments/day-23/submissions/your-name/solution/
```

Include a `README.md` explaining your data source, setup steps, and how to reproduce your audit.
