# Importar as bibliotecas
import sys
from PIL import Image, ImageFilter

def run(arg01, arg02, arg03):

    # Abrir a Imagem
    img1 = Image.open(arg01)

    if arg03 == '1':
        # Aplicar o espelhamento horizontal
        img2 = img1.transpose(Image.FLIP_LEFT_RIGHT)
        img2.save(arg02)

    elif arg03 == '2':
        # Aplicar o espelhamento horizontal
        img2 = img1.transpose(Image.FLIP_TOP_BOTTOM)
        img2.save(arg02)

    else:
        print("Erro")

    # Salvar a imagem resultante
    print("")

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2], sys.argv[3])