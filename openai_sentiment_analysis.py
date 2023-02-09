import os
import openai

openai.api_key = ""

text = input("Please enter the news article text: ")

prompt = f"Please read the text of the news article as positive or negative and give me output: {text}"

response = openai.Completion.create(
    model="davinci:ft-personal:sentiment-classifier-2023-04-01-02-12-27",
    prompt=prompt,
    temperature=1,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["stos"]
)

print(response.choices[0].text)
output_file = "output.txt"

with open(output_file, "w") as file:
    file.write(response.choices[0].text.strip())
