# Domain 2: Fundamentals of GenAI (24%)

Generative AI shows up heavily on the AWS AI Practitioner exam. This chapter follows [Domain 2](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain2.html) in the official guide.

---

## 2.1 Core GenAI concepts

### Tokens

Models process text as **tokens** (subword pieces). Pricing, latency, and context limits are usually expressed in tokens, not raw character counts.

### Chunking

For long documents, **chunking** splits text into segments that fit context windows and feed retrieval or summarization pipelines.

### Embeddings and vectors

An **embedding** is a dense numeric vector representing text, images, or other inputs. Similar meanings tend to map to nearby vectors, which powers **semantic search** and **RAG**.

### Prompt engineering

Crafting instructions, examples, and constraints so a model produces reliable outputs. See Domain 3 for techniques (few-shot, chain-of-thought, etc.).

### Transformers and foundation models (FMs)

**Transformer** architectures enabled large-scale pre-training on broad data. A **foundation model** is a large model pre-trained for general capabilities, then adapted (prompting, fine-tuning, tools) to specific tasks.

### Modalities and diffusion

- **Multimodal models** accept or produce more than one modality (text + image).
- **Diffusion models** are a common family for image/audio generation (iterative denoising).

### Foundation model lifecycle (conceptual)

**Data selection → model selection → pre-training → adaptation (fine-tuning / prompting) → evaluation → deployment → feedback loops.**

---

## 2.2 Capabilities, limits, and selection criteria

### Advantages of GenAI

- **Adaptability** across tasks with prompting and light integration.
- **Rapid prototyping** of assistants, summarization, drafting, and code help.
- **Developer productivity** when used with review and tests.

### Disadvantages and risks

- **Hallucinations:** plausible but false outputs.
- **Nondeterminism:** temperature and sampling change outputs run-to-run.
- **Interpretability:** hard to audit internal reasoning.
- **Compliance:** data handling, IP, and licensing constraints.

### Selection factors (exam-style)

Latency, cost, **context length**, modality (text vs image), **multilingual** needs, **fine-tuning** or **private customization** requirements, regional availability, and organizational policies.

### Business metrics

Examples: conversion rate, average handle time, customer satisfaction, revenue per user, defect rate in generated content (human review burden).

---

## 2.3 AWS for GenAI applications

### Services to recognize (not exhaustive)

| Need                                    | Typical AWS building blocks                          |
| --------------------------------------- | ---------------------------------------------------- |
| Managed FM access                       | **Amazon Bedrock**                                   |
| Experimentation / UI prototyping        | **Amazon Bedrock PartyRock** (conceptual playground) |
| Pre-built models & notebooks            | **Amazon SageMaker JumpStart**                       |
| Enterprise Q&A on company data          | **Amazon Q Business**                                |
| Developer assistance in the IDE         | **Amazon Q Developer**                               |
| AWS-native multimodal foundation models | **Amazon Nova** (family name in exam scope)          |

### Why teams use AWS GenAI services

You get security and compliance options, **IAM** integration, encryption, VPC patterns, regional footprint, and managed operations (less undifferentiated work for your team). You still pay for it: **cost tradeoffs** (token pricing, provisioned throughput, redundancy) matter.

### Cost tradeoffs (conceptual)

- **On-demand token** usage vs **provisioned throughput** for steady traffic.
- **Higher availability / multi-AZ** patterns vs cost.
- **Larger / more capable models** vs latency and price per request.

---

## Quick self-check

1. Define **embedding** in your own words and give one use case.
2. Name two disadvantages of GenAI that matter in **regulated** industries.
3. For **Bedrock**, **Q Business**, and **JumpStart**, assign each one: **managed FM consumption**, **enterprise knowledge assistant**, or **ML hub with pre-trained models**.

---

## Further reading (AWS)

- [What Is Amazon Bedrock?](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
- [Amazon Q Business](https://aws.amazon.com/q/business/)
- [PartyRock (Amazon Bedrock)](https://partyrock.aws/)
