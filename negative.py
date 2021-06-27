# Importar as bibliotecas
import sys
from PIL import Image, ImageFilter

def run(arg01, arg02):

    # Abrir a Imagem
    img1 = Image.open(arg01)

    # Carregar a imagem para uma matriz
    matriz = img1.load()

    # Realizar as operações pixela pixel de transformações
    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            r = 255 - matriz[i, j][0]  # retorna uma tupla (r, g, b)
            g = 255 - matriz[i, j][1]
            b = 255 - matriz[i, j][2]
            matriz[i, j] = (r, g, b)

    # Salvar a imagem resultante
    img1.save(arg02)

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])