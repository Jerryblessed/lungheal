import os
import numpy as np
from django.db import models
from django.utils import timezone
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Get the base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define available models with absolute paths
MODEL_PATHS = {
    'DenseNet': os.path.join(BASE_DIR, 'models', 'densenet121_model.keras'),
    'InceptionV3': os.path.join(BASE_DIR, 'models', 'inceptionv3_model.keras'),
    'MobileNet': os.path.join(BASE_DIR, 'models', 'mobilenetv2_model.keras'),
}

def load_selected_model(model_type):
    """Load model based on user selection, with error handling."""
    model_path = MODEL_PATHS.get(model_type)

    if not model_path or not os.path.exists(model_path):
        print(f"🚨 Model file not found: {model_path}")
        return None

    try:
        return load_model(model_path)
    except Exception as e:
        print(f"⚠️ Error loading model {model_type}: {str(e)}")
        return None

class Patientdb(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    state = models.CharField(max_length=50)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
    
    MODEL_CHOICES = [
        ('InceptionV3', 'InceptionV3'),
        ('MobileNet', 'MobileNet'),
        ('DenseNet', 'DenseNet'),
    ]
    model_type = models.CharField(max_length=20, choices=MODEL_CHOICES, default='InceptionV3')
    diagnosis = models.CharField(max_length=100, blank=True, null=True)
    classified = models.CharField(max_length=200, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """Predict diagnosis before saving."""
        model = load_selected_model(self.model_type)

        if not model:
            print(f"❌ Model {self.model_type} could not be loaded.")
            super().save(*args, **kwargs)
            return

        try:
            if not self.image:
                print("⚠️ No image uploaded.")
                super().save(*args, **kwargs)
                return

            img_path = self.image.path  # Ensure image is saved before accessing the path
            img = image.load_img(img_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            prediction = model.predict(img_array)
            
            # Ensure the output is as expected
            if prediction.shape[1] != 3:
                print(f"⚠️ Unexpected model output shape: {prediction.shape}")
                super().save(*args, **kwargs)
                return
            
            class_labels = ['Lung Adenocarcinoma', 'Normal Lung', 'Lung Squamous Cell Carcinoma']
            self.diagnosis = class_labels[np.argmax(prediction)]

        except Exception as e:
            print(f"⚠️ Error during image classification: {str(e)}")

        super().save(*args, **kwargs)

# import os

# import numpy as np
# from django.db import models
# from django.utils import timezone
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image

# # Get the base directory of the project
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # Define available models with absolute paths
# MODEL_PATHS = {
#     'DenseNet': os.path.join(BASE_DIR, 'models', 'densenet_model.h5'),
#     'InceptionV3': os.path.join(BASE_DIR, 'models', 'inceptionv3_model.h5'),
#     'MobileNet': os.path.join(BASE_DIR, 'models', 'mobilenet_model_s.h5'),
# }

# def load_selected_model(model_type):
#     """Load model based on user selection, with error handling."""
#     model_path = MODEL_PATHS.get(model_type)
    
#     if not model_path or not os.path.exists(model_path):
#         print(f"🚨 Model file not found: {model_path}")
#         return None

#     try:
#         return load_model(model_path)
#     except Exception as e:
#         print(f"⚠️ Error loading model {model_type}: {str(e)}")
#         return None

# class Patientdb(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     dob = models.DateField()
#     state = models.CharField(max_length=50)
#     gender = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='uploads/')
    
#     MODEL_CHOICES = [
#         ('InceptionV3', 'InceptionV3'),
#         ('MobileNet', 'MobileNet'),
#         ('DenseNet', 'DenseNet'),
#     ]
#     model_type = models.CharField(max_length=20, choices=MODEL_CHOICES, default='InceptionV3')
#     diagnosis = models.CharField(max_length=100, blank=True, null=True)
#     classified = models.CharField(max_length=200, blank=True)
#     uploaded = models.DateTimeField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         """Predict diagnosis before saving."""
#         model = load_selected_model(self.model_type)
        
#         if not model:
#             print(f"❌ Model {self.model_type} could not be loaded.")
#             super().save(*args, **kwargs)
#             return

#         try:
#             img_path = self.image.path
#             img = image.load_img(img_path, target_size=(224, 224))
#             img_array = image.img_to_array(img)
#             img_array = np.expand_dims(img_array, axis=0) / 255.0

#             prediction = model.predict(img_array)
#             class_labels = ['Malignant Adenocarcinoma', 'Benign', 'Malignant Squamous']
#             self.diagnosis = class_labels[np.argmax(prediction)]

#         except Exception as e:
#             print(f"⚠️ Error during image classification: {str(e)}")

#         super().save(*args, **kwargs)
