# Domain 4: Guidelines for Responsible AI (14%)

Responsible AI is not a separate "ethics add-on." It is how you limit harm, keep trust, and meet what stakeholders expect. Objectives follow [Domain 4](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain4.html).

---

## 4.1 Building responsible AI systems

### Pillars to recognize

- **Fairness and bias:** systematic skew that disadvantages groups.
- **Inclusivity:** datasets and evaluation cover diverse users and edge cases.
- **Robustness:** stable behavior under noise, typos, and adversarial prompts.
- **Safety:** preventing harmful outputs and unsafe recommendations.
- **Veracity:** truthfulness and grounding; related to hallucination risk.

### AWS tools (exam examples)

- **Amazon Bedrock Guardrails:** policy controls on prompts and completions (topics, denied content, sensitive information handling; you configure details to match your requirements).
- **Amazon SageMaker Clarify:** bias and explainability analysis for ML workflows.
- **SageMaker Model Monitor:** drift and quality monitoring in production.
- **Amazon Augmented AI (A2I):** human review workflows when automation is insufficient.

### Model selection with responsibility in mind

Consider **environmental impact** and **sustainability**: larger models consume more energy; right-size models for the task.

### Legal and reputational risks in GenAI

- **Intellectual property** disputes around training data and outputs.
- **Discriminatory outputs** and loss of trust.
- **End-user harm** from bad advice in sensitive domains.
- **Hallucinations** presented as facts.

### Data characteristics

**Diversity**, **balance**, **curation**, and **provenance** matter. Garbage or biased data produces garbage or biased behavior.

### Bias vs variance (effects)

- **Bias:** wrong assumptions; can underperform for entire subgroups.
- **Variance:** overfitting to noise; unstable generalization.

---

## 4.2 Transparency and explainability

### Transparent vs opaque

Some models and workflows allow clearer **feature attribution** or documented behavior; deep LLMs are often **partially opaque**. The exam expects you to understand **tradeoffs**: stronger safety filters or proprietary models may reduce inspectability.

### Tools and artifacts

- **SageMaker Model Cards:** document model details, limitations, and evaluation results.
- **Open models and licenses:** transparency into weights may be higher, but operational burden and compliance review still apply.

### Human-centered design

Explain outputs in ways users can **act on**: confidence cues, citations (for RAG), escalation paths, and clear capability limits.

---

## Quick self-check

1. Give one example each of **bias** risk and **robustness** risk in a customer chatbot.
2. Name two AWS services/tools from the exam guide used for **bias detection/monitoring** or **human review**.
3. What is the purpose of a **model card**?

---

## Further reading (AWS)

- [Responsible AI (AWS)](https://aws.amazon.com/machine-learning/responsible-ai/)
- [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [Amazon SageMaker Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-fairness-and-explainability.html)
