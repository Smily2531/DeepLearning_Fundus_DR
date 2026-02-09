**Project**: Deep Learning Fundus Image Analysis

**Summary**: Deep-Learning-Fundus-Image-Analysis is a compact, production-ready Flask web app that demonstrates diabetic retinopathy classification using an Xception-based convolutional neural network. It includes a small web UI for uploading fundus images, a ready-to-use model, and tools to (re)create the model from scratch.

**Highlights**
- **Easy demo**: Runs locally with Flask and accepts image uploads in the browser.
- **Reproducible model**: `create_full_model.py` builds an Xception model and saves `model/full.h5`.
- **Fallback weights**: If the full model file is not present, the app attempts a weights-only load from `model/Updated-Xception-diabetic-retinopathy.h5`.
- **Minimal dependencies**: Only `tensorflow`, `flask`, `numpy`, and `werkzeug` are required (see `requirements.txt`).

**Files of interest**
- `app.py` — Flask application and prediction logic. See [app.py](app.py)
- `create_full_model.py` — Builds and saves the Xception-based model. See [create_full_model.py](create_full_model.py)
- `model/full.h5` — Full saved model (architecture + weights). See [model/full.h5](model/full.h5)
- `model/Updated-Xception-diabetic-retinopathy.h5` — Provided weights fallback. See [model/Updated-Xception-diabetic-retinopathy.h5](model/Updated-Xception-diabetic-retinopathy.h5)
- `templates/` — HTML templates: `index.html` and `result.html`.
- `static/uploads/` — Uploaded images saved here during demo.

**Quick Start (Windows, recommended using the included virtualenv)**

1. Create and activate a virtual environment (if you don't already use the project `.venv`):

```powershell
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Optionally recreate the example model (this builds and saves `model/full.h5`).

```powershell
python create_full_model.py
```

4. Run the Flask app (development mode):

```powershell
python app.py
```

5. Open the demo in a browser: http://127.0.0.1:5000 — upload a fundus image and view the prediction.

**Notes on the Model**
- The script `create_full_model.py` constructs an Xception base with a global average pooling head and a final softmax layer for the 5-class diabetic retinopathy label set.
- The project ships a weights-only file (`model/Updated-Xception-diabetic-retinopathy.h5`) so the app can function without a fully serialized model. If you prefer the modern Keras native format, run the script to export then save again with `model.save('model/full.keras')`.

**Project Structure**
- `app.py` — web server, model load logic, preprocessing and routes.
- `create_full_model.py` — model architecture and initial save.
- `model/` — contains saved model artifacts.
- `templates/` — HTML templates for the web UI.
- `static/` — static assets and `uploads/` folder for input images.

**Troubleshooting**
- If TensorFlow fails to import or `ModuleNotFoundError` appears, ensure you installed dependencies into the active environment and that you are using a compatible Python version (3.8–3.11 recommended).
- If the web app prints "No model config found in H5 file", the repository shipped an H5 containing only weights — the app will attempt to rebuild the Xception architecture and load weights by name as a fallback.
- If you see performance-related warnings about CPU optimizations from TensorFlow, they are informational and safe to ignore for local demos.

**Testing the installation (quick HTTP check)**

From PowerShell, after the server is running, check the homepage status with:

```powershell
Invoke-WebRequest http://127.0.0.1:5000 -UseBasicParsing
```

A successful response will include the HTML for the index page.

**Want production deployment?**
- Use a WSGI server such as Gunicorn or Waitress (Windows) behind a reverse proxy. Containerize with Docker for consistent deployment.

**Contributing & License**
- Contributions: file a PR with a short description and test steps.
- License: This repository contains example code. Add a license file (e.g., MIT) if you plan to open-source it.

**Contact / Next steps**
- I can: (A) convert the saved model to the native `.keras` format, (B) add automated tests for the prediction route, or (C) containerize the app with a `Dockerfile` — tell me which you prefer.
