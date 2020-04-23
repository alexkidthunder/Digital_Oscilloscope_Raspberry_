import sys
from PyQt5 import QtWidgets
from view.graphicTela import graphicTela
from view.telaOsciloscopio import telaOsciloscopio
from controller.controllerI2C import controllerI2C
from controller.GerenciadorEventos import GerenciadorEventos

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = telaOsciloscopio()
        self.ui.programacao(self)
        self.scene = QtWidgets.QGraphicsScene()
        self.ui.graficview.setScene(self.scene)
        self.graphicTela = graphicTela(self.ui.graficview, self.scene)
        self.ui.graficview.drawBackground = self.graphicTela.drawBackground

def executavel(app=QtWidgets.QApplication(sys.argv), aplicacao=ApplicationWindow()):
    aplicacao.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    aplicacao = ApplicationWindow()
    # GerenciadorEventos coordena entre pegar os dados, conversão e a sua amostragem na tela
    GerenciadorEventos = GerenciadorEventos(aplicacao.ui, aplicacao.graphicTela, controllerI2C())
    # Da inicio na Thread
    GerenciadorEventos.run()
    executavel(app, aplicacao)
