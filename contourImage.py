# Importar as bibliotecas
import sys
from PIL import Image, ImageFilter

def run(arg01, arg02):

    # Abrir a Imagem
    img1 = Image.open(arg01)

    # Aplicar o filtro de Contour
    # A aplicação desse filtro resulta em uma imagem preto e branco, destacando os contornos entre os objetos
    # / personagens presentes na imagem
    img2 = img1.filter(ImageFilter.CONTOUR)

    # Salvar a imagem resultante
    img2.save(arg02)

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])