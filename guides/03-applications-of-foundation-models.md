# Domain 3: Applications of Foundation Models (28%)

This domain carries the most weight on the exam. Topics include FM-powered app design, **prompt engineering**, **training/fine-tuning** at a conceptual level, and **evaluation**. See [Domain 3](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain3.html) in the official guide.

---

## 3.1 Design considerations for FM applications

### Choosing a pre-trained model

Consider **cost**, **latency**, **modality**, **languages**, **context window**, **quality**, **licensing**, **customization** path, and whether you need **private** deployment options.

### Inference parameters (high level)

- **Temperature:** higher values increase randomness/creativity; lower values make outputs more deterministic/focused.
- **Max tokens / output length:** caps cost and runtime; may truncate answers.

### Retrieval Augmented Generation (RAG)

**RAG** pulls relevant documents or passages and conditions generation on them. That cuts dependence on whatever the model memorized during training and grounds answers in **your** content.

On AWS, **Amazon Bedrock Knowledge Bases** orchestrates ingestion, embeddings, retrieval, and integration with Bedrock models (exam-relevant pattern).

### Vector storage for embeddings

The exam guide explicitly mentions storing embeddings in **vector-capable** data services such as **Amazon OpenSearch Service**, **Amazon Aurora** / **RDS for PostgreSQL** with appropriate extensions, **Amazon Neptune**, and similar patterns. The key idea: **vector search** (similarity) + your governance model.

### Customization cost tradeoffs

| Approach                                    | Tradeoff summary                                                     |
| ------------------------------------------- | -------------------------------------------------------------------- |
| **In-context learning** (prompts, few-shot) | Fast to iterate; token cost; context limits                          |
| **RAG**                                     | Better grounding on private docs; needs solid retrieval and chunking |
| **Fine-tuning**                             | Can specialize behavior; needs curated data and MLOps discipline     |
| **Pre-training**                            | Extremely expensive; rarely relevant except conceptually             |

### Agents

**Agents** break problems into **multi-step** workflows: planning, tool use, retrieval, and execution. **Amazon Bedrock Agents** is the AWS-managed pattern; **agentic AI** and protocols like **Model Context Protocol (MCP)** appear as conceptual framing in the exam guide.

---

## 3.2 Prompt engineering techniques

### Building blocks

- **Instruction:** what the model should do.
- **Context:** background the model should use.
- **Negative prompts:** what to avoid (common in image models; also text constraints).
- **Prompt routing:** sending inputs to different models or prompts based on intent.

### Techniques

| Technique                  | Idea                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------------ |
| **Zero-shot**              | Instruction only, no examples                                                              |
| **One-shot / few-shot**    | Include examples to steer format and reasoning                                             |
| **Chain-of-thought (CoT)** | Ask the model to show intermediate reasoning steps (improves some tasks; increases tokens) |
| **Templates**              | Reusable prompts with variables for production consistency                                 |

### Best practices

Be **specific**, iterate with **evaluation**, use **guardrails** where appropriate, and version prompts like code.

### Risks

**Prompt injection**, **jailbreaking**, **data exposure** in prompts, and **poisoning** of retrieved content. Security (Domain 5) ties in here.

---

## 3.3 Training and fine-tuning (conceptual depth for the exam)

### Pre-training

Large-scale next-token or multimodal training on broad corpora; produces a **foundation model**.

### Fine-tuning and adaptation

- **Instruction tuning** aligns models with helpful, safe instruction following.
- **Domain adaptation** specializes behavior on industry language.
- **Transfer learning** reuses representations learned on one task for another.
- **RLHF** (reinforcement learning from human feedback) aligns models with human preferences (conceptual).

### Data preparation principles

Representative data, **label quality**, governance, rights to use data, and size appropriate to the method.

---

## 3.4 Evaluating foundation models and applications

### Methods

- **Human evaluation** for subjective quality and safety.
- **Benchmarks** for comparable scores on standard tasks.
- **Amazon Bedrock Model Evaluation** for comparing models and prompts in AWS workflows.

### Metrics (recognize names)

- **BLEU** / **ROUGE:** overlap-based text similarity (common in translation/summarization).
- **BERTScore:** semantic similarity using contextual embeddings.

### Business fit

Judge whether the system improves **productivity**, **engagement**, or task success, not only benchmark scores.

### Evaluating RAG and agents

Measure **retrieval precision**, answer faithfulness to sources, task completion for multi-step flows, and failure modes (wrong tool, bad retrieval).

---

## Hands-on tie-in

See:

- `examples/bedrock_converse.py`: inference parameters and messages API shape.
- `examples/bedrock_embeddings.py`: embeddings for retrieval-style designs.
- `examples/rag_similarity_concept.py`: cosine similarity for ranking chunks (learning aid).

---

## Quick self-check

1. Explain **RAG** in three sentences: problem it solves, mechanism, one AWS-aligned component name.
2. When would you **raise temperature** vs **lower** it for a support bot?
3. Name two risks that are **prompt-specific** vs two that are **retrieval-specific** in a RAG system.

---

## Further reading (AWS)

- [Prompt engineering concepts (Bedrock User Guide)](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-engineering-guidelines.html)
- [Knowledge Bases for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Model evaluation in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html)
