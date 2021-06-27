# Importar as bibliotecas
import sys
from PIL import Image, ImageFilter

def run(arg01, arg02, arg03):

    # Abrir a Imagem
    img1 = Image.open(arg01)

    # Carregar a imagem para uma matriz
    matriz = img1.load()
    if arg03 == 'r':
        # Realizar as operações da transformação pixel de transformações
        for i in range(img1.size[0]):
            for j in range(img1.size[1]):
                r = matriz[i, j][0]
                g = 0  # g = matriz[i,j][1]
                b = 0  # b = matriz[i,j][2]
                matriz[i, j] = (r, g, b)

    elif arg03 == 'g':
        for i in range(img1.size[0]):
            for j in range(img1.size[1]):
                r = 0  # r = matriz[i,j][0]
                g = matriz[i, j][1]
                b = 0  # b = matriz[i,j][2]
                matriz[i, j] = (r, g, b)

    elif arg03 == 'b':
        for i in range(img1.size[0]):
            for j in range(img1.size[1]):
                r = 0  # r = matriz[i,j][0]
                g = 0  # g = matriz[i,j][1]
                b = matriz[i, j][2]
                matriz[i, j] = (r, g, b)

    else:
        print("error")

    img2 = img1

    # Salvar a imagem resultante
    img2.save(arg02)

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2], sys.argv[3])