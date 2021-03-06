from model.I2C import I2C
import time
import threading

class controllerI2C(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__i2c = I2C()
        self.__voltagemV = ([], [])
        self.__indexes = [0, 0]
        self.__max_index = 60
        self.__delay_time = 0.15

    def __atualizar_voltagem( self, channel=0, value=5 ):
        self.__voltagemV[channel].append(value)
        if len(self.__voltagemV[channel]) >= self.__max_index:
            self.__voltagemV[channel].remove(self.__voltagemV[channel][0])
            self.__voltagemV[channel].remove(self.__voltagemV[channel][0])

    def set_delay_time(self, value=0.6):
        self.__delay_time = value

    def _atualizar_lista_voltagem(self):
        # Voltagem para o canal 1
        self.__i2c.write(0x51)
        time.sleep(self.__delay_time)
        channel_1 = self.__i2c.pegarvoltagem()
        self.__atualizar_voltagem(0, channel_1)
        # Voltagem para o canal 2
        self.__i2c.write(0x51)
        channel_2 = self.__i2c.pegarvoltagem()
        self.__atualizar_voltagem(1, channel_2)
        
    def pegar_voltagem(self):
        return tuple(self.__voltagemV[0]), tuple(self.__voltagemV[1])

    def run(self):
        while True:
            self.__i2c.write(0x51)
            self._atualizar_lista_voltagem()
            ##################testes#####################
            # rng = self.__i2c.range(); 
            # print("rng", rng)
