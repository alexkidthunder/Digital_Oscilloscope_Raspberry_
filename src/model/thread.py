from threading import Thread # Pode-se utilizar direto sem precisar criar uma função separada

       class Th(Thread):

                def init (self, num):
                      Thread.init(self)
                      self.num = num

                def run(self):

                      print "Hello "
                      print self.num


       a = Th(1)
       a.start()