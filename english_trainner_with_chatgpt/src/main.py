import openai

OPEN_AI_API_KEY = "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"

openai.api_key = OPEN_AI_API_KEY
openai.Model.list()

response = openai.Completion.create(
    engine='davinci',
    prompt='Once upon a time',
    max_tokens=50
)
print(response)

# response = openai.Completion.create(
#     engine="davinci-codex",
#     prompt="你的输入文本",
#     max_tokens=50
# )
#
# if response and response.choices:
#     reply = response.choices[0].text.strip()
#     print(reply)

