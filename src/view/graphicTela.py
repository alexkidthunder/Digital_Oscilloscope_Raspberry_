from PyQt5 import QtWidgets, QtGui, QtCore


class graphicTela:
    def __init__(self, graphicsView, scene):
        self.__graphicsView = graphicsView
        self.__scene = scene
        self.__pens = (
            QtGui.QPen(QtGui.QColor(156, 255, 157)), # Cores da linha do canal 1
            QtGui.QPen(QtGui.QColor(255, 255, 0))    # Cores da linha do canal 2
        )
        self.__paths = (
            QtGui.QPainterPath(),
            QtGui.QPainterPath(),
            QtGui.QPainterPath()
        )
        self.__channels_settings = (
            {
                "escala": {"vertical": 0.5, "horizontal": 0.1},
                "visivel": False
            },
            {
                "escala": {"vertical": 0.5, "horizontal": 0.1},
                "visivel": False
            }
        )
        self.__screen_size = {
            "width": 0,
            "height": 0,
            "tamanhocelula": 32
        }

    # Definido a escala Horizontal
    def definirEscalaHorizontal(self, novaEscala=1, channel=0):
        settings = self.__channels_settings[channel]
        settings.get("escala").update({"horizontal": novaEscala / 10})

    # Definido a escala Vertical
    def definirEscalaVertical(self, novaEscala=1, channel=0):
        settings = self.__channels_settings[channel]
        settings.get("escala").update({"vertical": novaEscala / 10})

    def visibilidadeCanal(self, channel=0, visible=True):
        self.__channels_settings[channel].update({"visivel": visible})#####

    # Desenhar a tela de fundo do osciloscópio 
    def drawBackground(self, painter, rect):
        background_brush = QtGui.QBrush(
            QtGui.QColor(10, 10, 10), QtCore.Qt.SolidPattern) # coloração de fundo
        painter.fillRect(rect, background_brush)
        pen = QtGui.QPen(QtGui.QColor(255, 255, 255)) # Core das linas
        pen.setWidth(1)
        painter.setPen(pen)
        allLines = []
        horigin = int(rect.height() / -1)
        worigin = int(rect.width() / -1)
        self.__screen_size.update(
            {"width": rect.width(), "height": rect.height()})
        
        # Desenhar as colunas para direita e para esquerda
        for column in range(0, int(rect.height()), self.__screen_size.get("tamanhocelula")):
            line = QtCore.QLineF(worigin, column, int(rect.width()), column)
            allLines.append(line)
        for column in range(0, horigin, self.__screen_size.get("tamanhocelula") * -1):
            line = QtCore.QLineF(worigin, column, int(rect.width()), column)
            allLines.append(line)

        # Desenhar as linhas para cima e para baixo
        for row in range(0, int(rect.width()), self.__screen_size.get("tamanhocelula")):
            line = QtCore.QLineF(row, horigin, row, int(rect.height()))
            allLines.append(line)
        for row in range(0, worigin, self.__screen_size.get("tamanhocelula") * -1):
            line = QtCore.QLineF(row, horigin, row, int(rect.height()))
            allLines.append(line)
        painter.drawLines(allLines)

        #Desenhar as linhas centrais
        pen.setWidth(5)
        painter.setPen(pen)
        line_1 = QtCore.QLineF(0, horigin, 0, int(rect.height()))
        line_2 = QtCore.QLineF(worigin, 0, int(rect.width()), 0)
        painter.drawLines([line_1, line_2])

    # Funcao para o tratamento dos dados
    def __voltagemValueToPoint(self, value=5, read_time=10, channel=0):
        total_height = self.__screen_size.get("height")
        temp_voltage = value - 2.5
        yPosition = (temp_voltage * total_height) / 2.5
        scale_x = self.__channels_settings[channel].get(
            "escala").get("horizontal")
        scale_y = self.__channels_settings[channel].get(
            "escala").get("vertical")
        return QtCore.QPointF(read_time * scale_x, yPosition * scale_y)

    # Função para desenhar as formas de ondas
    def _desenharCurva(self, selected_pen=0, values=[]):
        self.__paths[selected_pen].clear()
        pen = self.__pens[selected_pen]
        pen.setWidth(3)
        path = self.__paths[selected_pen]
        path.moveTo(0, 0)
        previous_last_point = self.__voltagemValueToPoint(
            values[0], 0, selected_pen)
        for counter in range(1, len(values), 2):
            if len(values) > counter + 1:
                read_time = counter * self.__screen_size.get("tamanhocelula")
                voltage_1, voltage_2 = values[counter], values[counter + 1]
                control_point_1 = previous_last_point
                control_point_2 = self.__voltagemValueToPoint(
                    voltage_1, read_time, selected_pen)
                read_time = (counter + 1) * self.__screen_size.get("tamanhocelula")
                end_point = self.__voltagemValueToPoint(
                    voltage_2, read_time, selected_pen)
                path.cubicTo(control_point_2, control_point_1, end_point)
                previous_last_point = end_point
        self.__scene.addPath(path, pen)

    #Função do ajuste das escalas
    def _desenharEscala(self):
        path = self.__paths[2]
        path.clear()
        pen = self.__pens[0]
        pen.setWidth(1)

        self.__scene.addPath(path, pen)

    # Função para abilitar a visualização da forma de onda de cada canal
    def desenharCurvasdosCanais(self, canal1=[], canal2=[]):#desenharCurvasdosCanais
        self.__scene.clear()
        self._desenharEscala()
        if self.__channels_settings[0].get("visivel"):
            self._desenharCurva(0, canal1)
        if self.__channels_settings[1].get("visivel"):
            self._desenharCurva(1, canal2)
