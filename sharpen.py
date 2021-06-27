# Importar as bibliotecas
import sys
from PIL import Image, ImageFilter

def run(arg01, arg02):

    # Abrir a Imagem
    img1 = Image.open(arg01)

    # Aplicar o filtro de Emboss
    # O filtro de emboss cria uma imagem denotando as diferentes regiões como se fossem relevos de diferentes alturas
    # regiões diferentes possuem claramente um relevo diferente umas das outras
    img2 = img1.filter(ImageFilter.SHARPEN)

    # Salvar a imagem resultante
    img2.save(arg02)

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])