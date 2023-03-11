import os
import openai
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")
if (len(sys.argv) != 2):
    print("Error:Need the title please!")
    exit()
title = sys.argv[1]
prompt = "I want to write a blog post about '" + title + "'.Give a list of 5 sections in a numbered bullet point format about the blog post"
#synopsis = openai.Completion.create(
#  model = "text-davinci-003",
#  prompt = prompt,
#  max_tokens = 3000,
#  temperature = 0.7
#)
#synopsis = synopsis.choices[0].text
#synopsis = synopsis.strip()
synopsis = """1. Introduction: What is AI and How it is Changing the Tech Landscape
2. Benefits of AI for Developers
3. Potential Risks of AI Replacing Developers
4. Solutions to Ensure AI Does Not Replace Developers
5. Conclusion: Final Thoughts on the Impact of AI on Developers""" 
print(synopsis)

lines = synopsis.strip().splitlines()

for section in lines:
    print(section)
    prompt = "I want to write a blog post about the title '" + title + "'. + synopsis + "\n\nGive a detailed explanation of the section '" + section + "' in a minimum of 500 words."
    print(prompt)
    exit()
