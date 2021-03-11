
import pygame
import random
pygame.init()

pygame.mixer.init()



width=900
height=500
gw=pygame.display.set_mode((width,height))#setting the game window, function takes tupple as an argument
pygame.display.set_caption("akhil ki snake game")#giving title to the game
pygame.display.update()
white=(255,255,255)
red=(255,0,0    )
green=(0,255,0)
black=(0,0,0)
def draw(x,y):
    pygame.draw.rect(gw,black,[x,y,15,15])
foont=pygame.font.SysFont(None,55)# a global variable telling font type and size 
def text_screen(text,color,x_font,y_font):
    ans=foont.render(text,True,color)# font.render is a function of pygame True is for antialising
    gw.blit(ans,[x_font,y_font])#blit is also a function
def start_game():
    clock=pygame.time.Clock()
    while 1:
        bk=0
        gw.fill((50,50,250))
        text_screen("welcome to the snakes",(10,10,10),300,200)
        text_screen("press enter to play",(10,10,10),300,300)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    
                    game_loop()
                    bk=1
                    break
        if bk==1:
            break           
        clock.tick(30)
        
img=pygame.image.load("photo.png")
backgr=pygame.transform.scale(img,(60,50)).convert_alpha()
def game_loop():   
    lives=3
    pygame.mixer.music.load("through.mp3")
    pygame.mixer.music.play()
    exit_game=False
    game_over=False
    snk_x=500
    snk_y=50
    snk_l=15
    snk_w=15
    fps=20
    vx=10
    vy=0
    fx=10*random.randrange(0,60)
    fy=10*random.randrange(6,40)
    score=0
    clock=pygame.time.Clock()
    ex=0
    pos=[]   
    lvz=0
    gd=5
    ed=False
    while not exit_game:
        if ed ==True:
            pygame.mixer.music.load("end.mp3")
            pygame.mixer.music.play()
            ed=False
        if gd==5:
            pygame.mixer.music.load("through.mp3")
            pygame.mixer.music.play()
            gd=6
        for event in pygame.event.get():
            if event.type==pygame.QUIT:#clicking the close button,game ends
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    gw.fill((random.randint(100,255),random.randint(50,255),random.randint(0,255)))
                if not ed:
                    if   event.key==pygame.K_RIGHT and vx==0:
                        #snk_x=snk_x+10
                        vx=10
                        vy=0
                    if event.key==pygame.K_LEFT and vx==0:
                        #snk_x=snk_x-10
                        vx=-10
                        vy=0
                    if event.key==pygame.K_UP and vy==0:
                        #snk_y=snk_y-10
                        vx=0
                        vy=-10
                    if event.key==pygame.K_DOWN and vy==0:
                        #snk_y=snk_y+10
                        vx=0
                        vy=10
                if event.key==pygame.K_k:
                    lives=0
                if event.key==pygame.K_RETURN and lvz==1:
                    gd=5
                    lives=3
                    score=0
                    pos=[]
                    fps=20
                    ex=0
                    lvz=0
        if snk_x>=width:
            snk_x=0
        if snk_x<0:
            snk_x=width
        if snk_y>=height:
            snk_y=50
        if snk_y<50:
            snk_y=height
        if score==0:
            green=(0,255,0)
        if abs(snk_x-fx)<15 and abs(snk_y-fy)<15:
            fx=10*random.randrange(0,60)
            fy=10*random.randrange(6,40)
            #snk_l=snk_l+10
            ex+=1
            pos.append([snk_x,snk_y])
            score=score+10
            if score%100==0:
                fps+=5
                green=(random.randint(50,150),random.randint(50,255),random.randint(0,255))
        snk_x=snk_x+vx
        snk_y=snk_y+vy           
        gw.fill(green)
        #pygame.draw.polygon (gw, black, [(140, 160), (140, 200), (360, 200), (360, 160)], 2)
        pygame.draw.circle(gw,(200,50,0),[fx,fy],10)
        pygame.draw.rect(gw,black,[snk_x,snk_y,snk_l,snk_w])# a list is given in order x ,y, width,length
        pygame.draw.rect(gw,(200,100,40),[0,0,width,50])
        for tes in range (lives):
            gw.blit(backgr,(600+(tes*80),0))
        for he in range (ex):
            draw(pos[he][0],pos[he][1])
        if pos[1:].count([snk_x,snk_y])==1:
            lives=lives-1
        text_screen("SCORE : "+str(score),black,10,10)
        if lives==0:
            ed=True
            lvz=1
            gd=5
            score=0
            pos=[]
            fps=20
            ex=0
            gw.fill((10,100,10))
            text_screen("your game is over",(0,0,0),width/2.5,200)
            text_screen("press enter to continue",(0,0,0),width/2.5,250)
        pos.append([snk_x,snk_y])
        pos=pos[1:]
        pygame.display.update()
        clock.tick(fps)
start_game()
pygame.quit()
quit()