# Importar as bibliotecas
import sys
from PIL import Image, ImageFilter

def run(arg01, arg02):

    # Abrir a Imagem
    img1 = Image.open(arg01)

    # Carregar a imagem para uma matriz
    matriz = img1.load()

    # Fazer a conversão
    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            r = matriz[i, j][0]
            g = matriz[i, j][1]
            b = matriz[i, j][2]
            pixels = int((r + g + b) / 3)
            if pixels > 128:
                resp = 255
            else:
                resp = 0
            matriz[i, j] = (resp, resp, resp)

    # Salvar a imagem resultante
    img1.save(arg02)

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])