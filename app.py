from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
import os
from flask_cors import CORS  # Import CORS
# Load environment variables
load_dotenv()
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes by default

# Configuration for OpenAI API key
openai.api_key = os.getenv('SECRET_KEY')
@app.route('/generar/certificado')
def generar_certificado():
    # Get the prompt from the query parameters
    mensaje = request.args.get('promp')

    if not mensaje:
        return
    try:
        # Call the OpenAI API to generate the certificate image
        response = openai.Image.create(
            prompt=mensaje,
            n=1,
            size="1024x1024"
        )

        # Get the generated image URL
        image_url = response['data'][0]['url']
        print(image_url)
        return jsonify({'image_url': image_url})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
