import  pygame, os, time, random

pygame.init() 
pygame.display.set_caption("Pi Oscilloscope")#Definindo o nome da aplicação
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'#Centralizando a tela da aplicação 
pygame.event.set_allowed([pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN, pygame.QUIT, pygame.MOUSEBUTTONUP])#Definindo  os botões

textHeight=22 ; font = pygame.font.Font(None, textHeight)#Definindo tamanho de texto
screenWidth = 760 ; screenHight = 380# Definindo comprimento e largura da tela da aplicação
screen = pygame.display.set_mode([screenWidth,screenHight],0,32)# Definindo o modelo de tela
display = pygame.Surface((512,256))
backCol = (155,96,100) ; black = (0,0,0) # Cor de fundo
pramCol = (135,206,235) # parameter colour

displayWidth = 512 ; displayHight = 256
LedRect = [ pygame.Rect((0,0),(0,0))]*17
inBuf = [0]*512 # quick way of getting a 512 long buffer
chOff = displayHight//4 # Channel Offset
run = [True,False,False,True,False] # run controls
expandT = 1 ; expandV = 1 # expanção inicial da voltagem e do tempo 

volts_sample = 5/1024 # volts por amostra
measureVolts = False;savedVoltage = 0
cursorT = 0; cursorV = 0; vMag = 1; svLed = False; stLed = False
savedVoltsC = -1 

def main():
    pygame.draw.rect(screen,backCol,(0,0,screenWidth,screenHight+2),0)
    defineControls()
    drawControls()
    time.sleep(0.1)

    while(1):
       time.sleep(0.001) # let other code have a look in 

       readData() # get buffer data#####

       plotWave() # draw waveform           
       if  measureVolts :
          updateControls(True)  
       drawScope() # display new screen
       checkForEvent()
       while run[4]: # if in hold mode wait here
         checkForEvent()
      
#Desenha o GRID     
def drawGrid():
   pygame.draw.rect(display,(240,240,240),(0,0,displayWidth,displayHight),0)
   for h in range(32,256,32): # draw horizontal
       pygame.draw.line(display,(120,120,120),(0,h),(512,h),1)
   for v in range(32,512,32): # draw vertical
       pygame.draw.line(display,(120,120,120),(v,0),(v,256),1)
   pygame.draw.line(display,(0,0,0),(256,0),(256,256),1)
   pygame.draw.line(display,(0,0,0),(0,128),(512,128),1)

#Nomes das caixas de marcar e indicadores
def drawControls():
    drawWords("Ampliar Tempo",10,300,black,backCol)
    drawWords("Ampliar Voltagem",220,300,black,backCol)
    drawWords("Canal",470,300,black,backCol)
    drawWords("2",490,320,black,backCol)
    drawWords("Run Single Freeze ",540,77,black,backCol)
    
    updateControls(True)

#Atualizador
def updateControls(blank):
    global vDisp
    if blank:
      pygame.draw.rect(screen,backCol,resultsRect,0)      
    for n in range(0,6): # time option LED
       drawWords("x"+str(1<<n),10+n*30,320,black,backCol)
       drawLED(n,expandT == 1<<n)
    for n in range(6,9): # voltage options
       drawWords("x"+str(1<<(n-6)),220+(n-6)*30,320,black,backCol)
       drawLED(n,expandV == 1<<(n-6))       
    
    drawLED(10,measureVolts)
    
    for n in range(13,17):
       drawLED(n,run[n-13])    
   
       
def trunk(value, place): # truncate a value string
    v=str(value)+"000000"
    if value>0:
       v = v[0:place]
    else:
       v = v[0:place+1] # extra place for the minus sign
    return v   

#Quando clica ele fica marcado   
def drawLED(n,state): # draw LED
    if state : 
        pygame.draw.rect(screen,(10,150,50),LedRect[n],0)
    else :   
        pygame.draw.rect(screen,(240,240,240),LedRect[n],0)
    
#Caixas de marcar que modificam o solicitado
def defineControls():
   global LedRect, resultsRect
   for n in range(0,6):
       LedRect[n] = pygame.Rect((10+n*30,336),(15,15))
   for n in range(6,9):
       LedRect[n] = pygame.Rect((220+(n-6)*30,336),(15,15))
   LedRect[9] = pygame.Rect((440,336),(15,15))  # time
   LedRect[10] = pygame.Rect((486,336),(15,15)) # volts
   LedRect[13] = pygame.Rect((545,100),(15,15)) # run
   LedRect[14] = pygame.Rect((580,100),(15,15)) # single
   LedRect[15] = pygame.Rect((628,100),(15,15)) # freeze
   resultsRect = pygame.Rect((639,125),(90,153))

#Forma de onda
def plotWave():
    global vMag
    lastX=0 ; lastY=0
    vMag = 2 # adjust voltage scale
    if expandV == 1:
        vMag = 4
    if expandV == 4:
        vMag =1
    drawGrid()
    s = 0 # sample pointer
    for n in range(0, displayWidth, expandT):
        y = (512-inBuf[s])//vMag + chOff
        if n != 0:
            pygame.draw.line(display,(0,200,0),(lastX ,lastY), (n ,y ),2)
        lastX = n
        lastY = y
        s += 1
    
    #if measureVolts :
     #  pygame.draw.line(display,(255,0,0),(0,cursorV>>2), (512,cursorV>>2),1)
      # if savedVoltsC != -1:
       #  for n in range(0,512,12):  
        #    pygame.draw.line(display,(255,0,0),(n,savedVoltsC),(n+6,savedVoltsC),1)
      
#Desenha na tela
def drawScope(): # put display onto scope controls
    screen.blit(display,(10,10))
    pygame.display.update()

#Desenha na tela as palavras
def drawWords(words,x,y,col,backCol) :
    textSurface = font.render(words, True, col, backCol)
    textRect = textSurface.get_rect()
    textRect.left = x
    textRect.top = y    
    screen.blit(textSurface, textRect)

################################################### Formato das ondas
def readData():  # get buffer and controls
    global cursorT, cursorV, run
    time.sleep(0.111) # let other code have a look in 
    if run[2]:  # No modo freeze joga os dados no lixo
        for i in range(0, 1024):
            junk = random.randrange(0, 255, 1) 
    else: # otherwise read into the buffer
        for i in range(0,512):
            inBuf[i] = random.randrange(0, 510, 1)
            cursorT = random.randrange(0, 255, 1)
            cursorV =  random.randrange(0, 255, 1)
    if run[1]: #single sweep requested
        run[1] = False
        run[2] = True # put in freeze mode
        updateControls(True)

###################################################

# Evento do mouse quando clica
def handleMouse(pos): # look at mouse down
   global expandT,expandV,measureVolts,svLed
   global savedVoltsC, run
   #print(pos)
   for n in range(0,6) :
      if LedRect[n].collidepoint(pos):
         expandT = 1<<n
   for n in range(6,9) :
      if LedRect[n].collidepoint(pos): 
         expandV = 1<<(n-6)
   
   if LedRect[10].collidepoint(pos):
       measureVolts = not(measureVolts) # toggle volts measurement
       if not measureVolts :
           savedVoltsC = -1   
   
   if LedRect[12].collidepoint(pos) and measureVolts: # save volts
       svLed = True
       savedVoltsC = cursorV>>2
   # run controls logic    
   if LedRect[13].collidepoint(pos) and not run[1]: # run
       run[0] = not(run[0])
       if not run[0]:
           run[2] = True
       else:
           run[2] = False
   if LedRect[14].collidepoint(pos): # single
         run[1] = True
         run[0] = False
         run[2] = False
         run[4] = True
         updateControls(False)
         drawScope()         
   if LedRect[15].collidepoint(pos) and not run[1]: # freeze
       run[2] = not(run[2])
       if not run[2]:
           run[0] = True
       else:
           run[0] = False     
   updateControls(False)

# Evento do mouse quando solta
def handleMouseUp(pos): # look at mouse up
   global savedVoltage, svLed, run 
   if LedRect[12].collidepoint(pos) and measureVolts:
       savedVoltage = vDisp
       svLed = False
       updateControls(False)
   if LedRect[14].collidepoint(pos): # single
       run[4] = False
       updateControls(False)

#Para finalizar o programa
def terminate(): # close down the program
    pygame.quit() # close pygame
    os._exit(1)

#Para checar eventos no sistema 
def checkForEvent(): # see if we need to quit
    event = pygame.event.poll()
    if event.type == pygame.QUIT :
         terminate()
    if event.type == pygame.KEYDOWN :
       if event.key == pygame.K_ESCAPE :
          terminate()
       if event.key == pygame.K_s : # screen dump
          os.system("scrot -u")
    if event.type == pygame.MOUSEBUTTONDOWN :
        handleMouse(pygame.mouse.get_pos())
    if event.type == pygame.MOUSEBUTTONUP :
        handleMouseUp(pygame.mouse.get_pos())                  
        
       
# Lógica principal
if __name__ == '__main__':    
    main()