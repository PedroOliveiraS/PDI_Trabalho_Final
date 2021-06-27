# Importar as bibliotecas
import sys
from PIL import Image, ImageFilter

def run(arg01, arg02):

    # Abrir a Imagem
    img1 = Image.open(arg01)

    # Aplicar o filtro de Emboss
    # O filtro de edge enhance faz com que as bordas de diferentes regiões estejam presentes de forma muito mais
    # explícita, ficando mais claro a distinção dessas regiões umas das outras (Ainda mais que o edge enhance normal)
    # As bordas chegam quase a brilhar em branco k
    img2 = img1.filter(ImageFilter.EDGE_ENHANCE_MORE)

    # Salvar a imagem resultante
    img2.save(arg02)

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])