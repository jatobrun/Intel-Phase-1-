#importando librerias OpenCV, numpy y el archivo que creamos para pre-procesar las imagenes
import cv2
import numpy as np
from L2-E2-preprocess_inputs import pose_estimation, text_detection, car_meta

# Cargando las imagenes en variables

Pose_Image = cv2.imread("ruta de la imagen") 
Text_Image = cv2.imread("ruta de la imagen")
Car_Image = cv2.imread("ruta de la imagen")

#lista de pruebas
test_names = ["Pose Estimation", "Text Detection", "Car Meta"]

# 

def test(test_func, test_name, test_image):
	new_images = test_fuc(test_image) #pasamos la imagen cargada por la funcion que creamos
def test_pose():
	comparison = test()
