# Importar as bibliotecas
import sys
from PIL import Image, ImageFilter

def run(arg01):
    # Abrir a Imagem
    img1 = Image.open(arg01)

    resp  = ""
    pixels = list(img1.getdata())
    fff = pixels[50][3]
    for i, p in enumerate(pixels):
        resp = resp + chr((255 - pixels[i][3]) + 96)
        #print("verificando = " + str(pixels[i][3]))
        if pixels[i+1][3] == fff:
            break

    print(resp)

if __name__ == "__main__":
    run(sys.argv[1])