from PyQt5 import QtCore

class GerenciadorEventos():
    def __init__(self, ui, telaOsciloscopio, controllerI2C):
        self.__ui = ui
        self.__controllerI2C = controllerI2C
        self.__telaOsciloscopio = telaOsciloscopio

        # Callback to checkbox event
        self.__ui.channel_1_checkbox.stateChanged.connect(lambda: self.checkbox_state_changed(1))
        self.__ui.channel_2_checkbox.stateChanged.connect(lambda: self.checkbox_state_changed(2))

        # Callback to slider event
        self.__ui.canal_1_escala_vertical.valueChanged.connect(    lambda: self.__scale_change(self.__ui.canal_1_escala_vertical, False, 0))
        self.__ui.canal_1_escala_horizontal.valueChanged.connect(  lambda: self.__scale_change(self.__ui.canal_1_escala_horizontal, True, 0))
        self.__ui.canal_2_escala_vertical.valueChanged.connect(    lambda: self.__scale_change(self.__ui.canal_2_escala_vertical, False, 1))
        self.__ui.canal_2_escala_horizontal.valueChanged.connect(  lambda: self.__scale_change(self.__ui.canal_2_escala_horizontal, True, 1))

        # Callback to double spin box
        self.__timer = QtCore.QTimer()
        self.__timer.timeout.connect(self.update_values_draw)
        self.__timer.start(50)

    # Checa as mudanças nas escalas
    def __scale_change(self, slider, scale_type=False, channel=0):
        if scale_type:
            self.__telaOsciloscopio.definirEscalaHorizontal(slider.value(), channel)
        else:
            self.__telaOsciloscopio.definirEscalaVertical(slider.value(), channel)

    # Atualiza os valores
    def update_values_draw(self):
        channel_1, channel_2 = self.__controllerI2C.pegar_voltagem()
        self.__telaOsciloscopio.desenharCurvasdosCanais(channel_1, channel_2)

    # Condição de estado dos Checkbox
    def checkbox_state_changed(self, checkboxCanal=1):
        if checkboxCanal == 1:
            if self.__ui.channel_1_checkbox.isChecked():
                self.__telaOsciloscopio.visibilidadeCanal(0, True)   # print("Checkbox 1 Checked")
            else:
                self.__telaOsciloscopio.visibilidadeCanal( 0, False) # print("Checkbox 1 Unchecked")
        elif checkboxCanal == 2:
            if self.__ui.channel_2_checkbox.isChecked():
                self.__telaOsciloscopio.visibilidadeCanal( 1, True)  # print("Checkbox 2 Checked")
            else:
                self.__telaOsciloscopio.visibilidadeCanal(1, False)  # print("Checkbox 2 Unchecked")

    def run(self):
        self.__controllerI2C.start()