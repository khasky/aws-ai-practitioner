# AWS services primer (exam-oriented)

This primer ties **in-scope services** from the official [in-scope list](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/aif-01-in-scope-services.html) to **exam-style mental models**. Use AWS documentation for details; this page is a shortcut, not a spec.

---

## Machine Learning (core names)

| Service                       | One-line role                                                         |
| ----------------------------- | --------------------------------------------------------------------- |
| **Amazon Bedrock**            | Managed foundation models, knowledge bases, agents, guardrails.       |
| **Amazon SageMaker AI**       | Build, train, deploy, monitor ML; JumpStart for pre-trained models.   |
| **Amazon Q Developer**        | AI assistant for builders (IDE/in-console help).                      |
| **Amazon Q Business**         | Enterprise Q&A across connected company data (governed access).       |
| **Amazon Nova**               | AWS foundation model family (multimodal capabilities vary by model).  |
| **Amazon Kendra**             | Intelligent enterprise search (often paired with retrieval patterns). |
| **Amazon Lex**                | Build conversational bots.                                            |
| **Amazon Polly**              | Text-to-speech.                                                       |
| **Amazon Transcribe**         | Speech-to-text.                                                       |
| **Amazon Translate**          | Machine translation.                                                  |
| **Amazon Comprehend**         | NLP insights (entities, sentiment, classification).                   |
| **Amazon Rekognition**        | Image and video analysis.                                             |
| **Amazon Textract**           | Extract text and structured data from documents.                      |
| **Amazon Personalize**        | Real-time personalization and recommendations.                        |
| **Amazon Fraud Detector**     | Fraud scoring with ML templates.                                      |
| **Amazon Augmented AI (A2I)** | Human review workflows.                                               |

---

## Analytics and data (common AI companions)

| Service                       | Role in AI stories                                                        |
| ----------------------------- | ------------------------------------------------------------------------- |
| **Amazon S3**                 | Lake/landing zone for documents, images, audio; Bedrock ingestion source. |
| **AWS Glue / DataBrew**       | ETL and data prep for features and curated datasets.                      |
| **Amazon Redshift**           | Warehouse analytics; often a reporting layer.                             |
| **Amazon OpenSearch Service** | Search + vector patterns for retrieval.                                   |
| **AWS Lake Formation**        | Governed data lake permissions.                                           |

The official **in-scope** page is authoritative; AWS updates exam scope from time to time.

---

## Security, identity, compliance

| Service             | Typical exam angle                                                   |
| ------------------- | -------------------------------------------------------------------- |
| **IAM**             | Least privilege for humans and workloads invoking Bedrock/SageMaker. |
| **KMS**             | Encryption keys for data and model artifacts.                        |
| **Secrets Manager** | Secrets rotation and access control.                                 |
| **Macie**           | Sensitive data discovery.                                            |
| **CloudTrail**      | Audit API usage.                                                     |
| **Config**          | Track configuration drift.                                           |
| **Audit Manager**   | Compliance evidence.                                                 |
| **Artifact**        | Download attestations and agreements.                                |

---

## Operations and cost

| Service                     | Role                                                                    |
| --------------------------- | ----------------------------------------------------------------------- |
| **CloudWatch**              | Metrics, logs, alarms for endpoints and applications.                   |
| **Trusted Advisor**         | Guidance on cost, security, fault tolerance.                            |
| **Cost Explorer / Budgets** | Track model spend and set alerts.                                       |
| **Well-Architected Tool**   | Review architectures against best practices (including sustainability). |

---

## How to study services for AIF-C01

1. **Match service → problem** (for example Textract → forms; Transcribe → audio notes).
2. Know **where Bedrock fits** vs **SageMaker AI** vs **application services** (Lex, Comprehend).
3. Understand **security building blocks** (IAM, KMS, logging) as **cross-cutting** requirements.

---

## Official link

- [In-scope AWS services and features (AIF-C01)](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/aif-01-in-scope-services.html)
