import openai
# from openai import OpenAI
# client = OpenAI()

openai.api_key = "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"

question = input("What is your question\n")

completion = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are an assistant. Answer the given question."},
    {"role": "user", "content": question}
  ]
)

print(completion.choices[0].message.content)

#  OPEN AI
# def aiAssistant(query):
#     print("def: "+query)
#     openai.api_key = "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"

#     client = OpenAI()

#     completion = client.chat.completions.create(
#       model="gpt-3.5-turbo",
#       messages=[
#         {"role": "system", "content": "You are an assistant. Answer the given question."},
#         {"role": "user", "content": query}
#       ]
#     )

#     print(completion.choices[0].message.content)
    
    # elif "what" in query:
    #     from engine.features import aiAssistant
    #     print("command.py: "+query)
    #     aiAssistant(query)