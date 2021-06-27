# PyQt 5 - Criando interfaces gráficas com o Python

import sys
import subprocess
from PIL import Image
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QGridLayout, QWidget, QMessageBox, QSlider, QFileDialog, QInputDialog
from PyQt5.QtCore import QSize, Qt, QProcess

def run():

    class MyWindow(QMainWindow):
        def __init__(self):
            super(MyWindow, self).__init__()
            self.setup_main_window()
            self.initUI()

        def setup_main_window(self):
            self.x = 1000
            self.y = 450
            self.setMinimumSize(QSize(self.x, self.y))
            self.setWindowTitle("Trabalho - Processamento Digital de Imagens")
            self.wid = QWidget(self)
            self.setCentralWidget(self.wid)
            self.layout = QGridLayout()
            self.wid.setLayout(self.layout)

        def initUI(self):
            # Criando a barra de menu
            self.barraDeMenu = self.menuBar()

            # Criando os menus
            self.menuArquivo = self.barraDeMenu.addMenu("&Arquivo")
            self.menuTransformacoes = self.barraDeMenu.addMenu("&Transformações")
            self.menuRotacoes = self.barraDeMenu.addMenu("&Rotações")
            self.menuSobre = self.barraDeMenu.addMenu("&Sobre")

            # Criando as actions
            ## Action de ABRIR
            self.opcaoAbrir = self.menuArquivo.addAction("&Abrir arquivo")
            self.opcaoAbrir.triggered.connect(self.open_file)
            self.opcaoAbrir.setShortcut("Ctrl+N")

                ## Action de Save File
            self.opcaoSaveFile = self.menuArquivo.addAction("&Salvar Imagem")
            self.opcaoSaveFile.triggered.connect(self.save_file)
            self.opcaoSaveFile.setShortcut("Ctrl+S")

                ## Action de FECHAR
            self.opcaoFechar = self.menuArquivo.addAction("&Fechar programa")
            self.opcaoFechar.triggered.connect(self.close)
            self.opcaoFechar.setShortcut("Ctrl+X")


            ## Action de SOBRE APP
            self.opcaoSobreSobre = self.menuSobre.addAction("&Sobre o aplicativo")
            self.opcaoSobreSobre.triggered.connect(self.exibir_mensagem)

            ## Action de SOBRE Imagem
            self.opcaoSobreImg = self.menuSobre.addAction("&Sobre a Imagem")
            self.opcaoSobreImg.triggered.connect(self.exibir_mensagem_imagem)

            ## Action de Converter uma imagem colorida para uma imagem com filtro de gamma
            self.opcaoGamma = self.menuTransformacoes.addAction("&Correção Gama")
            self.opcaoGamma.triggered.connect(self.transform_gamma)

            ## Action de Converter uma imagem colorida para uma imagem com filtro de negativo
            self.opcaoNegativo = self.menuTransformacoes.addAction("&Negativo")
            self.opcaoNegativo.triggered.connect(self.transform_negativo)

                ## Action de Converter uma imagem colorida para uma imagem com filtro de Blur
            self.opcaoBlur = self.menuTransformacoes.addAction("&Blur")
            self.opcaoBlur.triggered.connect(self.transform_blur)
            self.opcaoBlur.setShortcut("Ctrl+B")

            ## Action de Converter uma imagem colorida para uma imagem com filtro de Conntour
            self.opcaoContour = self.menuTransformacoes.addAction("&Contour")
            self.opcaoContour.triggered.connect(self.transform_contour)
            self.opcaoContour.setShortcut("Ctrl+C")

            ## Action de Converter uma imagem colorida para uma imagem com filtro de Detail
            self.opcaoDetail = self.menuTransformacoes.addAction("&Detail")
            self.opcaoDetail.triggered.connect(self.transform_detail)
            self.opcaoDetail.setShortcut("Ctrl+D")

            ## Action de Converter uma imagem colorida para uma imagem com filtro de Edge Enhance
            self.opcaoEdge = self.menuTransformacoes.addAction("&Edge Enhance")
            self.opcaoEdge.triggered.connect(self.transform_edge)

            ## Action de Converter uma imagem colorida para uma imagem com filtro de Edge Enhance More
            self.opcaoEdgeMore = self.menuTransformacoes.addAction("&Edge Enhance More")
            self.opcaoEdgeMore.triggered.connect(self.transform_edgeMore)

            ## Action de Converter uma imagem colorida para uma imagem com filtro de Emboss
            self.opcaoEmboss = self.menuTransformacoes.addAction("&Emboss")
            self.opcaoEmboss.triggered.connect(self.transform_emboss)
            self.opcaoEmboss.setShortcut("Ctrl+E")

            ## Action de Converter uma imagem colorida para uma imagem com filtro de Edges
            self.opcaoFindEdge = self.menuTransformacoes.addAction("&Find Edges")
            self.opcaoFindEdge.triggered.connect(self.transform_edges)
            self.opcaoFindEdge.setShortcut("Ctrl+F")

            ## Action de Converter uma imagem colorida para uma imagem com filtro de Sharpen
            self.opcaoSharpen = self.menuTransformacoes.addAction("&Sharpen")
            self.opcaoSharpen.triggered.connect(self.transform_sharpen)

            ## Action de Converter uma imagem colorida para uma imagem com filtro de Smooth
            self.opcaoSmooth = self.menuTransformacoes.addAction("&Smooth")
            self.opcaoSmooth.triggered.connect(self.transform_smooth)

            ## Action de Converter uma imagem colorida para uma imagem com filtro de Smooth More
            self.opcaoSmoothMore = self.menuTransformacoes.addAction("&Smooth More")
            self.opcaoSmoothMore.triggered.connect(self.transform_smoothMore)

            ## Action de Converter uma imagem colorida para uma imagem em Grayscale
            self.opcaoGrayscale = self.menuTransformacoes.addAction("&Grayscale")
            self.opcaoGrayscale.triggered.connect(self.trasnform_grayscale)
            self.opcaoGrayscale.setShortcut("Ctrl+G")

            ## Action de Converter uma imagem colorida para uma imagem com filtro de de detecção de borda 01
            self.opcaoBorda1 = self.menuTransformacoes.addAction("&Detecção de Bordas 01")
            self.opcaoBorda1.triggered.connect(self.transform_bordaum)

            ## Action de Converter uma imagem colorida para uma imagem com filtro de detecção de borda 02
            self.opcaoBorda2 = self.menuTransformacoes.addAction("&Detecção de Bordas 02")
            self.opcaoBorda2.triggered.connect(self.transform_bordadois)

            ## Action de Converter uma imagem colorida para uma imagem com filtro de detecção de borda 03
            self.opcaoBorda3 = self.menuTransformacoes.addAction("&Detecção de Bordas 03")
            self.opcaoBorda3.triggered.connect(self.transform_bordatres)

            ## Action de Converter uma imagem colorida para uma imagem com filtro de preto ebranco
            self.opcaoPretoEBranco = self.menuTransformacoes.addAction("&Preto e Branco")
            self.opcaoPretoEBranco.triggered.connect(self.transform_pretobranco)

            ## Action de Converter uma imagem colorida para uma imagem com filtro de separar o canal R
            self.opcaoR = self.menuTransformacoes.addAction("&Separar canal R")
            self.opcaoR.triggered.connect(self.transform_R)

            ## Action de Converter uma imagem colorida para uma imagem com filtro de separar o canal G
            self.opcaoG = self.menuTransformacoes.addAction("&Separar canal G")
            self.opcaoG.triggered.connect(self.transform_G)

            ## Action de Converter uma imagem colorida para uma imagem com filtro de separar o canal B
            self.opcaoB = self.menuTransformacoes.addAction("&Separar canal B")
            self.opcaoB.triggered.connect(self.transform_B)

            ## Action de Converter uma imagem colorida para uma imagem com filtro de separar o canal B
            self.opcaoB = self.menuTransformacoes.addAction("&Inserir mensagem secreta")
            self.opcaoB.triggered.connect(self.esteganografia_in)

            ## Action de Converter uma imagem colorida para uma imagem com filtro de separar o canal B
            self.opcaoB = self.menuTransformacoes.addAction("&Recuperar mensagem secreta")
            self.opcaoB.triggered.connect(self.esteganografia_out)

            ## Action de Rotacionar a esquerda
            self.opcaoRotacaoEsquerda = self.menuRotacoes.addAction("Rotacionar &Esquerda")
            self.opcaoRotacaoEsquerda.triggered.connect(self.rotacionar_esquerda)
            self.opcaoRotacaoEsquerda.setShortcut("Ctrl+Alt+E")

            ## Action de Rotacionar a direita
            self.opcaoRotacaoDireita = self.menuRotacoes.addAction("Rotacionar &Direita")
            self.opcaoRotacaoDireita.triggered.connect(self.rotacionar_direita)
            self.opcaoRotacaoDireita.setShortcut("Ctrl+Alt+D")

            ## Action de Espelhar Verticalmente
            self.opcaoEspelharVerticalmente = self.menuRotacoes.addAction("E&spelhar &Verticalmente")
            self.opcaoEspelharVerticalmente.triggered.connect(self.espelhar_verticalmente)
            self.opcaoEspelharVerticalmente.setShortcut("Ctrl+Alt+V")

            ## Action de Espelhar Horizontalmente
            self.opcaoEspelharVerticalmente = self.menuRotacoes.addAction("E&spelhar &Horizontalmente")
            self.opcaoEspelharVerticalmente.triggered.connect(self.espelhar_horizontalmente)
            self.opcaoEspelharVerticalmente.setShortcut("Ctrl+Alt+H")

            # Criar os outros widgets (Label, Button, Text, Image)

            # Criando um QLabel para o texto
            self.texto = QLabel("Trabalho - Processamento de Imagens", self)
            self.texto.adjustSize()
            self.texto.setAlignment(QtCore.Qt.AlignCenter)

            # Criando um QLabel para o QSlider
            self.textoSlider = QLabel("Transparência", self)
            self.textoSlider.adjustSize()
            self.textoSlider.setAlignment(QtCore.Qt.AlignCenter)

            # Criando um QSlider
            self.slider = QSlider(Qt.Vertical, self)
            self.slider.setRange(0, 100)
            self.slider.setFocusPolicy(Qt.NoFocus)
            self.slider.setValue(100)
            self.slider.setGeometry(900, 120, 15, 300)

            self.slider.sliderReleased.connect(self.change_transparency)

            # Criando as imagens
            self.imagem1 = QLabel(self)
            self.endereco1 = 'images/colored_1.jpg'
            self.pixmap1 = QtGui.QPixmap(self.endereco1)
            self.pixmap1 = self.pixmap1.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
            self.imagem1.setPixmap(self.pixmap1)
            self.imagem1.setAlignment(QtCore.Qt.AlignCenter)

            self.imagem2 = QLabel(self)
            self.endereco2 = 'images/colored_1.jpg'
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)
            self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

            # Organizando os widgets dentro do gridLayout
            self.layout.addWidget(self.texto, 0, 0, 1, 2)
            self.layout.addWidget(self.textoSlider, 1, 2, alignment=Qt.AlignCenter)
            self.layout.addWidget(self.imagem1, 2, 0)
            self.layout.addWidget(self.imagem2, 2, 1)
            self.layout.setRowStretch(0, 0)
            self.layout.setRowStretch(2,1)

            self.p = None;

        # Método para ações dos botões
        def esteganografia_in(self):
            text, msg = QInputDialog.getText(self, 'input dialog', 'Insira a curta mensagem secreta que você deseja inserir na imagem')
            if msg:
                print(str(text))
                self.entrada = self.endereco1
                self.saida = 'images/converted_mesageIn.png'
                print(self.entrada[:-4])
                self.script = './esteganografia.py'
                self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + '\"' + \
                               self.saida + '\" ' + str(text)
                print(self.program)
                subprocess.run(self.program, shell=True)
                self.end_transform()


        def esteganografia_out(self):
            self.entrada = self.endereco1
            print(self.entrada[:-4])
            self.script = './esteganoout.py'
            if self.p is None:
                self.p = QProcess()
                self.p.readyReadStandardOutput.connect(self.handle_stdout)
                self.p.readyReadStandardError.connect(self.handle_stderr)
                self.p.finished.connect(self.finalizar)
                self.p.start("python", [self.script, self.entrada])

        def finalizar(self):
            #self.message = "acabou bolsoanro"
            #print(self.message)
            self.p = None;

        def save_file(self):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "imagem.png",
                                                      filter='All files (*.*);; Images (*.jpg;*.png)'
                                                      "All Files (*);;Text Files (*.txt)", options=options)
            if fileName:
                print(fileName)
                fileName = fileName + '.png'
                img1 = Image.open(self.endereco2)
                img1.save(fileName)

        def open_file(self):
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                caption='Open image',
                                                                directory=QtCore.QDir.currentPath(),
                                                                filter='All files (*.*);; Images (*.jpg;*.png)',
                                                                initialFilter='Images (*.jpg;*.png)')
            print(fileName)
            if fileName != ' ':
                self.endereco1 = fileName
                self.pixmap1 = QtGui.QPixmap(self.endereco1)
                self.pixmap1 = self.pixmap1.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
                self.imagem1.setPixmap(self.pixmap1)
                self.saida = self.endereco1
                self.end_transform()

        def transform_gamma(self):
            text, msg = QInputDialog.getText(self, 'input dialog',
                                             'Insira o gamma desejado (0.5, 1, 1.5, 2, 2.5, 3.0')
            if msg:
                print(str(text))
                self.entrada = self.endereco1
                self.saida = 'images/converted_gamma.png'
                print(self.entrada[:-4])
                self.script = './correcaogama.py'
                self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + '\"' + \
                               self.saida + '\" ' + str(text)
                print(self.program)
                subprocess.run(self.program, shell=True)
                self.end_transform()

        def transform_edge(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_enhance.png'
            print(self.entrada[:-4])
            self.script = './edgeEnhance.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_negativo(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_negativo.png'
            print(self.entrada[:-4])
            self.script = './negative.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_edgeMore(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_enhanceMore.png'
            print(self.entrada[:-4])
            self.script = './edgeEnhanceMore.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_sharpen(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_sharpen.png'
            print(self.entrada[:-4])
            self.script = './sharpen.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_smooth(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_smooth.png'
            print(self.entrada[:-4])
            self.script = './smooth.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_smoothMore(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_smoothMore.png'
            print(self.entrada[:-4])
            self.script = './smoothMore.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_bordaum(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_detBorda01.png'
            print(self.entrada[:-4])
            self.script = './bordaum.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_bordadois(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_detBorda02.png'
            print(self.entrada[:-4])
            self.script = './bordadois.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_bordatres(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_detBorda03.png'
            print(self.entrada[:-4])
            self.script = './bordatres.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_pretobranco(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_pretoebranco.png'
            print(self.entrada[:-4])
            self.script = './pretobranco.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_R(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_channelR.png'
            print(self.entrada[:-4])
            self.script = './RBGChannels.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + '\"' + \
                           self.saida + '\" r'
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_G(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_channelG.png'
            print(self.entrada[:-4])
            self.script = './RBGChannels.py'

            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + '\"' + \
                           self.saida + '\" g'
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_B(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_channelB.png'
            print(self.entrada[:-4])
            self.script = './RBGChannels.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + '\"' + \
                           self.saida + '\" b'
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_blur(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_blur.png'
            print(self.entrada[:-4])
            self.script = './blurImage.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_contour(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_contour.png'
            print(self.entrada[:-4])
            self.script = './contourImage.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_detail(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_detail.png'
            print(self.entrada[:-4])
            self.script = './detailImage.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_emboss(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_emboss.png'
            print(self.entrada[:-4])
            self.script = './embossImage.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def transform_edges(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_edges.png'
            print(self.entrada[:-4])
            self.script = './findEdgesImage.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def trasnform_grayscale(self):
            self.entrada = self.endereco1
            self.saida = 'images/converted_grayscale.png'
            print(self.entrada[:-4])
            self.script = './grayscaleImage.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' +  '\"' + self.saida + '\" '
            print(self.program)
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def end_transform(self):
            self.endereco2 = self.saida
            self.pixmap2 = QtGui.QPixmap(self.endereco2)
            self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
            self.imagem2.setPixmap(self.pixmap2)

        def exibir_mensagem(self):
            self.mensagem = QMessageBox()
            self.mensagem.setIcon(QMessageBox.Information)
            self.mensagem.setWindowTitle("Informativo")
            self.mensagem.setText("Trabalho Final de Processamento Digital de Imagens")
            self.mensagem.setInformativeText("Alunos: \nIasmin Quirino Moura\nPedro Ottávio de Oliveira Silva\n"
                                          "Ituiutaba, Minas Gerais\n"
                                          "Data da última atualização: 25/06/2021")

            self.mensagem.exec_()

        def exibir_mensagem_imagem(self):
            newimagepy = Image.open(self.endereco1)
            nomeArquivo = newimagepy.filename.split('/')[-1]
            width, height = newimagepy.size
            typ = newimagepy.format


            self.mensagem = QMessageBox()
            self.mensagem.setIcon(QMessageBox.Information)
            self.mensagem.setWindowTitle("Informativo")
            self.mensagem.setText("Informações sobre a Imagem")
            self.mensagem.setInformativeText("Nome do arquivo: " + nomeArquivo + "\nTipo do arquivo:" + str(typ) + "\n"
                                                                       "Largura: " + str(width) + "\nAltura: " + str(height))
            self.mensagem.exec_()

        def rotacionar_esquerda(self):
            self.entrada = self.endereco2
            self.saida = 'images/imageRotacionada.png'
            print(self.entrada[:-4])
            self.script = './rotacionar.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' +  '\"' + \
                           self.saida + '\" 1'
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def rotacionar_direita(self):
            self.entrada = self.endereco2
            self.saida = 'images/imageRotacionada.png'
            print(self.entrada[:-4])
            self.script = './rotacionar.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + '\"' + \
                           self.saida + '\" 2'
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def espelhar_horizontalmente(self):
            self.entrada = self.endereco2
            self.saida = 'images/imageEspelhada.png'
            print(self.entrada[:-4])
            self.script = 'espelhar.py'
            self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + '\"' + \
                           self.saida + '\" 1'
            subprocess.run(self.program, shell=True)
            self.end_transform()

        def espelhar_verticalmente(self):
            self.entrada = self.endereco2
            self.saida = 'images/imageEspelhada.png'
            print(self.entrada[:-4])
            self.script = 'espelhar.py'
            self.terceiro = '2'
            #self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + '\"' + \
            #               self.saida + '\" 2'
            #print(self.program)
            # subprocess.run(self.program, shell=True)
            #self.end_transform()
            if self.p is None:
                #self.message = "Rodando o processo"
                #print(self.message)
                self.p = QProcess()

                self.p.readyReadStandardOutput.connect(self.handle_stdout)
                self.p.readyReadStandardError.connect(self.handle_stderr)


                self.p.finished.connect(self.process_finished)
                self.program = [self.script, self.entrada, self.saida, self.terceiro]
                print(self.program)
                self.p.start("python", [self.script, self.entrada, self.saida, self.terceiro])


        def handle_stderr(self):
            data = self.p.readAllStandardError()
            stderr = bytes(data).decode("utf8")
            print("strderr" + stderr)

        def handle_stdout(self):
            data = self.p.readAllStandardOutput()
            stdout = bytes(data).decode("utf8")
            #self.saida = stdout
            print("stdout = " + stdout)
            self.mensagem = QMessageBox()
            self.mensagem.setIcon(QMessageBox.Information)
            self.mensagem.setWindowTitle("Informativo")
            self.mensagem.setText("Mensagem Recuperada")
            self.mensagem.setInformativeText(stdout)

            self.mensagem.exec_()

        def process_finished(self):
            self.message = "acabou bolsoanro"
            print(self.message)
            self.p = None;
            self.end_transform()

        def change_transparency(self):
            value = self.slider.value()
            self.terceiro = int((255 * value)  / 100)
            self.entrada = self.endereco2
            self.saida = 'images/imageTransparency.png'
            print(self.entrada[:-4])
            self.script = './mudarTransparencia.py'
            if self.p is None:
                self.message = "Rodando o processo"
                print(self.message)
                self.p = QProcess()
                self.p.readyReadStandardOutput.connect(self.handle_stdout)
                self.p.readyReadStandardError.connect(self.handle_stderr)
                self.p.finished.connect(self.process_finished)
                #self.program = [self.script, self.entrada, self.saida, self.terceiro]
                #print(self.program)
                self.p.start("python", [self.script, self.entrada, self.saida, str(self.terceiro)])

    def window():
        app = QApplication(sys.argv)
        win = MyWindow()
        win.show()
        sys.exit(app.exec_())

    window()

if __name__== "__main__":
    run()