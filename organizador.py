import os
import shutil
from PySide6.QtPdfWidgets import *
from PySide6.QtGui import QIcon
from ui_organizador import Ui_MainWindow, QApplication, QMainWindow, QFileDialog
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Organizador de Arquivos')

    
        self.file = ''
        self.btn_abrir.clicked.connect(self.open_path)
        self.btn_organizar.clicked.connect(self.organizar)
    
    def open_path(self):
        self.file = QFileDialog.getExistingDirectory(self, str("Pasta xml"),'/home',QFileDialog.Option.ShowDirsOnly | QFileDialog.Option.DontResolveSymlinks)

        self.txt_path.setText(self.file)
        self.file = str(self.file)

    def organizar(self):
        path = self.file
        arquivos =  os.listdir(path)
        for arquivo in arquivos:
            filename, extension = os.path.splitext(arquivo)
            extension = extension[1:]
            if os.path.exists(path + '/' + extension):
                shutil.move(path + '/' + arquivo, path + '/' + extension + '/' + arquivo)
            else:
                os.makedirs(path + '/' + extension)
                shutil.move(path + '/' + arquivo, path + '/' + extension)

                   


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()      
