from Sampledata_ForEmbedding_9 import documents
from Embedding_11 import embed_text, embed_texts
import math

texts = [doc["text"] for doc in documents]
vectors = embed_texts(texts)

for doc, vector in zip(documents, vectors):
    print(
        doc["id"],
        "dimension =",
        len(vector)
    )

#query = "I paid once but my card shows the charge twice"
query = "I want to change my password"

query_vector = embed_text(query)

print("Query:", query)
print(
    "Query dimension:",
    len(query_vector)
)

import math

def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot / (norm_a * norm_b)

scored = []
for doc, vector in zip(documents, vectors):
    score = cosine_similarity(query_vector, vector)
    scored.append((score, doc))

scored.sort(key=lambda item: item[0], reverse=True)

for score, doc in scored:
    print(round(score, 4), doc["id"], doc["text"])