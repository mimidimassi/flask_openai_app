from flask import Flask ,jsonify,request
import openai
app=Flask(__name__)

#engines = openai.Engine.list()
# Replace 'your-api-key' with your actual OpenAI API key
api_key = 'your-api-key_updated'

# Set the OpenAI API key
openai.api_key = api_key


# Define a route for serving the story
@app.route('/', methods=['POST', 'GET'])
def generate_story():
    if request.method == 'POST':
        # Get the prompt from the request body
        data = request.json
        prompt = data.get('prompt')
    elif request.method == 'GET':
        # Get the prompt from the query string
        prompt = "Rédigez-moi une histoire."
    # Generate the story using the GPT-3.5 model
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=prompt,
        max_tokens=100,
        temperature=0.5,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )

    # Extract the generated story from the response
    story = response.choices[0].text.strip()

    # Return the generated story as JSON
    return jsonify({"story": story})

if __name__=="__main__":

  app.run(debug=True)

