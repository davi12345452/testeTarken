import cv2
import numpy as np

# Carregando a imagem
imagem = cv2.imread('meteor_challenge_01.png')
cv2.imshow('Imagem Original', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Definindo os pontos de cor escolhidos
pontos_escolhidos = [[255, 0, 0], [255, 255, 255]]  # Exemplo de pontos escolhidos (vermelho, verde, azul)

# Convertendo a imagem para o espaço de cores RGB
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Criando uma imagem vazia para armazenar o resultado
imagem_resultado = np.zeros(imagem_rgb.shape, dtype=np.uint8)

# Percorrendo a imagem e aplicando as cores
for y in range(imagem_rgb.shape[0]):
    for x in range(imagem_rgb.shape[1]):
        pixel = imagem_rgb[y, x]
        if pixel.tolist() in pontos_escolhidos:
            imagem_resultado[y, x] = [255, 255, 255]  # Branco
        else:
            vizinhos = []
            if y > 0:
                vizinhos.append(imagem_rgb[y - 1, x])
            if y < imagem_rgb.shape[0] - 1:
                vizinhos.append(imagem_rgb[y + 1, x])
            if x > 0:
                vizinhos.append(imagem_rgb[y, x - 1])
            if x < imagem_rgb.shape[1] - 1:
                vizinhos.append(imagem_rgb[y, x + 1])
            if any(vizinho.tolist() in pontos_escolhidos for vizinho in vizinhos):
                imagem_resultado[y, x] = [100, 100, 100]  # Cinza
            else:
                imagem_resultado[y, x] = [0, 0, 0]  # Preto

cv2.imshow('Imagem Resultado', imagem_resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()