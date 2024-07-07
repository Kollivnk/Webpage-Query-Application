import openai

openai.api_key = 'sk-proj-oHJ1F8GVspwiKQ5iT8McT3BlbkFJRzS8a6D5yB79aRnMdUgH'

response = openai.Completion.create(
    engine="gpt-3.5-turbo",
    prompt="Translate the following English text to French: 'Hello, how are you?'",
    max_tokens=60
)

print(response.choices[0].text.strip())
