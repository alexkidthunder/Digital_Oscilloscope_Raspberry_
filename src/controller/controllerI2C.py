from model.I2C import I2C
import time

class controllerI2C():
    def __init__(self):        
        self.__i2c = I2C()
        self.__voltagemV = ([], [])
        self.__indexes = [0, 0]
        self.__max_index = 60
        self.__delay_time = 0.6

    def set_delay_time(self, value=0.5):
        self.__delay_time = value

    def __update_voltage(self, channel=0, value=5):
        self.__voltagemV[channel].append(value)
        if len(self.__voltagemV[channel]) >= self.__max_index:
            self.__voltagemV[channel].remove(self.__voltagemV[channel][0])
            self.__voltagemV[channel].remove(self.__voltagemV[channel][0])

    def _update_voltage_list(self):
        self.__i2c.write(0x51)
        time.sleep(self.__delay_time)
        channel_1 = self.__i2c.getVoltage()
        self.__update_voltage(0, channel_1)
        self.__i2c.write(0x51)
        channel_2 = self.__i2c.getVoltage()
        self.__update_voltage(1, channel_2)
        # print("channel_1", channel_1, "channel_2", channel_2)

    def pegar_voltagem(self):
        return tuple(self.__voltagemV[0]), tuple(self.__voltagemV[1])

    def run(self):
        while True:
            self.__i2c.write(0x51)
            self._update_voltage_list()
            #testes
            # rng = self.__i2c.range(); 
            # print("rng", rng)
