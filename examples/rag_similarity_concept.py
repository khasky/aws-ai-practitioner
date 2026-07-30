"""
Conceptual helper: cosine similarity between two embedding vectors.

RAG retrieval often ranks document chunks by similarity between:
  - query embedding
  - chunk embeddings

This file is plain math for learning; no AWS calls. In production you would
store vectors in a database that supports similarity search (for example
OpenSearch k-NN, Aurora/pgvector patterns, or managed vector features), not
only in-memory Python lists.
"""

from __future__ import annotations

import math


def cosine_similarity(a: list[float], b: list[float]) -> float:
    if len(a) != len(b) or not a:
        raise ValueError("Vectors must be non-empty and equal length.")
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def main() -> None:
    # Toy vectors (not real embeddings; only illustrate ranking).
    query = [1.0, 0.0, 0.0]
    chunk_a = [0.9, 0.1, 0.0]  # closer to query
    chunk_b = [0.0, 1.0, 0.0]  # orthogonal

    print("similarity(query, chunk_a):", round(cosine_similarity(query, chunk_a), 4))
    print("similarity(query, chunk_b):", round(cosine_similarity(query, chunk_b), 4))


if __name__ == "__main__":
    main()
