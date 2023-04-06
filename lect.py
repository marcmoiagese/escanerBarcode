#!/usr/bin/env python

import cv2
from pyzbar import pyzbar

# Inicialitzem la càmera
cap = cv2.VideoCapture(0)

while True:
    # Llegim el frame de la càmera
    ret, frame = cap.read()

    # Convertim el frame a una imatge en escala de grisos
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Llegim els codis de barres de la imatge en escala de grisos
    codes = pyzbar.decode(gray)

    # Si s'ha llegit algun codi de barres, el mostrem per pantalla
    if codes:
        print('Codi de barres: {}'.format(codes))

    # Mostrem el frame per pantalla
    cv2.imshow('frame', frame)

    # Si l'usuari prem la tecla "q", sortim del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Alliberem la càmera i tanquem les finestres
cap.release()
cv2.destroyAllWindows()
