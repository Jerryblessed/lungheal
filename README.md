# LungHeal - AI Histopathology Lung Cancer Detection Web App

LungHeal is a web application that empowers doctors and patients to upload histopathology lung images and receive accurate AI-driven diagnoses using state-of-the-art deep learning models. 🧬✨

## Dataset
📚 We use the publicly available **Lung and Colon Cancer Histopathological Images Dataset** from Kaggle. This curated dataset enables precise model training across three diagnostic classes:
- Benign
- Malignant Squamous Cell Carcinoma
- Malignant Adenocarcinoma

## Model Architecture
🤖 LungHeal introduces **three AI models** for image classification:
- **MobileNetV2**
- **DenseNet121**
- **InceptionV3**

All models are in `.keras` format for better metadata handling and are available for users to select the most accurate result. This is a major improvement over legacy systems that only used `.h` format with ResNet.

## New Functionalities for Hackathon 🛠️
- 🚀 Added support for **multi-model selection** with individual prediction outputs.
- 🖼️ Support for **histopathology-based diagnosis** instead of standard X-rays.
- 👨‍⚕️ Dual login system for **patients and doctors**.
- 🌐 Intuitive UI built with **React** and backend powered by **Django**.

## Web Application Flow
1. User logs in (doctor or patient).
2. Upload histopathology lung image.
3. Select preferred AI model (MobileNetV2, DenseNet121, or InceptionV3).
4. AI returns prediction: **Benign**, **Malignant Squamous**, or **Malignant Adenocarcinoma**.

## Technologies Used
- Python
- Django (Backend)
- React (Frontend)
- Keras (Model framework)
- HTML/CSS
- TensorFlow

## Getting Started
```bash
# Clone the repository
git clone https://github.com/jerryblessed/lungheal.git
cd lungheal

# Install backend dependencies
pip install -r requirements.txt

# Run Django server
python manage.py runserver

# In another terminal, run frontend
cd frontend
npm install
npm start
```
Visit `http://localhost:3000` to interact with the web app.

## Prior Solutions vs LungHeal
Traditional treatment included:
- 💉 **Chemotherapy** – Uses strong drugs, often with severe side effects.
- 🔪 **Surgery** – Removes tumors but isn’t always viable.
- ☢️ **Radiation** – Risky and may affect healthy tissue.

**LungHeal provides a non-invasive, accurate, and fast diagnosis option powered by AI.**

## Quote That Inspires Us 💡
> "It is health that is the real wealth and not pieces of gold and silver."

---
Made with ❤️ by **Team LungHeal** – Your AI partner for faster, safer lung cancer detection.
