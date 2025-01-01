import pygame
import random 
import os
import sys

pygame.init()
pygame.mixer.init()


def show_snake(window,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(window,color,[x,y,snake_size,snake_size])

def show_score(text,color,score_x,score_y):
    score = font.render(text,True,color)
    window.blit(score,[score_x,score_y])

def show_food(window,color,food_x,food_y,food_size):
    pygame.draw.rect(window,color,[food_x,food_y,food_size,food_size])

def line(window,color,window_height,window_wight):
    pygame.draw.line(window,color,(0,0),(window_height,0),5)
    pygame.draw.line(window,color,(window_height,0),(window_height,window_wight),7)
    pygame.draw.line(window,color,(window_height,window_wight),(0,window_wight),7)
    pygame.draw.line(window,color,(0,0),(0,window_wight),5)

def show_line(text,color,x,y):
    score = style_font.render(text,True,color)
    window.blit(score,[x,y])

def homescreen():
    start_game = False
    bgimage = pygame.image.load('h_back.jpg')
    bgimage = pygame.transform.scale(bgimage,(window_height,window_wight)).convert_alpha()
    gamestart = pygame.mixer.Sound('gamestart.mp3')
    startloop = pygame.mixer.Sound('gameloop.mp3')
    while not start_game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                start_game=True
                pygame.QUIT()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    startloop.stop()
                    gamestart.play()
                    gameloop()    
        window.fill(white)
        window.blit(bgimage,(0,0))
        startloop.play()
        show_line("Press space for start the game",blue,80,550)
        pygame.display.update()
    clock.tick(fps)


def gameloop():
    
    # game variable 
    game_over = False
    exit_game = False
    
    # snake variable
    snake_x = 55
    snake_y = 44
    snake_list = []
    snake_size = 10
    snake_len = 1

    # speed vaiable
    velocity_x = 0 
    velocity_y = 0 
    u_velocity = 5
 
    # score variable
    score_x = 5
    score_y = 5 
    score = 0 

    # image variable
    bgiamge = pygame.image.load('snake.jpg')
    bgiamge = pygame.transform.scale(bgiamge,(window_height,window_wight))

    overig = pygame.image.load('gmover.jpg')
    overig = pygame.transform.scale(overig,(window_height,window_wight))


    # food variable
    food_x = random.randint(20,int(window_wight/2))
    food_y = random.randint(20,int(window_height/2))
    food_size = 10

    # sound variable 
    
    eating = pygame.mixer.Sound('eating.mp3')
    gamelose = pygame.mixer.Sound('gameloose.mp3')
    gamestart = pygame.mixer.Sound('gamestart.mp3')

    while not exit_game:    
        if game_over:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
                        gamestart.play()
                        gameloop()    

            window.fill(white)
            window.blit(overig,(0,0)) # show gameover screen
            show_score('Press Enter to contine',red,150,470) # show gemover lines
            show_score(f'Score:{score}',red,270,510)
            with open('highscore.txt','w') as f:
                f.write(str(highscore))

        else:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                        if velocity_x == 0:
                            velocity_x = u_velocity
                            velocity_y = 0 
                    if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                        if velocity_x == 0:
                            velocity_x = -u_velocity
                            velocity_y = 0 
                    if event.key==pygame.K_UP or event.key==pygame.K_w:
                        if velocity_y == 0:
                            velocity_y = -u_velocity
                            velocity_x = 0 
                    if event.key==pygame.K_DOWN or event.key==pygame.K_s:
                        if velocity_y == 0:   
                            velocity_y = u_velocity
                            velocity_x = 0     
                    if event.key==pygame.K_i:
                        if u_velocity < 10:
                           u_velocity +=1   
                    if event.key==pygame.K_o:
                        if u_velocity >1:
                           u_velocity -=1     
            snake_x += velocity_x
            snake_y += velocity_y 

            # Food event
            if abs(snake_x-food_x) < 8 and abs(snake_y-food_y) < 8:
                score += 10
                food_x = random.randint(20,int(window_wight/2))
                food_y = random.randint(20,int(window_height/2))
                snake_len +=5
                eating.play()

            # hite event
            if snake_x<0 or snake_x>window_height or snake_y<0 or snake_y>window_wight:
                gamelose.play()
                game_over = True
  
            # add head increase 
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            # file check 
            if (not os.path.exists('highscore.txt')):
                with open('highscore.txt','w') as f:
                    f.write('0')   
            # open file
            with open('highscore.txt','r') as f:
                highscore = f.read()
            # increase highscore or check
            if score > int(highscore):
                highscore = score

            # delete head
            if len(snake_list) > snake_len:      
                del snake_list[0]
            
            # hite evwent 
            if head in snake_list[:-1]:
                gamelose.play()
                game_over = True      

            window.fill(green)
            window.blit(bgiamge,(0,0)) # upload bg image 
            show_snake(window,black,snake_list,snake_size)
            show_line(f'Score:{score}',red,score_x,score_y)
            show_line(f'highscore:{highscore}',red,score_x+400,score_y)
            show_food(window,Magenta,food_x,food_y,food_size)
            line(window,red,window_height,window_wight)
        pygame.display.update()
        clock.tick(fps)
    

    pygame.quit()
    sys.exit()




# window variable 
window_height = 700
window_wight = 600

#color 
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)
green = (144,238,144)
Magenta = (255, 0, 255) 

window = pygame.display.set_mode((window_height,window_wight))
pygame.display.set_caption("gamers")

# font variable
font_name = 'Georgia'
font = pygame.font.SysFont(False,55)
style_font = pygame.font.SysFont(font_name,45)

# fps event
fps = 60    
clock = pygame.time.Clock()

homescreen()


