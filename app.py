import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from ultralytics import YOLO
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for the Flask app
CORS(app, resources={r"/*": {"origins": "*"}})

RELEASE_URL = "https://github.com/HebaHamdan2/ChildDrawingsSpeak-backend/releases/download/v.1.0.0/best.pt"  
MODEL_PATH = "/tmp/best.pt"  

def download_model():
    if not os.path.exists(MODEL_PATH):
        response = requests.get(RELEASE_URL)
        if response.status_code == 200:
            with open(MODEL_PATH, 'wb') as f:
                f.write(response.content)

# Download the model if it doesn't exist
download_model()

# Load the YOLO model
model = YOLO(MODEL_PATH)

# Define allowed file extensions for uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict', methods=['POST'])
def predict():
    # Check if an image file is included in the request
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']
    
    # Validate file format
    if not (file and allowed_file(file.filename)):
        return jsonify({'error': 'Invalid file format. Allowed formats: png, jpg, jpeg'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join("/tmp", filename)

    # Save the uploaded file to the temporary directory
    file.save(filepath)

    try:
        # Run inference using the YOLO model
        results = model.predict(source=filepath, show=False)

        # Cleanup the temporary file after prediction
        os.remove(filepath)

        # Extract and format results
        if isinstance(results, list) and hasattr(results[0], 'probs') and results[0].probs is not None:
            probs = results[0].probs.data.numpy()
            label_names = {0: 'Anger and aggression', 1: 'Anxiety', 2: 'Happy', 3: 'Sad'}
            predictions = {label_names.get(i, f'Class {i}'): f"{prob * 100:.2f}%" for i, prob in enumerate(probs)}
            return jsonify({'predictions': predictions}), 200
        else:
            return jsonify({'error': 'Unable to process the image'}), 500

    except Exception as e:
        # Log the error and cleanup
        if os.path.exists(filepath):
            os.remove(filepath)
        return jsonify({'error': f"Error during prediction: {str(e)}"}), 500

# Main entry point for Vercel deployment
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5000)))