import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing")

client = genai.Client(api_key=api_key)

ticket = "My delivery is 20 minutes late."

prompt = f"""
Classify each support ticket as LOW, MEDIUM or HIGH priority. Return only the label.

Example 1 
Ticket: "I forgot how to change my profile photo." 
Priority: LOW

Example 2
Ticket: "Payment succeeded but the order was not created. 
Priority: HIGH

Now classify:
Ticket: "{ticket}" 
Priority:

In ans we need both Ticket and priority both
"""


response = client.models.generate_content(
    model=model,
    contents=prompt
)

print(response.text)