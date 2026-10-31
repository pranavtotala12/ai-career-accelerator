from Embedding_11 import embed_text

text = "A customer was charged twice."
vector = embed_text(text)

print("Text:", text)
print("Python type:", type(vector))
print("Dimension:", len(vector))
print("First 5 values:", vector[:5])