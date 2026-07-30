"""
Amazon Bedrock: embedding model invocation (InvokeModel).

Embeddings are dense vectors used for semantic search, clustering, and RAG.

Prerequisites:
  - IAM permission for bedrock:InvokeModel on the embedding model ID.
  - Replace MODEL_ID with an embedding model available in your region.

This example uses the InvokeModel operation with a JSON body. Different models
use different JSON schemas; always check the model provider documentation.
"""

import json
import os

import boto3


def main() -> None:
    region = os.environ.get("AWS_REGION", "us-east-1")
    # Example: Amazon Titan Embeddings; verify exact model ID in your account/region.
    model_id = os.environ.get(
        "BEDROCK_EMBEDDING_MODEL_ID",
        "amazon.titan-embed-text-v2:0",
    )

    client = boto3.client("bedrock-runtime", region_name=region)

    payload = {
        "inputText": "Retrieval Augmented Generation grounds answers in retrieved documents.",
        # Some Titan embedding versions support dimensions / normalization flags; check docs for your model ID.
    }

    response = client.invoke_model(
        modelId=model_id,
        body=json.dumps(payload),
        contentType="application/json",
        accept="application/json",
    )

    body = json.loads(response["body"].read())

    # Titan Text Embeddings V2 returns embedding in "embedding" (list[float]).
    embedding = body.get("embedding")
    if embedding is None:
        print(json.dumps(body, indent=2))
        return

    print(f"dimensions: {len(embedding)}")
    print(f"first 8 values: {embedding[:8]}")


if __name__ == "__main__":
    main()
