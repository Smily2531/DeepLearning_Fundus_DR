from flask import Flask, render_template, request
import numpy as np
import os

from tensorflow.keras.models import load_model, Model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import preprocess_input, Xception
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from werkzeug.utils import secure_filename

# ---------------- FLASK APP ----------------
app = Flask(__name__)

# ---------------- FOLDERS ----------------
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------------- CLASSES ----------------
CLASSES = [
    "No Diabetic Retinopathy",
    "Mild Diabetic Retinopathy",
    "Moderate Diabetic Retinopathy",
    "Severe Diabetic Retinopathy",
    "Proliferative Diabetic Retinopathy"
]

# ---------------- LOAD MODEL ----------------
# Prefer a full saved model if provided by the user (model/full.h5), otherwise
# fall back to the shipped weights file.
if os.path.exists('model/full.h5'):
    MODEL_PATH = 'model/full.h5'
else:
    MODEL_PATH = 'model/Updated-Xception-diabetic-retinopathy.h5'

try:
    model = load_model(MODEL_PATH, compile=False)
    print("✅ Full model loaded successfully")
except ValueError:
    # The .h5 file may contain only weights (no model config). Build a compatible
    # Xception-based classifier and load the weights as a fallback.
    print("⚠️ No model config found in H5 file — attempting weights-only load")
    base = Xception(weights=None, include_top=False, input_shape=(299, 299, 3))
    x = base.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    outputs = Dense(len(CLASSES), activation='softmax')(x)
    model = Model(inputs=base.input, outputs=outputs)
    try:
        model.load_weights(MODEL_PATH)
        print("✅ Weights loaded into Xception-based model")
    except ValueError:
        print("⚠️ Exact weights load failed — retrying by name (partial load)")
        model.load_weights(MODEL_PATH, by_name=True)
        print("✅ Partial weights loaded by name into Xception-based model")



# ---------------- IMAGE PREPROCESS ----------------
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(299, 299))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

# ---------------- ROUTES ----------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded"

    file = request.files['file']
    if file.filename == '':
        return "No file selected"

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    img = preprocess_image(file_path)
    prediction = model.predict(img)
    predicted_class = CLASSES[np.argmax(prediction)]

    return render_template(
        'result.html',
        prediction=predicted_class,
        image_path=file_path
    )

# ---------------- MAIN ----------------
if __name__ == '__main__':
    app.run(debug=True)
