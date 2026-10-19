import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing")

client = genai.Client(api_key=api_key)

# review = "The app is easy to use, but checkout takes too long."

# prompt = f"""
# Classify the sentiment of the customer review.
# Allowed labels: positive, neutral, negative.
# Return only one label.

review = "Order 4512 was delivered on 12 Oct. the customer paid rs 1499"

prompt = f"""
get order number, delivery date, and amount from {review}
"""



response = client.models.generate_content(
    model=model,
    contents=prompt
)

print(response.text)