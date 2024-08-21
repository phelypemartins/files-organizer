## Organizador de arquivos com Python

Solução: Esse programa foi desenvolvido para organizar arquivos em pastas no computador de acordo com as extensões. Nasceu devido a uma necessidade de organizar arquivos que são baixados na máquina e ficam empilhados gerando bagunça na pasta.

### Principais bibliotecas utilizadas

• import os \
• import shutil \
• from PySide6.QtPdfWidgets \
• from PySide6.QtGui \
• from ui_organizador \
• import sys

### Uma solução conveniente

Organizando os arquivos por extensão, podemos ter uma visão macro de arquivos que não estão mais em uso. Por exemplo, arquivos de imagem com extensões JPEG ou PNG podem ser facilmente encontrados e deletados quando juntados em uma mesma pasta.

### Tecnologias utilizadas

• VS Code \
• Pyhon \
• QT Desing

### Como utilizar o programa através de um instalador?

Sem ícone na interface: \
No terminal, digite: `pyinstaller --onefile --windowed organizador.py`

Com ícone na interface: \
No terminal, digite: `pyinstaller --onefile --windowed --icon=icone.png organizador.py`

Obs.: Caso queira adicionar um ícone a sua janela, deverá colocar o ícone em formato PNG dentro do diretório do programa e entrar com o seguinte código abaixo:

```python
appIcon = QIcon("_imgs/icone.png")
self.setWindowIcon(appIcon)
```

