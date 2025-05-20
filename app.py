from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/fetch-url', methods=['GET'])
def fetch_url():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'Missing URL parameter'}), 400

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return jsonify({'html': response.text})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/proxy-image', methods=['GET'])
def proxy_image():
    image_url = request.args.get('image_url')
    if not image_url:
        return jsonify({'error': 'Missing image_url parameter'}), 400

    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()

        # Get content type from the response headers
        content_type = response.headers.get('content-type')
        if not content_type or not content_type.startswith('image/'):
            return jsonify({'error': 'URL does not point to a valid image'}), 400

        return response.content, 200, {'Content-Type': content_type}
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
