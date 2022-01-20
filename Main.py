import random, math, os, sys,time, pygame as p
from pygame.locals import *
from Sprites import *
from Stars import *

WINSIZE = [1280, 960]
WINCENTER = [640,480]
NUMSTARS = 150

failend=0
intro =0
score=0

def manage_image():
    img = load_image('spaceship.png')
    Player.images = [img,p.transform.flip(img,1,0)]
    Bomb.images=[img]
    img = load_image('enemy.png')
    Enemy.images = [img]
    
    img = load_image('shoot.png')
    img1 = load_image('shooot.png')
    Missile.images = [img,img1]
    
    img = load_image('bossshoot.png')
    img1=load_image('bossshoot1.png')
    img2=load_image('bossshoot2.png')
    BossMissile.images=[img,img1,img2]
    
    img= load_image('Game.png')
    GameOver.images = [img]
    
    img=load_image('Fail.png')
    img1=load_image('Retry.png')
    img2=load_image('Logo.png')
    img3=load_image('Enter.png')
    img4=load_image('Point.png')
    img5=load_image('Score.png')
    TextLabel.images=[img,img1,img2,img3,img4,img5]
    explist = os.listdir(main_dir+'\\difficulty\\')
    explist.sort()
    for e in explist:
        img = load_image((main_dir+'\\difficulty\\')+e)
        TextLabel.images.append(img)
    img = load_image('bomb.png')
    TextLabel.images.append(img)
    img = load_image('tutorial.png')
    TextLabel.images.append(img)
    Explode.images = []
    explist = os.listdir(main_dir+'\\explode')
    explist.sort()
    for e in explist:
        img = load_image(main_dir+'\\explode\\'+e)
        Explode.images.append(img)
        
    Boss.images=[]
    explist = os.listdir(main_dir+'\\boss')
    explist.sort()
    for e in explist:
        img = load_image(main_dir+'\\boss\\'+e)
        Boss.images.append(img)

def game_intro():
    global intro
    global enter
    while not intro:
            screen.fill(black)
 #add contents            
            if not allsprites.has(logo)and not allsprites.has(tutorial):
                allsprites.add(logo)
            if not allsprites.has(enter) and not allsprites.has(tutorial):
                cal_time= time.time()-start_time
                if math.ceil(cal_time)%2==0:
                    enter=EnterLabel()
                    allsprites.add(enter)
            draw_stars(screen, stars, black)
            move_stars(stars)
            draw_stars(screen, stars, white)    
        
 #handle keyevent        
            for e in p.event.get(): 
                if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                    sys.exit() 
                if e.type == KEYDOWN and e.key == K_RETURN:
                    
                    if allsprites.has(tutorial):
                        allsprites.empty()
                        intro=1
                    else:
                        allsprites.empty()
                        allsprites.add(tutorial)
            if not allsprites.has(enter) and allsprites.has(tutorial):
                cal_time= time.time()-start_time
                if math.ceil(cal_time)%2==0:
                    enter=EnterLabel()
                    enter.rect=(360,820)
                    allsprites.add(enter)        
                            
 #update screen                               
            enemies.update()            
            allsprites.update()
            allsprites.draw(screen)
            p.display.flip()    
            clock.tick(100)

def game_play():
    global difficulty_label
    global difficulty
    global bosscount
    global scoremag
    global point
    global score
    bombcount=0
    bombshot=0
    bombNum=3
    eneNum=4
    while player.alive:
        bomb = Bomb()
        scoreT=False
        failend=1
        screen.fill(black)
        text = font.render(str(score),True,fontcolor,None)
        text1 = font.render(str(bombNum),True,fontcolor,None)
        
 #add contents       
        allsprites.add(player)
        if not allsprites.has(coin,bomb_Count):
            allsprites.add(coin,bomb_Count)
        if not allsprites.has(difficulty_label):
            if difficulty_label.index<difficulty_label.difficulty:
                difficulty_label.index+=1
                difficulty_label=DifficultyLabel(difficulty_label.index,difficulty_label.difficulty)
            allsprites.add(difficulty_label)
        if bombshot:
            bombs.add(bomb)
            allsprites.add(bomb)
            bombcount+=1
            if bombcount==30:
                bombcount=0
                bombshot=0
        if bomb_Count.rect.y==900:
            screen.blit(text1,(1190,885))
        if coin.rect.y==30:
            screen.blit(text,textRect)
        
        if(len(enemies)<eneNum) and player.status==1:          
            enemy = Enemy1()
            allsprites.add(enemy)
            enemies.add(enemy)
            oldenemies.add(enemy)
            
        draw_stars(screen, stars, black)
        move_stars(stars)
        draw_stars(screen, stars, white)
 #adapt change based on score

        if score>49:                
                enemy.speedy= random.randrange(1,4)
                scoremag=2
                point =2
                difficulty_label.difficulty=7
        if score>99:
            enemy.speedx1= random.randrange(1,3)
            enemy.speedx2= random.randrange(-3,-1)
            
            scoremag=3
            point =3
            difficulty_label.difficulty=8
            if bosscount==1 and not allsprites.has(boss):
                allsprites.add(boss)
                boss.life=score
                health = boss.life 
                bombNum+=1
        if score>149:
            enemy.speedy= random.randrange(2,5)
            scoremag=4
            point =4
            eneNum=5
            difficulty_label.difficulty=9
        if score>199:
            enemy.speedx1= random.randrange(2,4)
            enemy.speedx2= random.randrange(-4,-2)
            scoremag=5
            point =5
            eneNum=6
            difficulty_label.difficulty=10
            if bosscount==2 and not allsprites.has(boss):
                allsprites.add(boss)
                boss.life=score
                health = boss.life
                bombNum+=1
        if score>300:
            enemy.speedy= random.randrange(2,5)
            enemy.speedx1= random.randrange(2,5)
            enemy.speedx2= random.randrange(-5,-2)
            scoremag=6
            point =6
            
            difficulty_label.difficulty=11
            if bosscount==3 and not allsprites.has(boss):
                allsprites.add(boss)
                boss.life=score
                health = boss.life
                bombNum+=1
        if score>400:
            enemy.speedy= random.randrange(3,6)
            enemy.speedx= random.randrange(3,6)
            enemy.speedx= random.randrange(-6,-3)
            scoremag=7
            point =7
            eneNum=7
            difficulty_label.difficulty=12
            if bosscount==4 and not allsprites.has(boss):
                allsprites.add(boss)
                boss.life=score
                health = boss.life
                bombNum+=1
        if score>500:
            scoremag=8
            point =8
            eneNum=8
            difficulty_label.difficulty=13
            if bosscount==5 and not allsprites.has(boss):
                allsprites.add(boss)
                boss.life=score
                health = boss.life
                bombNum+=1
        if allsprites.has(boss):
            if boss.rect.y>=0:   
                while len(bossmissiles)<health/25 and len(bombs)==0:
                    bosmi = boss.fire()
                    bossmissiles.add(bosmi)
                    allsprites.add(bosmi)
            
 #set boundry to handle player_move
        if player.status==0:
            if player.rect.y>800:
                player.rect.move_ip(0,-4)
            if player.rect.y<=800:
                player.status=1
        
        if 0<=player.rect.x<=1200:
            player.rect.move_ip(player.movex,0)
        elif player.rect.x<0: 
            player.rect.move_ip(1,0)
        elif player.rect.x>1200:
            player.rect.move_ip(-1,0)
        if 0<=player.rect.y<=920:
            player.rect.move_ip(0,player.movey)
        elif player.rect .y<0: 
            player.rect.move_ip(0,1)
        elif player.rect.y>90:
            player.rect.move_ip(0,-1)
        
 #collide_event
        for bosmi in bossmissiles:
            if p.sprite.collide_circle(player, bosmi):
                player.explode().add(allsprites)
                coin.kill()
                bomb_Count.kill()
                difficulty_label.kill()
                all.empty()
                failend=0
                bosmi.kill()
                boss.is_kill_player=1
            for bomb in bombs:
                if p.sprite.collide_circle(bomb, bosmi):
                   bosmi.kill()
                   bomb.kill() 
        for enemy in enemies:
            if len(oldenemies)<7:
                for oldenemy in oldenemies:
                    if oldenemy.rect.y<-50:
                        if p.sprite.collide_rect(oldenemy,enemy):
                            if not oldenemy.rect == enemy.rect:
                                oldenemy.kill()
                                enemy.kill()
            if enemy.rect.top > enemy.area.bottom:
                enemy.kill()
            for bomb in bombs:
                if p.sprite.collide_rect(bomb,enemy):
                    enemy.explode().add(allsprites)
                    score+=point
                    bomb.kill()
                if p.sprite.collide_rect(bomb,boss):
                    boss.gotshoot()
                    if boss.life==0:
                        bosscount+=1
                        boss.explode().add(allsprites)
                        allsprites.remove(boss)
                    bomb.kill()
            for missile in missiles:
                if p.sprite.collide_rect(missile,enemy):
                    enemy.explode().add(allsprites)
                    score+=point
                    missile.kill()
                if p.sprite.collide_rect(missile,boss):
                    boss.gotshoot()
                    if boss.life==0:
                        bosscount+=1
                        boss.explode().add(allsprites)
                        allsprites.remove(boss)
                    missile.kill()
            
            if p.sprite.collide_circle(player, enemy):
                failend=0
                boss.is_kill_player=1
                enemy.kill();
                player.explode().add(allsprites)
                coin.kill()
                bomb_Count.kill()
                difficulty_label.kill()
                all.empty()
 #key_states                
        key_state = p.key.get_pressed()
        if key_state[p.K_RIGHT or e.key == ord('d')]:
            player.movex = 5
        elif key_state[p.K_LEFT ]:
            player.movex = -5                  
        if key_state[p.K_UP or e.key == ord('w')]:
            player.movey =-5
        if key_state[p.K_DOWN or e.key == ord('s')]:
            player.movey =5  
 #key_events      
        for e in p.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                p.quit()
                
                sys.exit()
            if e.type == p.KEYDOWN:
                if e.key == p.K_b:
                    if bombNum>0:
                        bombshot=1
                        bombNum-=1
                if e.key == p.K_LEFT or e.key == ord('a'):
                    if 0<=player.rect.x<=WINSIZE[0]:
                        player.movex = -5
                    else :
                        player.movex = 0
                if e.key == p.K_RIGHT or e.key == ord('d'):
                    if 0<=player.rect.x<=WINSIZE[0]:
                        player.movex = 5
                    else :
                        player.movex = 0
                if e.key == p.K_UP or e.key == ord('w'):
                    if -11<=player.rect.y<=940:
                        player.movey=-5
                    else :
                        player.movey = 0
                elif e.key == p.K_DOWN or e.key == ord('s'):
                    if -11<=player.rect.y<=940:
                        player.movey=5
                    else :
                        player.movey = 0
                if e.key == p.K_SPACE:
                    newMissile = player.fire()
                    newMissile.add(missiles,allsprites)
                            
            if e.type == p.KEYUP:
                if e.key == p.K_LEFT or e.key == ord('a'):
                        player.movex = 0
                if e.key == p.K_RIGHT or e.key == ord('d'):
                        player.movex = 0
                if e.key == p.K_UP or e.key == ord('w'):
                        player.movey = 0
                elif e.key == p.K_DOWN or e.key == ord('s'):
                        player.movey = 0
                    
                
 #update screen
        enemies.update()            
        allsprites.update()
        allsprites.draw(screen)
        p.display.flip()
        clock.tick(90)

def game_outro():
    global textRect
    global score
    while not failend:
            screen.fill(black)
            text = font.render(str(score),True,fontcolor,None)
 #add contents          
            if len(allsprites)==0:
                allsprites.add(go,fail,retry,scoreboard)
            if allsprites.has(go):
                textRect = text.get_rect(center=(730,495))
                screen.blit(text,textRect)    
                                
            draw_stars(screen, stars, black)
            move_stars(stars)
            draw_stars(screen, stars, white)

 #manage key event        
            for e in p.event.get():  
                if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                    sys.exit()
                if e.type == KEYDOWN and e.key == K_r:
                    player.alive = True
                    intro=1
                    score=0
                    main()

 #update screen           
            enemies.update()            
            allsprites.update()
            allsprites.draw(screen)
            p.display.flip()    
            clock.tick(100)
    
def main():
 #declare global    
    global black,white,fontcolor,text,textRect,font,clock 
    global enemies,oldenemies,allsprites,missiles,stars,bossmissiles,bombs,all
    global scoremag,point,bosscount,failend,start_time,difficulty
    global coin,player,screen,boss,logo,enter,go,fail,retry,scoreboard,difficulty_label,bomb,bomb_Count,tutorial

 #declare variable
    point=1
    scoremag=1
    bosscount=1
    failend=0
    done = 0
    stars = initialize_stars()
    clock = p.time.Clock()
    difficulty=6
 #interface build for game initiate    
    p.init()
    p.display.set_caption('WE GO MARS')
    screen = p.display.set_mode(WINSIZE)
    font = p.font.Font((os.path.abspath('font')+'\Starjedi.ttf'),45)
    font.set_italic(True)
    font.set_bold(True)
    fontcolor = 255,222,6
    white = 255, 240, 200
    black = 0, 0, 0
    screen.fill(black)
    p.mouse.set_visible(0)
    
 #set score text    
    text = font.render(str(score),True,fontcolor,None)
    textRect = text.get_rect(center = (160,70))

 #add images       
    manage_image()

 #declare Groups of Sprites    
    all = p.sprite.Group()
    missiles = p.sprite.Group()
    bombs = p.sprite.Group()
    enemies = p.sprite.Group()
    oldenemies = p.sprite.Group()
    bossmissiles= p.sprite.Group()
    allsprites = p.sprite.RenderPlain()

 #declare Sprites    
    coin = Coin()
    difficulty_label = DifficultyLabel(difficulty,difficulty)
    player = Player(Missile)
    go = GameOver()
    logo = TextLabel(2,(640,400))
    fail = TextLabel(0,(750,400))
    retry = TextLabel(1,(750,550))
    scoreboard = TextLabel(5,(750,500))
    tutorial = TextLabel(15,(660,480))
    bomb_Count = BombCount()
    
    bomb = Bomb()
    
    enter = EnterLabel()
    boss = Boss(BossMissile)
    
    all.add(player)
    player.alive = True 
    
 #main game loop
    start_time = time.time()
    while not done:
        global intro
        game_intro()
        game_play()
        game_outro()
        
        
if __name__ == '__main__':
    main()
