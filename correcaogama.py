# Importar as bibliotecas
import sys
from PIL import Image, ImageFilter

def run(arg01, arg02, arg03):
    # Abrir a imagem
    img = Image.open(arg01)

    matriz = img.load()
    gamma = float(arg03)

    # Realizar as operações pixela pixel de transformações
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = int((matriz[i, j][0] / 255) ** gamma * 255)
            g = int((matriz[i, j][1] / 255) ** gamma * 255)
            b = int((matriz[i, j][2] / 255) ** gamma * 255)
            matriz[i, j] = (r, g, b)

    # Salvar a imagem
    img.save(arg02)

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2], sys.argv[3])