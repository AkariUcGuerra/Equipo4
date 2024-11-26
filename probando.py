# -*- coding: utf-8 -*-
"""
C:\\Users\\puchu\\Documents\\Séptimo Semestre\\Robótica\\RedBrazo\\Fotos
Created on Wed Sep 11 11:48:41 2024

@author: puchu
"""
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, GlobalAveragePooling2D
from tensorflow.keras.applications import VGG16
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam

# Dimensiones de entrada
IMG_WIDTH, IMG_HEIGHT = 150, 150

# Preprocesamiento de imágenes (aumentación de datos)
datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

# Directorio donde se encuentran tus imágenes organizadas por carpetas (fresa, manzana, mango, uva)
train_generator = datagen.flow_from_directory(
    'C:\\Users\\puchu\\Documents\\Séptimo Semestre\\Robótica\\RedBrazo\\Fotos',  # Carpeta de entrenamiento
    target_size=(IMG_WIDTH, IMG_HEIGHT),
    batch_size=32,
    class_mode='categorical'  # Sin 'subset' ya que no hay split
)

validation_generator = datagen.flow_from_directory(
    'C:\\Users\\puchu\\Documents\\Séptimo Semestre\\Robótica\\validacion',  # Carpeta de validación
    target_size=(IMG_WIDTH, IMG_HEIGHT),
    batch_size=32,
    class_mode='categorical'  # Sin 'subset'
)

# Cargar el modelo VGG16 preentrenado y adaptar para tu tarea
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(IMG_WIDTH, IMG_HEIGHT, 3))
x = base_model.output
x = GlobalAveragePooling2D()(x)  # Reemplazar Flatten con GlobalAveragePooling para mejorar generalización
x = Dense(128, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.001))(x)
x = Dropout(0.5)(x)
predictions = Dense(4, activation='softmax')(x)  # 4 clases (fresa, manzana, mango, uva)

model = Model(inputs=base_model.input, outputs=predictions)

# Congelar las capas del modelo base para evitar sobreajuste en las primeras épocas
for layer in base_model.layers:
    layer.trainable = False

# Compilación del modelo
model.compile(optimizer=Adam(learning_rate=1e-4), loss='categorical_crossentropy', metrics=['accuracy'])

# Configuración de Early Stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Entrenamiento del modelo
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // validation_generator.batch_size,
    epochs=30,
    callbacks=[early_stopping]
)

# Guardar el modelo entrenado
model.save('boing_detector_model.h5')

# Función para preprocesar imagen y predecir
def predict_image(model, image):
    image_resized = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))  # Redimensionar a tamaño adecuado
    image_resized = np.expand_dims(image_resized, axis=0)  # Expandir dimensiones para predicción
    image_resized = image_resized / 255.0  # Normalizar como durante el entrenamiento
    prediction = model.predict(image_resized)
    return prediction

# Cargar el modelo entrenado
model = tf.keras.models.load_model('boing_detector_model.h5')

