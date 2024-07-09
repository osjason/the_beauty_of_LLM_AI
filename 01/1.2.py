from openai import OpenAI
import os

"""
请确保您的 openai api 的额度足够
"""

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],
  base_url=os.environ['OPENAI_BASE']
)

COMPLETION_MODEL = "gpt-3.5-turbo-instruct"

prompt = """
Man Utd must win trophies, says Ten Hag ahead of League Cup final

请将上面这句话的人名提取出来，并用 json 的方式展示出来
"""

def get_response(prompt):
    completions = client.completions.create (
        model=COMPLETION_MODEL,
        prompt=prompt,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.0,        
    )
    message = completions.choices[0].text
    return message

print(get_response(prompt)) 

"""
{
  "title": "Factory Stock PVC Inflatable Frog, Hot Selling Night Market Stall Toy with Light for Children's Water Play",
  "selling_points": [
    "Made with high quality PVC material",
    "Inflatable and easy to store",
    "Attractive design with glowing feature",
    "Perfect for water play and night markets",
    "Available in stock for immediate purchase"
  ],
  "price_range": "$15 - $25"
}
"""