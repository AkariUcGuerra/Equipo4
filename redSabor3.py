# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 15:12:11 2024

@author: erik2
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import cv2
import matplotlib.pyplot as plt
import time

# Parámetros básicos
img_width, img_height = 128, 128
num_classes = 5  # Manzana, Mango, Uva, Fresa, Sin producto
batch_size = 32
epochs = 30

# Creación del modelo
model = Sequential()

# Capas convolucionales
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Aplanamos los datos
model.add(Flatten())

# Capa totalmente conectada
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))

# Capa de salida con activación softmax (para clasificación multiclase)
model.add(Dense(num_classes, activation='softmax'))

# Compilación del modelo
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Resumen del modelo
model.summary()

# Directorio con imágenes clasificadas en carpetas (Manzana, Mango, Uva, Guayaba, Fresa)
train_data_dir = 'C:\\Users\\puchu\\Documents\\Séptimo Semestre\\Robótica\\RedBrazo\\Fotos'

# Preprocesamiento de las imágenes con aumentación
train_datagen = ImageDataGenerator(
    rescale=1.0/255.0,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

# Verificar la cantidad de imágenes por clase
print("Cantidad de imágenes por clase (entrenamiento):")
for cls, idx in train_generator.class_indices.items():
    print(f"{cls}: {np.sum(train_generator.classes == idx)}")

# Calcular pesos de clases manualmente
class_counts = np.bincount(train_generator.classes)
total_samples = len(train_generator.classes)
class_weights = {i: total_samples / (num_classes * count) for i, count in enumerate(class_counts)}

# Entrenamiento del modelo con pesos de clase
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // batch_size,
    epochs=epochs,
    class_weight=class_weights  # Aplicar los pesos de clase
)

# Guardar el modelo entrenado para usarlo en Spyder
model.save('clasificador_boing_color_fresa.h5')

# Graficar la precisión y pérdida durante el entrenamiento
plt.plot(history.history['accuracy'], label='Precisión de entrenamiento')
plt.plot(history.history['val_accuracy'], label='Precisión de validación')
plt.xlabel('Época')
plt.ylabel('Precisión')
plt.legend()
plt.show()

plt.plot(history.history['loss'], label='Pérdida de entrenamiento')
plt.plot(history.history['val_loss'], label='Pérdida de validación')
plt.xlabel('Época')
plt.ylabel('Pérdida')
plt.legend()
plt.show()

# Evaluar en el set de validación
val_loss, val_acc = model.evaluate(validation_generator)
print(f"Pérdida en validación: {val_loss}")
print(f"Precisión en validación: {val_acc}")

# Generar la matriz de confusión para el set de validación
Y_pred = model.predict(validation_generator)
y_pred = np.argmax(Y_pred, axis=1)

# Obtener etiquetas verdaderas del generador
y_true = validation_generator.classes

# Crear la matriz de confusión
cm = np.zeros((num_classes, num_classes), dtype=int)
for i in range(len(y_true)):
    cm[y_true[i], y_pred[i]] += 1

# Graficar la matriz de confusión
fig, ax = plt.subplots(figsize=(10, 10))
cax = ax.matshow(cm, cmap='Blues')
fig.colorbar(cax)
plt.xlabel('Predicción')
plt.ylabel('Real')
plt.xticks(ticks=np.arange(num_classes), labels=list(train_generator.class_indices.keys()), rotation=45)
plt.yticks(ticks=np.arange(num_classes), labels=list(train_generator.class_indices.keys()))
plt.show()

# Función para capturar y clasificar una imagen con la cámara cada 10 segundos
def clasificar_con_camara():
    # Cargar el modelo
    model = tf.keras.models.load_model('clasificador_boing_color_fresa.h5')

    # Clases
    clases = ['Manzana', 'Mango', 'Uva', 'Fresa', 'Sin producto']

    # Iniciar la cámara
    cap = cv2.VideoCapture(0)

    # Tiempo inicial
    start_time = time.time()

    while True:
        ret, frame = cap.read()
        if ret:
            # Redimensionar la imagen a 128x128
            img_resized = cv2.resize(frame, (img_width, img_height))
            img_array = np.expand_dims(img_resized, axis=0) / 255.0

            # Tiempo transcurrido
            elapsed_time = time.time() - start_time

            # Mostrar predicción cada 10 segundos
            if elapsed_time >= 10:
                # Predicción
                prediccion = model.predict(img_array)
                clase_predicha = clases[np.argmax(prediccion)]

                # Mostrar la clase predicha en la imagen
                cv2.putText(frame, f'Sabor: {clase_predicha}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                # Preguntar si la predicción fue correcta o incorrecta
                print(f'La predicción es: {clase_predicha}')
                print("Presiona 'c' si la predicción es correcta, 'i' si es incorrecta.")

                # Reiniciar el tiempo
                start_time = time.time()

            # Mostrar la imagen con la clase predicha
            cv2.imshow('Clasificador Boing', frame)
            # Romper el bucle con la tecla 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # Registrar si la predicción es correcta o incorrecta
            elif cv2.waitKey(1) & 0xFF == ord('c'):
                print("La predicción fue correcta.")
            elif cv2.waitKey(1) & 0xFF == ord('i'):
                print("La predicción fue incorrecta.")

    # Liberar la cámara y cerrar las ventanas
    cap.release()
    cv2.destroyAllWindows()

# Llamar a la función de clasificación en tiempo real
clasificar_con_camara()
