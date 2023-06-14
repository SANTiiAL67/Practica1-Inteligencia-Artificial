# Practica2-Inteligencia-Artificial

El link al github es: https://github.com/SANTiiAL67/Practica1-Inteligencia-Artificial

Título: Modelo clasificación
Objetivo: El objetivo de esta práctica es la construcción de dos modelos de
clasificación, uno de texto y otro de imágenes. Los datos que usaremos son los
recolectados en la práctica 1.
Instrucciones:
1. Modelos:
• Clasificador texto: los alumnos deberán entrenar un modelo de
clasificación de texto, para distinguir entre sinopsis de “horror” y
comedia en Español.
• Clasificador de imágenes: los alumnos deberán entrenar un modelo de
clasificación de imágenes, para ser capaces de clasificar entre las
diferentes clases que recolectaron de Wallapop.
2. Feature extraction:
• Texto: Se pueden usar técnicas clásicas como BOW, o probar técnicas
más avanzadas de extracción de características de los textos.
• Imagen: Se deberá usar un modelo pre-entrenado para la extracción de
características, hay muchos modelos disponibles, la elección es libre de
cada grupo (https://keras.io/api/applications/).
3. Visualización:
• Imagen: los alumnos deberán visualizar las imágenes en un espacio de
dos dimensiones y en un espacio de tres dimensiones. Para ello tendrán
que usar los vectores extraídos de las imágenes, alguna técnica de
reducción de dimensiones para poder visualizarlo.
4. Puesta en “producción”:
• Texto: el clasificador de texto deberá implementarse en un servicio para
poder ser consumido por peticiones “http”, para la implementación del
servicio los alumnos se pueden apoyar en Flask o FastApi. Este servicio
se usará desde un front, este se encuentra disponible en el campus
Unidad 2 “Front ML model”.
5. Entrega:
• La entrega se evaluará mediante:
• Un zip con el código y los modelos.
• La revisión del cumplimento de los objetivos.
