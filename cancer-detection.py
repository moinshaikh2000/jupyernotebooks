#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow import keras
from keras.applications.efficientnet import EfficientNetB4
from keras.applications.efficientnet import preprocess_input, decode_predictions
import numpy as np


# In[ ]:


model = EfficientNetB4(weights='imagenet')



# In[4]:


img_path = '/kaggle/input/ant-image/ant.jpeg'
img = keras.utils.load_img(img_path, target_size=(380, 380))
x = keras.utils.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)
# decode the results into a list of tuples (class, description, probability)
# (one such list for each sample in the batch)
print('Predicted:', decode_predictions(preds, top=3)[0])


# In[5]:


## Fine Tuning the Model for Cancer Detection


# In[6]:


from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D


# In[7]:


# create the base pre-trained model
base_model = EfficientNetB4(weights='imagenet', include_top=False)


# In[8]:


# add a global spatial average pooling layer
x = base_model.output
x = GlobalAveragePooling2D()(x)
# let's add a fully-connected layer
x = Dense(1024, activation='relu')(x)
# and a logistic layer -- let's say we have 2 classes
predictions = Dense(1, activation='sigmoid')(x)


# In[15]:


# this is the model we will train
model = Model(inputs=base_model.input, outputs=predictions)

# first: train only the top layers (which were randomly initialized)
# i.e. freeze all convolutional InceptionV3 layers
for layer in base_model.layers:
    layer.trainable = False

# compile the model (should be done *after* setting layers to non-trainable)
model.compile(optimizer='rmsprop', loss='binary_crossentropy',metrics=['Accuracy','Precision','Recall'])



# In[10]:


train_ds = keras.utils.image_dataset_from_directory(
    '/kaggle/input/melanoma-cancer-dataset/train',
    labels='inferred',
    label_mode='int',
    color_mode='rgb',
    batch_size=32,
    image_size=(380, 380),
    shuffle=True,
    seed=1,
    interpolation='bilinear',
)


# In[11]:


train_ds.class_names


# In[12]:


for i,j in train_ds.take(1):
    print(j)


# In[13]:


val_ds = keras.utils.image_dataset_from_directory(
    '/kaggle/input/melanoma-cancer-dataset/test',
    labels='inferred',
    label_mode='int',
    color_mode='rgb',
    batch_size=32,
    image_size=(380, 380),
    shuffle=True,
    seed=1,
    interpolation='bilinear',
)


# In[16]:


history = model.fit(train_ds,epochs=10,validation_data=val_ds)


# In[17]:


model.save('cancer.h5')


# In[20]:


img_path = '/kaggle/input/cancer-sample/C0464485-Lentigo_maligna_melanoma_copy.max-600x600.png'
img = keras.utils.load_img(img_path, target_size=(380, 380))
x = keras.utils.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)


# In[21]:


preds


# In[ ]:




