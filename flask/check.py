from PIL import Image
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model

classifier_model = "E:\\major project\\major_phase2\\saved.h5"

def process_image(image_path):
    model = load_model(classifier_model)
    img = Image.open(image_path)
    img = img.resize((94, 55))
    img = np.array(img)
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    return pred[0]

if __name__ == "__main__":
    image_path = "uploads/image.png"
    pred = process_image(image_path)
    with open('output.txt', 'w') as f:
        f.write(f"predicted class : {'normal' if pred[0] > 0.5 else 'cataract'}")
