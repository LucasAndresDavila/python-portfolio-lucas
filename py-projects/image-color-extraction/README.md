**Extracción de Colores con KMeans**


**Descripción del Proyecto**
Este script en Python aplica K-Means clustering para identificar los colores predominantes en una imagen. Utiliza aprendizaje no supervisado para segmentar los píxeles en grupos cromáticos representativos, permitiendo visualizar la paleta de colores dominante de manera objetiva.

**Propósito y Aplicaciones**
El algoritmo de clustering permite extraer patrones cromáticos con múltiples aplicaciones, tales como:
- *Diseño gráfico y branding:* Identificación de paletas de colores para material visual.
- *Procesamiento de imágenes:* Segmentación de color para análisis computacional.
- *Visualización de datos:* Representación de patrones de color en conjuntos de imágenes.

**Funcionamiento del Script**
- Carga la imagen (example.jpg) desde el directorio local.
- Convierte la imagen a un arreglo de píxeles en formato RGB.
- Normaliza los valores para garantizar una correcta segmentación.
- Aplica el algoritmo KMeans para encontrar los n colores principales.
- Genera una paleta visual con los colores detectados.

**Requisitos**
Asegúrate de tener Python 3 instalado y ejecuta los siguientes comandos para instalar las dependencias:
- pip install numpy matplotlib scikit-learn Pillow

**Posibles Mejoras**
- Ajuste dinámico de n_colors basado en la imagen.
- Implementación de métricas para evaluar la segmentación de colores.
- Integración con una interfaz gráfica para una visualización interactiva.

**Autor**
Proyecto desarrollado por *Lic. Lucas Andrés Dávila*, técnico en Data Science, con experiencia en clustering y análisis de datos aplicado.
