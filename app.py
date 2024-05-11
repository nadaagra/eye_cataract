from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import io

# Initialize Flask application
app = Flask(__name__)

# Load the trained model
model = load_model('cataract_detection_model.h5')

# Define route for predicting cataract
@app.route('/predict', methods=['POST'])
def predict_cataract():
    try:
        # Check if an image file is uploaded
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'}), 400

        # Get the uploaded image file
        image_file = request.files['image']

        # Read the image file
        img_bytes = image_file.read()

        # Convert the image bytes to an image array
        img = image.load_img(io.BytesIO(img_bytes), target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0  # Normalize the image data

        # Make a prediction
        prediction = model.predict(img_array)

        # Get the predicted class
        predicted_class = 'normal' if prediction[0][0] > 0.5 else 'cataract'

        return jsonify({'result': predicted_class}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5000")

