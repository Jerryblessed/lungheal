import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'models', 'inceptionv3_model.keras')
# model_path = os.path.join(BASE_DIR, 'models', 'densenet_model.h5')

print(f"Checking if model exists at: {model_path}")
print("File exists:", os.path.exists(model_path))
