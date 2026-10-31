import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
embedding_model = os.getenv(
    "GEMINI_EMBEDDING_MODEL",
    "gemini-embedding-2"
)
embedding_dimension = int(
    os.getenv("EMBEDDING_DIMENSION", "768")
)

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing")

client = genai.Client(api_key=api_key)

def embed_text(text: str) -> list[float]:
    cleaned = text.strip()

    if not cleaned:
        raise ValueError("Text cannot be empty")

    result = client.models.embed_content(
            model=embedding_model,
            contents=cleaned,
            config=types.EmbedContentConfig(
            output_dimensionality=embedding_dimension
        ),
    )

    return result.embeddings[0].values

def embed_texts(texts: list[str]) -> list[list[float]]:
    vectors = []

    for text in texts:
        vector = embed_text(text)
        vectors.append(vector)

    return vectors