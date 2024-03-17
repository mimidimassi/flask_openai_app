import openai

# Replace 'your-api-key' with your actual OpenAI API key
api_key = 'your-api-key'

# Set the OpenAI API key
openai.api_key = api_key

# Define the prompt
prompt = "Rédigez-moi une histoire."

# Generate the story using the GPT-3.5 model
response = openai.Completion.create(
    engine="davinci-002",
    prompt=prompt,
    max_tokens=100
)

# Extract the generated story from the response
story = response.choices[0].text.strip()

# Print the generated story
print("Generated story:")
print(story)
