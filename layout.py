#Passos para importar o PyQt
#1.entrar na pasta Scripts no local do instalação do python
#    Para fazer isso:
#2. buscar no windows por python
#3. Mouse, tecla direita, abrir local do arquivo
#4. Novamente, abrir local do arquivo
#5. Abrir pasta Scripts
#6. Copiar o caminho mostrado
#7. Prompt de comando
#8. CD <colar o caminho>
#9. pip install pyqt5

#layout.py
#exemplos de interfaces usando PyQt
#github.com\pyqt\examples

from PyQt5.QtWidgets import *

def botao_clicado1():
    alerta=QMessageBox()
    alerta.setText('Você clicou no botão Esquerdo!')
    alerta.exec_()

def botao_clicado2():
    alerta=QMessageBox()
    alerta.setText('Você clicou no botão Direito!')
    alerta.exec_()


#cria uma aplicação
app= QApplication([])

btDireito=QPushButton('Direito')
btEsquerdo=QPushButton('Esquerdo')

btEsquerdo.clicked.connect(botao_clicado1)
btDireito.clicked.connect(botao_clicado2)

#define layout horizontal (retire H e bote V para vertical)
layout= QHBoxLayout()
layout.addWidget(btEsquerdo)
layout.addWidget(btDireito)

#define uma janela gráfica
window=QWidget()
window.setLayout(layout)
window.show()

app.exec_()
