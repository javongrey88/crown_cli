import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
print("Using model:", "gpt-3.5-turbo")


# Use the new OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")

client = OpenAI(api_key=api_key)

def get_product_recommendations(hair_type, goal):
    prompt = f"""
Suggest 3 affordable, natural hair products for someone with {hair_type} hair whose primary goal is {goal}.
For each product, give:
1. Product Name
2. Why it's recommended
3. A Google search link to find it
Respond in this format:

[Product Name]
- Description
- Google Link
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a Black hair care specialist who recommends natural, budget-conscious products "
                    "that avoid heavy chemicals and focus on sustainability."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=400
    )

    return response.choices[0].message.content
