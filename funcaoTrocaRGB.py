import cv2
import numpy as np

imagem = cv2.imread('meteor_challenge_01.png')
cv2.imshow('Imagem Original', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

rgb_image = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

rgbImageList = rgb_image.tolist()

def converter_imagem(rgb):
    for y in range(704):
        for x in range(704):
            if rgbImageList[y][x] in rgb:
                rgbImageList[y][x] = [255, 255, 255]
            else:
                rgbImageList[y][x] = [100, 100, 100]

    rgb_Image = np.array(rgbImageList, dtype=np.uint8)
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # Realizando a dilatação
    imagem_engrossada = cv2.dilate(rgb_Image, elemento_estruturante, iterations=1)

    cv2.imshow('Imagem Processada', cv2.cvtColor(rgb_Image, cv2.COLOR_RGB2BGR))
    cv2.imshow('Imagem Engrossada', cv2.cvtColor(imagem_engrossada, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

converter_imagem([[255, 0, 0]])
