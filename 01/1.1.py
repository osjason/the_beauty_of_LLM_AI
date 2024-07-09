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
Consideration proudct : 工厂现货PVC充气青蛙夜市地摊热卖充气玩具发光蛙儿童水上玩具

1. Compose human readale product title used on Amazon in english within 20 words.
2. Write 5 selling points for the products in Amazon.
3. Evaluate a price range for this product in U.S.

Output the result in json format with three properties called title, selling_points and price_range
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