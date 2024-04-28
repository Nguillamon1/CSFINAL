from flask import Flask, render_template
import random
import requests

app = Flask(__name__)

# List of art prompts
prompts = [
    "Draw a scene with a sunset in the background",
    "Create an artwork featuring a mythical creature",
    "Illustrate a moment of peace in a bustling city",
    "Sketch a character experiencing joy",
    "Paint a landscape from a bird's-eye view",
    "Compose a scene with contrasting themes of fire and water",
    "Illustrate an ancient tree with a secret door.",
    "Create a digital painting of a futuristic city at night.",
    "Sketch a portrait of a person made entirely of natural elements like leaves and flowers.",
    "Draw a peaceful scene inside a snow globe.",
    "Paint a bustling market scene from a medieval period.",
    "Illustrate a ship sailing on a sea under a starry sky.",
    "Compose a scene where day meets night in the same landscape.",
    "Create an artwork featuring a banquet in an enchanted forest.",
    "Sketch an animal that is a hybrid of two different species.",
    "Illustrate a character finding an unexpected treasure in the attic."
]

def fetch_colors():
    try:
        response = requests.get('https://csscolorsapi.com/api/colors')
        response.raise_for_status()  # Raises an HTTPError for bad responses
        colors = response.json()  # Make sure this matches the JSON structure from the API
        return colors
    except requests.RequestException as e:
        print(f"Failed to fetch colors: {e}")
        return []  # Return an empty list if there's a failure

@app.route('/')
def index():
    colors = fetch_colors()  # Fetch colors to display initially
    return render_template('index.html', colors=colors)

@app.route('/generate')
def generate():
    prompt = random.choice(prompts)
    colors = fetch_colors()  # Fetch colors to ensure they are always fresh with each prompt
    return render_template('prompt.html', prompt=prompt, colors=colors)

if __name__ == "__main__":
    app.run(debug=True)