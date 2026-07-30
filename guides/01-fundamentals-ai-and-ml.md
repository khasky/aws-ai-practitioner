# Domain 1: Fundamentals of AI and ML (20%)

This domain covers vocabulary and the ML lifecycle; later domains assume you know these terms. Objectives match the **AWS Certified AI Practitioner (AIF-C01)** exam guide ([Domain 1](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html)).

---

## 1.1 Core concepts and terminology

### Artificial intelligence (AI)

**AI** is the broad goal of building systems that perform tasks that typically require human-like intelligence: perception, language understanding, reasoning, recommendation, and decision support.

### Machine learning (ML)

**ML** is a subset of AI where behavior improves from **data** and **experience** (training) rather than from hand-coded rules alone. A **model** maps inputs to outputs; an **algorithm** is the procedure used to learn that mapping.

### Deep learning

**Deep learning** uses **neural networks** with many layers to learn hierarchical representations. It powers most modern computer vision and NLP systems and underpins large **transformer**-based language models.

### Generative AI (GenAI)

**GenAI** models learn to **generate** new content (text, images, audio, code) conditioned on prompts or other inputs. GenAI is a subset of AI; it overlaps heavily with ML and deep learning.

### Inference types

- **Real-time (online) inference:** low-latency responses (chatbots, fraud scoring on a click).
- **Batch inference:** scoring large volumes asynchronously (overnight scoring of customers, bulk document processing).

### Data types you must recognize

| Category                 | Examples                                                                    |
| ------------------------ | --------------------------------------------------------------------------- |
| **Labeled vs unlabeled** | Labeled: spam/not spam. Unlabeled: raw text for clustering or pre-training. |
| **Structured**           | Rows/columns in databases (tabular).                                        |
| **Unstructured**         | PDFs, images, audio, free text.                                             |
| **Time series**          | Metrics over time (demand forecasting).                                     |
| **Modalities**           | Text, image, audio, video; **multimodal** models use more than one.      |

### Learning paradigms

- **Supervised learning:** learn input→output from labeled examples (classification, regression).
- **Unsupervised learning:** find structure without labels (clustering, dimensionality reduction).
- **Reinforcement learning:** learn via rewards/penalties from an environment (games, robotics, some recommendation/control problems).

### Terms that appear on decisions and ethics questions

- **Bias:** systematic errors that hurt certain groups or scenarios.
- **Fairness:** expectations that models do not unjustly disadvantage groups; definitions vary by context.
- **Variance:** sensitivity to training data noise (**overfitting** = high variance; **underfitting** = high bias).
- **Training vs inference:** training learns parameters; inference applies the model to new data.

---

## 1.2 Practical use cases: when AI helps, and when it does not

### Where AI/ML tends to add value

- **Scale:** scoring millions of events or documents faster than manual review.
- **Automation:** routing, triage, tagging, summarization, first-line support.
- **Assisted decision-making:** recommendations and risk scores with human oversight.
- **Perception tasks:** speech-to-text, object detection, document understanding.

### When AI/ML may be the wrong tool

- **Deterministic guarantees** are required and cannot tolerate probabilistic error.
- **Cost exceeds benefit:** model lifecycle (data, monitoring, retraining) costs more than the problem’s value.
- **Insufficient or untrusted data** makes learning unreliable.
- **Regulatory or safety** context demands interpretability or audit trails you cannot support.

### Technique selection (high level)

| Problem shape             | Common technique family                      |
| ------------------------- | -------------------------------------------- |
| Predict a number          | **Regression**                               |
| Predict a category        | **Classification**                           |
| Group similar items       | **Clustering**                               |
| Rank or recommend         | **Recommendation** systems, learning-to-rank |
| Sequence or generate text | **LLMs** / sequence models                   |

### AWS managed AI services (recognize the role)

Examples from the exam scope: **Amazon SageMaker AI** (end-to-end ML platform), **Amazon Transcribe** (speech-to-text), **Amazon Translate** (machine translation), **Amazon Comprehend** (NLP insights), **Amazon Lex** (conversational interfaces), **Amazon Polly** (text-to-speech). You should match **service capability** to **use case**, not memorize every API.

---

## 1.3 The ML development lifecycle

A typical lifecycle includes:

1. **Business framing:** define success metrics and constraints.
2. **Data:** collection, labeling, cataloging, quality checks.
3. **Exploratory data analysis (EDA):** distributions, missing values, leakage risks.
4. **Preprocessing & feature engineering:** cleaning, encoding, scaling.
5. **Training:** choose algorithms, train, validate.
6. **Hyperparameter tuning:** improve generalization (exam: know it exists; practitioner exam does not require doing it).
7. **Evaluation:** technical metrics plus business KPIs.
8. **Deployment:** batch or real-time endpoints, A/B tests.
9. **Monitoring & operations:** drift, quality, retraining triggers (**MLOps** themes).

### Sources of models

- **Pre-trained open models** or **foundation models** (consume via API).
- **Custom training** on your data (more control, more responsibility).

### Ways to “use a model” in production

- **Managed API** (for example **Amazon Bedrock** model access).
- **Self-hosted** endpoints on **Amazon SageMaker AI** or container services (**ECS**, **EKS**, **EC2**).

### MLOps (what to remember)

Repeatable pipelines, experiment tracking, scalable training/inference, **model monitoring**, and governance hooks (lineage, approvals) so production systems stay reliable as data and models evolve.

### Metrics: technical vs business

- **Technical:** accuracy, precision/recall, **F1**, **AUC-ROC**, error rates.
- **Business:** cost per inference, revenue impact, customer satisfaction, compliance incidents avoided.

---

## Quick self-check

1. Explain how **supervised** learning differs from **unsupervised** learning in one sentence each.
2. Name one strength and one weakness of using **GenAI** for customer support.
3. List three stages of the ML lifecycle between **raw data** and **production monitoring**.

---

## Further reading (AWS)

- [What Is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
- [AWS Machine Learning Services](https://aws.amazon.com/machine-learning/)
