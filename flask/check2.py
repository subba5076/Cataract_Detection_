from PIL import Image
import matplotlib.pyplot as plt

import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import *
from tensorflow.keras import preprocessing
import time



classifier_model = "E:\\major project\\major_phase2\\saved.h5"
path = "E:\\major project\\major_phase2\\flask\\uploads\\image.png"
model = load_model(classifier_model)
img = Image.open(path)
plt.imshow(np.array(img))
img = np.array(img.resize((94, 55)))
img = np.expand_dims(img, axis=0)
pred = model.predict(img)
print(pred)
print(f"predicted class : {'normal' if pred[0] > 0.5 else 'cataract'}")





