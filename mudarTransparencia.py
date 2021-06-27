# Importar as bibliotecas
import sys
from PIL import Image, ImageFilter

def run(arg01, arg02, arg03):

    # Abrir a Imagem
    img1 = Image.open(arg01)

    # Converter a imagem para JPG
    imgpng = img1.convert('RGBA')

    pixels = list(imgpng.getdata())

    for i, p in enumerate(pixels):
        alpha = int(arg03)
        pixels[i] = (p[0], p[1], p[2], alpha)

    outputImg = Image.new('RGBA', img1.size)

    # Inserir os pixels alterados
    outputImg.putdata(pixels)

    # Salvar a iamgem nova
    outputImg.save(arg02)

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2], sys.argv[3])