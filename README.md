# Digital Oscilloscope Raspberry
Problema da matéria de Sistema Digital envolvendo Raspberry Pi, no qual tem a intenção de ter um software de um osciloscópio digital, que usa de uma SBC(Single Board Computer), mais especificamente uma Raspberry Pi e um conversor de sinal ADS1115,porém foi substituído pelo emulador YARPie, no qual emula os sinais recebidos do protocolo I2C.

# Informações:

Este projeto tem como finalidade a comunicação entre o conversor de sinal ADS115 com uma SBC através do protocolo I2C. Com o sucesso da comunicação entre os dois, os dados coletados são mostrados numa tela referente ao osciloscópio, no qual pode ser alterado a escala de sua visualização.

# Bibliotecas utilizadas:

>1. 'pygame': Pygame é uma biblioteca de jogos multiplataforma feita para ser utilizada em conjunto com a linguagem de programação Python.
>2. 'graphicTela' representação da tela do Osciloscópio.
>3. 'I2C' Converte os dados que o osciloscópio recebe em volts.
>4. 'controllerI2C' controle da comunicação entre o I2C e o conversor ADS1115.
>5. 'GerenciadorEventos' Gerenciador de eventos ocorridos durante o processo.

# Configurações:

Foi utilizado o Python3.x, com isso, pra configurar execute usando ele.
> - pip install pygame
> - pip install PyQt5

# Execução

Quando terminar as configurações abra o local do arquivo no src e execute:
> - No windows: python .\main.py
> - No linux: python3 ./main.py
> - =>Tendo em consideração que para o linux as configurações tem que ser as seguintes:
> - pip3 install pygame
> - pip3 install PyQt5

# Extra

> -  PygameAplicationOscill, uma aplicação no qual somente necessita do pygame configurado. No qual apresenta as primeiras tentativas do testes da parte gráfica com especificas funções do YARPie e o desenho dos dados obtidos na tela.
Para executar essa aplicação:
> - No windows: python .\PygameAplicationOscill.py
> - No linux: python3 ./PygameAplicationOscill.py
