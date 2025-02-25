from openai import OpenAI

client = OpenAI(
  api_key="tu dajemy klucz"
)

completion = client.chat.completions.create(
  model="gpt-4o",
  store=True,
  messages=[
      {"role": "system", "content": "Jesteś 15 latkiem który wymyśla głupie dowcipy"},
      {"role": "user", "content": "Opowiedz dowcip"}
  ]
)

print(completion.choices[0].message.content)
