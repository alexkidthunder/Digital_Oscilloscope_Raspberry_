import RPi_emu.GPIO as GPIO
import time
import random 

class I2C:
    def __init__(self):       
        random.seed() #Random numero como light level
        self.__address = 0x70
        self.__smbus = GPIO.SMBus(0)     
        GPIO.add_autoreply(self.__address, 2, 5)
        GPIO.add_autoreply(self.__address, 3, 1)

    def range(self):
        range1 = self.__smbus.read_byte_data(self.__address, 2)
        range2 = self.__smbus.read_byte_data(self.__address, 3)
        range3 = (range1 << 8) + range2
        return range3

    def write(self,value):
        self.__smbus.write_byte_data(self.__address, 0, value)
        GPIO.add_autoreply(self.__address, 1, random.randrange(0, 255, 1)) #Random numero pro registrador 1 (light level)
        return -1

    def pegarvoltagem(self):#Envia os dados atravéz do read_byte_data
        Bvoltagem = self.__smbus.read_byte_data(self.__address, 1)
        #Transformando o binario para a respectiva voltagem
        voltage = (5 * Bvoltagem) / 256.0
        #print(voltage) # Mostrar no terminal a voltagem
        return voltage