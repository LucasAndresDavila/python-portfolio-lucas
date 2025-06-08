from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

image = mpimg.imread('example.jpg')

if image.dtype == np.float32 or image.max() <= 1.0:
    image = (image * 255).astype(np.uint8)

w, h, d = image.shape
pixels = image.reshape((w * h, d))

n_colors = 10
model = KMeans(n_clusters=n_colors, random_state=42).fit(pixels)
palette = np.uint8(model.cluster_centers_)

plt.imshow([palette])
plt.axis('off')
plt.title('Paleta de colores obtenidos')
plt.show()