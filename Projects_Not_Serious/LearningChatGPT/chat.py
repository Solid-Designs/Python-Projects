import openai

openai.api_key = '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'

completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo', 
    messages = [
        {"role": "system", "content":"You are a google ads copywriting assistant"},
        {"role": "user", "content": "Write generic ad copy for a used car dealership"} ]
    )

print(completion.choices[0].message.content)