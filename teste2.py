import cv2

# Carregando a imagem
image = cv2.imread('meteor_challenge_01.png')

# Convertendo a imagem para escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicando um filtro de realce de bordas
edges = cv2.Canny(gray_image, 100, 200)

# Encontrando os contornos na imagem
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterando sobre os contornos encontrados
for contour in contours:
    # Obtendo o retângulo delimitador do contorno
    x, y, w, h = cv2.boundingRect(contour)

    # Extraindo a região de interesse (ROI) da imagem original
    roi = image[y:y + h, x:x + w]

    # Faça a análise da ROI para procurar a frase oculta

    # Exemplo: Imprimindo os valores dos pixels na ROI
    for row in roi:
        for pixel in row:
            print(pixel)

# Exiba a imagem original e a imagem processada
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()