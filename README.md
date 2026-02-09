🎥Demo Video
[Watch Demo Video](https://drive.google.com/file/d/1IXfuCTzVBveESOMuqrYycPx3vBaAFveU/view?usp=sharing)

🩺 Deep Learning Fundus Image Analysis

Deep-Learning-Fundus-Image-Analysis is a compact, production-ready Flask web app for diabetic retinopathy classification using an Xception-based convolutional neural network. Upload fundus images via the browser, get instant predictions, or recreate the model from scratch.

🚀 Highlights

💻 Easy demo: Runs locally with Flask; upload images directly in the browser.

🔄 Reproducible model: create_full_model.py builds an Xception model and saves model/full.h5.

🛠 Fallback weights: If full.h5 is missing, the app uses model/Updated-Xception-diabetic-retinopathy.h5.

📦 Minimal dependencies: Only tensorflow, flask, numpy, and werkzeug.

📁 Project Structure
├─ app.py                    # Flask server & prediction logic
├─ create_full_model.py       # Builds & saves the Xception model
├─ model/
│  ├─ full.h5                 # Full saved model
│  └─ Updated-Xception-diabetic-retinopathy.h5  # Weights fallback
├─ templates/
│  ├─ index.html
│  └─ result.html
└─ static/
   └─ uploads/               # Uploaded images

🖼 Screenshots
1️⃣ Home Page

<img width="1800" height="987" alt="image" src="https://github.com/user-attachments/assets/dc126191-6bdf-4b69-9c58-b90807ee4746" />

2️⃣ Upload Image & Prediction

<img width="955" height="868" alt="image" src="https://github.com/user-attachments/assets/e47146b2-d35e-4ad7-abb0-2a883216b45a" />

3️⃣ Prediction Result

<img width="1149" height="846" alt="image" src="https://github.com/user-attachments/assets/435050de-53c7-4835-86e3-c2bcdb379e8b" />


Replace path/to/screenshotX.png with your uploaded images in the repo.

⚡ Quick Start (Windows recommended with virtualenv)

Create & activate virtualenv

python -m venv .venv
& .\.venv\Scripts\Activate.ps1


Install dependencies

pip install -r requirements.txt


Optionally recreate the example model

python create_full_model.py


Run the Flask app

python app.py


Open in browser: http://127.0.0.1:5000

Upload a fundus image and see the prediction! 🩷

🧠 Notes on the Model

Architecture: Xception base + global average pooling + softmax for 5-class diabetic retinopathy.

Weights-only file: Updated-Xception-diabetic-retinopathy.h5 allows the app to function even without full.h5.

Optional: Export in modern Keras format:

model.save('model/full.keras')

⚙ Troubleshooting

TensorFlow import errors? ✅ Ensure dependencies installed in active environment.

“No model config found in H5 file”? ✅ The app will rebuild architecture and load weights.

CPU optimization warnings? ✅ Informational, safe to ignore for local demos.

🧪 Testing Installation

Check homepage status:

Invoke-WebRequest http://127.0.0.1:5000 -UseBasicParsing


Successful response includes the HTML for index.html.

🚢 Production Deployment

Use Gunicorn or Waitress behind a reverse proxy.

Optional: Containerize with Docker for consistent deployment.

🤝 Contributing & License

PR with a short description & test steps are welcome.

Add a license file (e.g., MIT) if open-sourcing.
