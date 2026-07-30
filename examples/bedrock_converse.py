"""
Amazon Bedrock: Converse API example (AWS SDK for Python / boto3).

Prerequisites:
  - IAM permission for bedrock:InvokeModel on the chosen model ID (and regional allowlisting if your account uses model access controls).
  - Replace MODEL_ID and REGION with values valid for your account.

Reference:
  https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html
"""

import json
import os
import sys

import boto3


def main() -> None:
    region = os.environ.get("AWS_REGION", "us-east-1")
    # Example IDs differ by region and model provider; use the Bedrock console or ListFoundationModels.
    model_id = os.environ.get(
        "BEDROCK_MODEL_ID",
        "anthropic.claude-3-haiku-20240307-v1:0",
    )

    client = boto3.client("bedrock-runtime", region_name=region)

    user_message = (
        "In two sentences, explain what temperature does in LLM inference."
    )

    # Converse uses a messages array with content blocks (text, image, etc.).
    response = client.converse(
        modelId=model_id,
        messages=[
            {
                "role": "user",
                "content": [{"text": user_message}],
            }
        ],
        inferenceConfig={
            "maxTokens": 256,
            "temperature": 0.2,
            "topP": 0.9,
        },
    )

    # Output shape: response["output"]["message"]["content"][*]["text"]
    message = response.get("output", {}).get("message", {})
    parts = message.get("content", [])
    texts = [p.get("text", "") for p in parts if "text" in p]
    reply = "\n".join(t for t in texts if t).strip()

    usage = response.get("usage", {})
    print(reply or json.dumps(response, default=str, indent=2))
    if usage:
        print("\n--- usage ---", file=sys.stderr)
        print(json.dumps(usage, indent=2), file=sys.stderr)


if __name__ == "__main__":
    main()
