from tensorflow.keras.applications import Xception
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Model
import os

CLASSES = [
    "No Diabetic Retinopathy",
    "Mild Diabetic Retinopathy",
    "Moderate Diabetic Retinopathy",
    "Severe Diabetic Retinopathy",
    "Proliferative Diabetic Retinopathy"
]

os.makedirs('model', exist_ok=True)
base = Xception(weights=None, include_top=False, input_shape=(299,299,3))
x = base.output
x = GlobalAveragePooling2D()(x)
outputs = Dense(len(CLASSES), activation='softmax')(x)
model = Model(inputs=base.input, outputs=outputs)

# Save the full model (architecture + initial weights)
model.save('model/full.h5')
print('Saved model/full.h5')
