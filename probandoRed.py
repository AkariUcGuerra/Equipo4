# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 00:31:37 2024

@author: puchu
"""

import cv2
import numpy as np
import tensorflow as tf
import time

# Dimensiones de las imágenes de entrada (las mismas usadas durante el entrenamiento)
IMG_WIDTH, IMG_HEIGHT = 150, 150

# Cargar el modelo previamente entrenado
model = tf.keras.models.load_model('boing_detector_model.h5')

# Etiquetas de las clases (sabores de Boing)
labels = ['Fresa', 'Manzana', 'Mango', 'Uva']

# Función para preprocesar imagen y hacer predicción
def predict_image(model, image):
    image_resized = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))  # Redimensionar imagen a tamaño adecuado
    image_resized = np.expand_dims(image_resized, axis=0)  # Expandir dimensiones para que sea compatible con el modelo
    image_resized = image_resized / 255.0  # Normalizar como en el entrenamiento
    prediction = model.predict(image_resized)
    return prediction

# Función principal para capturar video en tiempo real y hacer predicciones
def real_time_detection():
    cap = cv2.VideoCapture(2)  # Iniciar captura de video

    while True:
        ret, frame = cap.read()  # Leer cuadro de la cámara
        if not ret:
            break

        # Mostrar imagen capturada
        cv2.imshow('Boing Detector - Esperando 5 segundos...', frame)

        # Esperar 5 segundos antes de hacer una predicción
        start_time = time.time()
        while time.time() - start_time < 5:  # Mantener el bucle durante 5 segundos
            ret, frame = cap.read()  # Actualizar el cuadro de la cámara
            if not ret:
                break
            cv2.imshow('Boing Detector - Esperando 5 segundos...', frame)

            # Salir si se presiona la tecla 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                return

        # Hacer predicción tras 5 segundos
        prediction = predict_image(model, frame)
        confidence = np.max(prediction)
        label_index = np.argmax(prediction)

        # Mostrar el resultado basado en el umbral de confianza
        if confidence >= 0.5:  # Si la confianza es mayor o igual al 90%
            label = labels[label_index]
            print(f'Boing detectado: {label} con {confidence * 100:.2f}% de confianza')
        else:
            print('No se reconoce el objeto. Confianza baja.')

        # Salir si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # Liberar la cámara
    cv2.destroyAllWindows()  # Cerrar todas las ventanas de OpenCV

# Ejecutar la función de detección en tiempo real
real_time_detection()
