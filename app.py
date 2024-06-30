import urllib.request
import mejor_calidad

imagen_url = 'https://ejemplo.com/imagen.jpg'

# Descargar la imagen desde la URL
req = urllib.request.urlopen(imagen_url)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr, -1)

# Mejorar la calidad de la imagen utilizando el módulo
imagen_mejorada = mejorar_calidad.mejorar_calidad_imagen(img)

# Guardar la imagen mejorada
cv2.imwrite("imagen_mejorada.jpg", imagen_mejorada)
