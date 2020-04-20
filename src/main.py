from view.graphic import graphic
from controller.controllerI2C import controllerI2C
from controller.eventController import EventController


def execute_oscilloscope(app=QtWidgets.QApplication(sys.argv), application=ApplicationWindow()):
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":       
    eventHandler = EventHandler(
        application.oscilloscopeGraphic, controllerI2C())
    EventController.run()
