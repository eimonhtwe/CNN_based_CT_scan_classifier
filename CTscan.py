

import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras.utils import img_to_array, load_img
from PIL import Image
import streamlit as st

# Load the model
FILE_ID = "1QQQlL932iw5duTdDe3HwxY0hkDCpjCFi"
URL = f"https://drive.google.com/uc?id={FILE_ID}"
LOCAL = "model_CNN2_L.h5"

@st.cache_resource
def load_model():
    if not os.path.exists(LOCAL) or os.path.getsize(LOCAL) < 1024:
        gdown.download(URL, LOCAL, quiet=False)
    return tf.keras.models.load_model(LOCAL)

model = load_model()

# Compile the model if needed
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Streamlit app setup
st.title('What type of lung nodule is this?')
st.write("Upload a CT scan image and we'll tell you what type of lung nodule the patient has.")
image_input = st.file_uploader('Upload your image here:')

button = st.button('Classify Image')

if button and image_input is not None:
    # Load and preprocess the image
    img = Image.open(image_input).convert('L')  # Convert to grayscale
    img = img.resize((224, 224))  # Resize image to 224x224
    img = np.expand_dims(img_to_array(img), axis=0)  # Convert image to array and add batch dimension
    img = img / 255.0  # Normalize the image

    # Make a prediction
    pred = model.predict(img)

    # Display the result
    if np.argmax(pred, axis=1) == 0:
        st.write('This nodule appears to be benign.')
    elif np.argmax(pred, axis=1) == 1:
        st.write('This nodule appears to be malignant.')
    else:
        st.write('There does not appear to be a nodule present.')