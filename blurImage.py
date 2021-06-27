# Importar as bibliotecas
import sys
from PIL import Image, ImageFilter

def run(arg01, arg02):

    # Abrir a Imagem
    img1 = Image.open(arg01)

    # Aplicar o filtro Blur
    # Esse filtro aplica um efeito de embaçamento / enevoamento na imagem
    img2 = img1.filter(ImageFilter.BLUR)

    # Salvar a imagem resultante
    img2.save(arg02)

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])