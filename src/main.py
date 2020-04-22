from PyQt5 import QtWidgets
from view.graphicTela import graphicTela
from view.telaOsciloscopio import telaOsciloscopio
from controller.controllerI2C import controllerI2C
from controller.GerenciadorEventos import GerenciadorEventos
import sys

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = telaOsciloscopio()
        self.ui.setupUi(self)

        self.scene = QtWidgets.QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        self.graphicTela = graphicTela(
            self.ui.graphicsView, self.scene)
        self.ui.graphicsView.drawBackground = self.graphicTela.drawBackground


def execute_oscilloscope(app=QtWidgets.QApplication(sys.argv), aplicacao=ApplicationWindow()):
    aplicacao.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    aplicacao = ApplicationWindow()
    GerenciadorEventos = GerenciadorEventos(
        aplicacao.ui, aplicacao.graphicTela, controllerI2C())
    GerenciadorEventos.run()
    execute_oscilloscope(app, aplicacao)
