# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_frame.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class telaOsciloscopio(object):
    def programacao(self, Osciloscopio):
        Osciloscopio.setObjectName("Osciloscopio")
        Osciloscopio.resize(900, 500)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 4, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 4, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 4, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 4, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 4, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Osciloscopio.setPalette(palette)
        self.centralW = QtWidgets.QWidget(Osciloscopio)
        self.centralW.setObjectName("centralW")
        self.vertical_lay_out = QtWidgets.QVBoxLayout(self.centralW)
        self.vertical_lay_out.setObjectName("vertical_lay_out")
        self.frame = QtWidgets.QFrame(self.centralW)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frame.setPalette(palette)
        self.frame.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.vertical_lay_out_3 = QtWidgets.QVBoxLayout(self.frame)
        self.vertical_lay_out_3.setObjectName("vertical_lay_out_3")
        self.h_layout_canvas = QtWidgets.QHBoxLayout()
        self.h_layout_canvas.setObjectName("h_layout_canvas")
        self.graficview = QtWidgets.QGraphicsView(self.frame)
        self.graficview.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graficview.setObjectName("graficview")
        self.h_layout_canvas.addWidget(self.graficview)
        self.vertical_lay_out_3.addLayout(self.h_layout_canvas)
        self.comandos_h_layout = QtWidgets.QHBoxLayout()
        self.comandos_h_layout.setObjectName("comandos_h_layout")
        self.canals_v_cfig_layout = QtWidgets.QVBoxLayout()
        self.canals_v_cfig_layout.setObjectName("canals_v_cfig_layout")
        self.escala_de_canal_h_layout = QtWidgets.QHBoxLayout()
        self.escala_de_canal_h_layout.setObjectName("escala_de_canal_h_layout")
        self.escala_canal_1_v_layout = QtWidgets.QVBoxLayout()
        self.escala_canal_1_v_layout.setObjectName("escala_canal_1_v_layout")
        self.channel_1_checkbox = QtWidgets.QCheckBox(self.frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.channel_1_checkbox.setPalette(palette)
        self.channel_1_checkbox.setObjectName("channel_1_checkbox")
        self.escala_canal_1_v_layout.addWidget(self.channel_1_checkbox)
        self.canal_1_v_escala_hlayout = QtWidgets.QHBoxLayout()
        self.canal_1_v_escala_hlayout.setObjectName("canal_1_v_escala_hlayout")
        self.canal_1_v_escala_label = QtWidgets.QLabel(self.frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.canal_1_v_escala_label.setPalette(palette)
        self.canal_1_v_escala_label.setObjectName("canal_1_v_escala_label")
        self.canal_1_v_escala_hlayout.addWidget(self.canal_1_v_escala_label)
        self.canal_1_escala_vertical = QtWidgets.QSlider(self.frame)
        self.canal_1_escala_vertical.setMinimum(6)
        self.canal_1_escala_vertical.setMaximum(10)
        self.canal_1_escala_vertical.setOrientation(QtCore.Qt.Horizontal)
        self.canal_1_escala_vertical.setObjectName("canal_1_escala_vertical") 
        self.canal_1_v_escala_hlayout.addWidget(self.canal_1_escala_vertical)
        self.escala_canal_1_v_layout.addLayout(self.canal_1_v_escala_hlayout)
        self.canal_1_h_escala_layout = QtWidgets.QHBoxLayout()
        self.canal_1_h_escala_layout.setObjectName("canal_1_h_escala_layout")
        self.canal_1_h_escala_label = QtWidgets.QLabel(self.frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.canal_1_h_escala_label.setPalette(palette)
        self.canal_1_h_escala_label.setObjectName("canal_1_h_escala_label")
        self.canal_1_h_escala_layout.addWidget(self.canal_1_h_escala_label)
        self.canal_1_escala_horizontal = QtWidgets.QSlider(self.frame)
        self.canal_1_escala_horizontal.setMinimum(1)
        self.canal_1_escala_horizontal.setMaximum(10)
        self.canal_1_escala_horizontal.setOrientation(QtCore.Qt.Horizontal)
        self.canal_1_escala_horizontal.setObjectName("canal_1_escala_horizontal")
        self.canal_1_h_escala_layout.addWidget(self.canal_1_escala_horizontal)
        self.escala_canal_1_v_layout.addLayout(self.canal_1_h_escala_layout)
        self.escala_de_canal_h_layout.addLayout(self.escala_canal_1_v_layout)
        self.canal_2_escala_v_layout = QtWidgets.QVBoxLayout()
        self.canal_2_escala_v_layout.setObjectName("canal_2_escala_v_layout")
        self.channel_2_checkbox = QtWidgets.QCheckBox(self.frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.channel_2_checkbox.setPalette(palette)
        self.channel_2_checkbox.setObjectName("channel_2_checkbox")
        self.canal_2_escala_v_layout.addWidget(self.channel_2_checkbox)
        self.canal_2_escala_h_layout = QtWidgets.QHBoxLayout()
        self.canal_2_escala_h_layout.setObjectName("canal_2_escala_h_layout")
        self.canal_2_escala_v_label = QtWidgets.QLabel(self.frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.canal_2_escala_v_label.setPalette(palette)
        self.canal_2_escala_v_label.setObjectName("canal_2_escala_v_label")
        self.canal_2_escala_h_layout.addWidget(self.canal_2_escala_v_label)
        self.canal_2_escala_vertical = QtWidgets.QSlider(self.frame)
        self.canal_2_escala_vertical.setMinimum(6)
        self.canal_2_escala_vertical.setMaximum(10)
        self.canal_2_escala_vertical.setOrientation(QtCore.Qt.Horizontal)
        self.canal_2_escala_vertical.setObjectName("canal_2_escala_vertical")
        self.canal_2_escala_h_layout.addWidget(self.canal_2_escala_vertical)
        self.canal_2_escala_v_layout.addLayout(self.canal_2_escala_h_layout)
        self.canal_2_escala_h_layout = QtWidgets.QHBoxLayout()
        self.canal_2_escala_h_layout.setObjectName("canal_2_escala_h_layout")
        self.canal_2_escala_h_label = QtWidgets.QLabel(self.frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.canal_2_escala_h_label.setPalette(palette)
        self.canal_2_escala_h_label.setObjectName("canal_2_escala_h_label")
        self.canal_2_escala_h_layout.addWidget(self.canal_2_escala_h_label)
        self.canal_2_escala_horizontal = QtWidgets.QSlider(self.frame)
        self.canal_2_escala_horizontal.setMinimum(4)
        self.canal_2_escala_horizontal.setMaximum(10)
        self.canal_2_escala_horizontal.setOrientation(QtCore.Qt.Horizontal)
        self.canal_2_escala_horizontal.setObjectName("canal_2_escala_horizontal")
        self.canal_2_escala_h_layout.addWidget(self.canal_2_escala_horizontal)
        self.canal_2_escala_v_layout.addLayout(self.canal_2_escala_h_layout)
        self.escala_de_canal_h_layout.addLayout(self.canal_2_escala_v_layout)
        self.canals_v_cfig_layout.addLayout(self.escala_de_canal_h_layout)
        self.canals_checkbox_h_layout = QtWidgets.QHBoxLayout()
        self.canals_checkbox_h_layout.setObjectName("canals_checkbox_h_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.canals_checkbox_h_layout.addLayout(self.horizontalLayout)
        self.canals_v_cfig_layout.addLayout(self.canals_checkbox_h_layout)
        self.comandos_h_layout.addLayout(self.canals_v_cfig_layout)
        self.vertical_lay_out_3.addLayout(self.comandos_h_layout)
        self.vertical_lay_out.addWidget(self.frame)
        Osciloscopio.setCentralWidget(self.centralW)
        self.menu = QtWidgets.QMenuBar(Osciloscopio)
        self.menu.setGeometry(QtCore.QRect(0, 0, 800, 201))
        self.menu.setObjectName("menu")
        Osciloscopio.setMenuBar(self.menu)
        self.statusbar = QtWidgets.QStatusBar(Osciloscopio)
        self.statusbar.setObjectName("statusbar")
        Osciloscopio.setStatusBar(self.statusbar)

        self.retranslateUi(Osciloscopio)
        QtCore.QMetaObject.connectSlotsByName(Osciloscopio)

    def retranslateUi(self, Osciloscopio):
        _translate = QtCore.QCoreApplication.translate
        Osciloscopio.setWindowTitle(_translate("Osciloscopio", "Osciloscópio"))
        self.channel_1_checkbox.setText(_translate("Osciloscopio", "Canal 1 - Verde"))
        self.channel_2_checkbox.setText(_translate("Osciloscopio", "Canal 2 - Amarelo"))
        self.canal_1_v_escala_label.setText(_translate("Osciloscopio", "Escala Vertical(5mV)"))
        self.canal_1_h_escala_label.setText(_translate("Osciloscopio", "Escala Horizontal"))
        self.canal_2_escala_v_label.setText(_translate("Osciloscopio", "Escala Vertical(5mV)"))
        self.canal_2_escala_h_label.setText(_translate("Osciloscopio", "Escala Horizontal"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Osciloscopio = QtWidgets.QMainWindow()
    ui = telaOsciloscopio()
    ui.programacao(Osciloscopio)
    Osciloscopio.show()
    sys.exit(app.exec_())