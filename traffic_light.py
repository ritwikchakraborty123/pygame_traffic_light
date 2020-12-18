import pygame
import schedule 
import time

pygame.init()

SIDE=260

win = pygame.display.set_mode((260,440))

pygame.display.set_caption('Traffic Light')

white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
yellow=(255,255,0)
black=(0,0,0)

red_visible=False
yellow_visible=False
green_visible=False
reset=True

FONT=pygame.font.SysFont('comicsans',30)

clock = pygame.time.Clock()
run = True

images = []

files =["off.png","red.png","green.png","yellow.png"]

for i in range (4):	
    image=pygame.image.load(files[i])
    images.append(image)

#260 * 366 

def drawWindow():
    global red_visible
    global yellow_visible
    global green_visible
    global reset

    win.fill((0,0,0))

    if red_visible:
        win.blit(images[1],(0,40))
        text=FONT.render("STOP!",1,red)
        win.blit(text,(SIDE/2-text.get_width()/2,420))
    if yellow_visible:
        win.blit(images[3],(0,40))
        text=FONT.render("prepare!",1,yellow)
        win.blit(text,(SIDE/2-text.get_width()/2,420))
    if green_visible:
        win.blit(images[2],(0,40))
        text=FONT.render("GO!",1,green)
        win.blit(text,(SIDE/2-text.get_width()/2,420))
    if reset:
        win.blit(images[0],(0,40))
        text=FONT.render("all light reset",1,white)
        win.blit(text,(SIDE/2-text.get_width()/2,420))
    
    text=FONT.render("Traffic Light ! ",1,white)
    win.blit(text,(SIDE/2-text.get_width()/2,00))
    
    pygame.display.update()


def change(a,b,c,d):
    global red_visible
    global yellow_visible
    global green_visible
    global reset
    red_visible=a
    yellow_visible=b
    green_visible=c
    reset=d
val=3
def modulate():
    global val
    if(val==0):
        change(True,False,False,False)
    elif(val==1) :
        change(False,True,False,False)
    elif(val==2) :
        change(False,False,True,False)
    else:
        change(False,False,False,True)
    val+=1
    val%=4    

while run:
    clock.tick(60)
    modulate()

    pygame.time.wait(5000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False


    drawWindow()            

