#!/usr/bin/env python
# coding: utf-8

# In[8]:


import tensorflow as tf
from tensorflow.keras.utils import image_dataset_from_directory 
from tensorflow.keras.layers import *
from tensorflow.keras.models import Sequential
import matplotlib.pyplot as plt


# In[9]:


dataset_path = r"C:\Users\shaik\OneDrive\Desktop\Projects"


# In[10]:


img_size = (128, 128)   # better than 64x64 for detail
batch_size = 32


# In[11]:


train_ds = image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="training",
    seed=42,
    image_size=img_size,
    batch_size=batch_size,
    label_mode="binary"
)


# In[12]:


val_ds = image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="validation",
    seed=42,
    image_size=img_size,
    batch_size=batch_size,
    label_mode="binary"
)


# In[13]:


AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)


# In[14]:


data_augmentation = Sequential([
    RandomFlip("horizontal"),
    RandomRotation(0.1),
    RandomZoom(0.1),
])


# In[15]:


model = Sequential([
    data_augmentation,   # applies augmentation on the fly
    Rescaling(1./255, input_shape=(128,128,3)),  # normalize
    
    Conv2D(32, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),   # prevents overfitting
    Dense(1, activation='sigmoid')   # binary classification
])


# In[16]:


model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy", tf.keras.metrics.Precision(), tf.keras.metrics.Recall()]
)


# In[17]:


history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=15
)


# In[19]:


plt.plot(history.history['accuracy'], label='Train Acc')
plt.plot(history.history['val_accuracy'], label='Val Acc')
plt.legend()
plt.show()


# In[20]:


model.save("AiClassifier")


# In[21]:


import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image


# In[25]:


#
img_path = r"C:\Users\shaik\OneDrive\Desktop\Projects\RealArt\RealArt\4a092cb31ce8d11f8ca53137d86c276f.jpg"
img = image.load_img(img_path, target_size=(128,128))  # must match training size
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)  # add batch dimension
img_array = img_array / 255.0  # normalize same as training

# Predict
prediction = model.predict(img_array)

if prediction[0][0] > 0.5:
    print("Prediction: Class 1 (e.g. Real Art)")
else:
    print("Prediction: Class 0 (e.g. AI Image)")


# In[26]:





# In[ ]:




