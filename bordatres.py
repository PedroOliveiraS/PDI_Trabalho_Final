# Importar as bibliotecas
import sys
from PIL import Image, ImageFilter

def run(arg01, arg02):

    # Abrir a Imagem
    img1 = Image.open(arg01)

    # Criar o Kernel
    kernel = ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8, -1, -1, -1, -1), 1, 0)

    # Aplicar o filtro na imagem
    img2 = img1.filter(kernel)

    # Salvar a imagem
    img2.save(arg02)

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])