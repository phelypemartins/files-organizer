import os
import shutil
from PySide6.QtPdfWidgets import *
from PySide6.QtGui import QIcon
from ui_organizador import Ui_MainWindow, QApplication, QMainWindow, QFileDialog
import sys

# Criação da classe
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Organizador de Arquivos') # Definição de título para a janela
        #appIcon = QIcon("_imgs/icone.png")  "Caso eu quisesse definir um ícone dentro da minha janela"
        #self.setWindowIcon(appIcon)

    
        self.file = ''

        #Definição das funcionalidades dos botões
        self.btn_abrir.clicked.connect(self.open_path)
        self.btn_organizar.clicked.connect(self.organizar)
    
    #Comando para selecionar a pasta ao clicar no botão "Abrir"
    def open_path(self):
        self.file = QFileDialog.getExistingDirectory(self, str("Pasta xml"),'/home',QFileDialog.Option.ShowDirsOnly | QFileDialog.Option.DontResolveSymlinks)

        #Enviando o caminho para o txt_path
        self.txt_path.setText(self.file)
        self.file = str(self.file)

    # Comando para organizar os arquivos
    def organizar(self):
        #Definição do caminho para o Path
        path = self.file
        #Pegando a lista de arquivos
        arquivos =  os.listdir(path)
        for arquivo in arquivos:
            filename, extension = os.path.splitext(arquivo)
            extension = extension[1:]
            #Condição para saber se a pasta com nome da extensão existe
            if os.path.exists(path + '/' + extension):
                shutil.move(path + '/' + arquivo, path + '/' + extension + '/' + arquivo)
            #Caso não exista, ele cria uma pasta nova e move os arquivos para dentro dessa pasta    
            else:
                os.makedirs(path + '/' + extension)
                shutil.move(path + '/' + arquivo, path + '/' + extension)

                   

# Execução da interface
if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()      
