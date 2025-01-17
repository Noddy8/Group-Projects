import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="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",
)

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Give me 5 Quiz Questions about python in Json format without and extra chat and explanation that starts with array."
                }
            ]
        }
    ]
)
# print(message)
# response_text = message.content[1]
# print(response_text)
message = str(message.content)
with open('output.json', 'w') as file:
    file.write(message)

print("Output has been saved to 'output.txt'")