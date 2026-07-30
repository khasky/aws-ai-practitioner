# Domain 5: Security, Compliance, and Governance for AI Solutions (14%)

AI workloads use normal **cloud security** practices plus **new attack surfaces** (prompt injection, data leakage via retrieval). Content maps to [Domain 5](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain5.html).

---

## 5.1 Securing AI systems on AWS

### Identity and access

Use **IAM roles** with least privilege, separate **data** access from **model invocation** permissions, and avoid long-lived keys where roles suffice.

### Encryption

Encrypt **data at rest** (for example with **AWS KMS**) and **in transit** (TLS). For regulated workloads, understand **key management** and rotation patterns.

### Network isolation

**Amazon VPC**, **security groups**, and **PrivateLink** patterns reduce exposure of APIs and data services to the public internet when your requirements call for that.

### Data protection and discovery

**Amazon Macie** helps discover sensitive data in S3; combine with classification and access policies.

### AI-specific threats

- **Prompt injection:** untrusted text in prompts that manipulates model behavior.
- **Data exfiltration** via clever prompts or tool misuse in agentic flows.
- **Poisoning** of knowledge sources used in RAG.

### Lineage and documentation

**Data lineage** and **cataloging** support audits: where training or retrieval data originated, who approved usage, and how models were evaluated. **Model cards** document provenance and limitations.

### Secure data engineering practices

Access controls, integrity checks, **privacy-enhancing** approaches where applicable, and quality validation before fine-tuning or indexing.

---

## 5.2 Governance and compliance

### AWS services that support audit and compliance workflows (examples)

- **AWS CloudTrail:** API activity logging.
- **AWS Config:** resource configuration history and rules.
- **AWS Audit Manager:** evidence collection for frameworks.
- **AWS Artifact:** on-demand compliance reports and agreements.
- **Amazon Inspector:** workload vulnerability scanning (know the role).
- **AWS Trusted Advisor:** cost/security/fault-tolerance checks (high level).

### Data governance themes

Retention, residency, monitoring, observability, and lifecycle rules aligned to policy.

### Processes and frameworks

Written policies, periodic reviews, training for builders, and structured approaches such as the **Generative AI Security Scoping Matrix** (exam-mentioned framing for scoping risks and controls).

---

## Shared responsibility model (quick reminder)

AWS secures **the cloud**. Customers secure **what they put in it**: data, IAM policies, encryption configuration, network paths, and safe application design (including prompts and retrieval pipelines).

---

## Quick self-check

1. Name **two** security controls and **one** AI-specific threat from this domain.
2. Which service primarily records **who called which AWS API** in your account?
3. Why does **RAG** increase the importance of **knowledge-base access control**?

---

## Further reading (AWS)

- [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)
- [Security in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/security.html)
- [AWS Audit Manager](https://aws.amazon.com/audit-manager/)
