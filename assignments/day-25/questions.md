# Day 25 Assignment

## Topic: AI Agents, Tool Use, and Reliability Benchmarking

Complete the assignment in one folder named `solution` containing code, test cases, logs, and a research report.

This is a hard-level research assignment. You are expected to study agent workflows, define reliability tests, and measure failures instead of only showing a successful demo. The assignment has only one question.

Recommended libraries:

```bash
python3 -m pip install pandas pydantic requests rich
```

You may use local rule-based agents, public APIs, or model APIs approved by your instructor. Do not place private keys or private data in the repository.

## Question 1: Design and Benchmark a Tool-Using AI Agent

Build or simulate an AI agent that can solve tasks by choosing from at least three tools. Example tools include calculator, search over local notes, CSV analyzer, weather mock API, file summarizer, unit converter, or task planner.

Your work must include:

1. a clear agent architecture diagram or text flow showing inputs, planner, tool calls, observations, and final answer;
2. at least three implemented tools with strict input and output schemas;
3. at least 20 benchmark tasks, including easy, medium, hard, and trick tasks;
4. logs showing tool choices, arguments, observations, and final answers;
5. reliability metrics, such as task success rate, invalid tool-call rate, hallucinated answer rate, and average number of tool calls;
6. at least five failure cases with root-cause analysis;
7. guardrails for unsafe, impossible, private, or out-of-scope requests;
8. a recommendation for improving the agent before real use.

Your final report must answer this research question:

```text
How reliable is your tool-using agent under realistic and adversarial tasks, and what changes are needed before it can be trusted?
```

## Submission

Submit your work in one folder:

```text
assignments/day-25/submissions/your-name/solution/
```

Include a `README.md` explaining how to run the benchmark and inspect the logs.
