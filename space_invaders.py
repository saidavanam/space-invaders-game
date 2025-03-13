import pygame
import random
from pygame import mixer

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((800, 600)) ## create a screen.(width,height)
# set_mode() method creates a window of the desired size and returns a Surface object that represents the window.
# (0,0) at top left corner and (799,599) at bottom right corner.

background = pygame.image.load('space_background.jpg') # load the image
#if background file is heavy then loop may run slow and in that case increase the speed of the player and enemy 

background = pygame.transform.scale(background,(800,600)) # scale the image to the desired size

#background sound
mixer.music.load('background.wav')
mixer.music.play(-1) # -1 is used to play the music in loop

pygame.display.set_caption("space invaders") # set the title of the window
icon = pygame.image.load('ufo.png') # load the image. make sure you use 32x32 image.only as icon
pygame.display.set_icon(icon)



#player
player1img = pygame.image.load('player1.png')
player1X = 370
player1Y = 480
player1Xchange = 0 # change in X coordinate of player1
player1Ychange = 0 # change in Y coordinate of player1
# X and Y coordinates of player1.

#enemy
enemies = []
enemyX = []
enemyY = []
enemyXchange = []
enemyYchange = []
num_enemies = 6

for i in range(num_enemies):
    enemies.append(pygame.image.load('enemy1.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(0,80))
    enemyXchange.append(2)
    enemyYchange.append(40)

#bullet
# Bullet setup
bulletimg = pygame.image.load('bullet.png')
bullets = []  # List to store multiple bullets
bulletYchange = 0.5


score = 0
font = pygame.font.Font('freesansbold.ttf',32) #second argument is font size
#This is th font given by pygame to display the score on the screen. If we want other fonts download from google and use it.
textX = 10
textY = 10

#game over text
over_font = pygame.font.Font('freesansbold.ttf',32)

def game_over_text():
    global score
    over_text = over_font.render(f"GAME OVER.YOUR SCORE:{score}",True,(255,0,0))
    screen.blit(over_text,(200,250))

def show_score(x,y):
    global score
    score_value = font.render("Score: "+str(score),True,(0,255,0))
    screen.blit(score_value,(x,y))



def player(x,y):
    # screen.blit(player1img,(player1X,player1Y)) # blit() method is used to draw the player on the screen
    # blit() method takes 2 arguments, first is the image and second is the coordinates where the image should be placed

    screen.blit(player1img,(x,y))

def enemy(x,y,i):
    screen.blit(enemies[i],(x[i],y[i]))

def fire_bullet(x,y):
    bullets.append([x+16,y]) # append new bullet at player's position


def iscollision(enemyX,enemyY,bulletX,bulletY): #collision detection function
    distance = ((enemyX-bulletX)**2 + (enemyY-bulletY)**2)**0.5
    if distance < 27:
        return True
    else:
        return False
    


# while True:
#     pass -> using this syntax will make the program run forever so system will hang

#to prevent the system from hanging, we can use events
# Events are actions that are detected by the program like closing the window,pressing mouse button, pressing keyboard key etc..
running = True
while running:
    screen.fill((0,0,0)) # fill the screen with black color.use rapidtables.com to get the RGB values of any color
    screen.blit(background,(0,0)) # draw the background image on the screen

    for event in pygame.event.get(): # get all the events that are happening
        if event.type == pygame.QUIT: #pygame.QUIT is an event that is triggered when the close button is clicked
            running = False

        # if keystroke  is pressed check whether its right or left
        if event.type == pygame.KEYDOWN: # check if any key is pressed
            if event.key == pygame.K_LEFT: # check if the key pressed is left arrow key
                player1Xchange -= 0.3
                # print("Left arrow is pressed")

            if event.key == pygame.K_RIGHT: # check if the key pressed is right arrow key
                player1Xchange += 0.3
                # print("Right arrow is pressed")  
            
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound('laser.wav')
                bullet_sound.play()
                fire_bullet(player1X,player1Y)
            
            # if event.key == pygame.K_UP: # check if the key pressed is up arrow key
            #     player1Ychange -= 0.1
            #     print("Up arrow is pressed")
            
            # if event.key == pygame.K_DOWN: # check if the key pressed is down arrow key
            #     player1Ychange += 0.1
            #     print("Down arrow is pressed")


        if event.type ==pygame.KEYUP: #releasing the key after pressing
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player1Xchange,player1Ychange = 0,0 #stopping the player when the key is released
                # print("keystroke has been released")



    player1X += player1Xchange

    if player1X <=0: # if player1 crosses the left boundary of the screen
        player1X = 0 # set the X coordinate of player1 to 0
    if player1X >=736: # if player1 crosses the right boundary of the screen. we took 736 because the width of the player1 image is 64
        player1X = 736 # set the X coordinate of player1 to 736

    

    for i in range(num_enemies):


        if enemyY[i] > 416:
            for j in range(num_enemies):
                enemyY[j] = 2000
            game_over_text() 
        if  enemyX[i] <=0: # if enemy1 crosses the left boundary of the screen
            enemyXchange[i] = 0.3 # set the X coordinate of enemy1 to 0.3
            enemyY[i] += enemyYchange[i]
        elif  enemyX[i] >=736: 
            enemyXchange[i] = -0.3
            enemyY[i] += enemyYchange[i]
        enemyX[i] += enemyXchange[i]

        new_bullets = []
        for bullet in bullets:
            bullet[1] -= bulletYchange
            if bullet[1] >0:
                new_bullets.append(bullet)
                screen.blit(bulletimg,(bullet[0],bullet[1]))
            if iscollision(enemyX[i],enemyY[i],bullet[0],bullet[1]):
                explosion_sound = mixer.Sound('explosion.wav')
                explosion_sound.play()
                score += 1
                print("Score:", score)
                enemyX[i], enemyY[i] = random.randint(0, 735), random.randint(50, 150)
        bullets = new_bullets


        enemy(enemyX,enemyY,i)



    player(player1X,player1Y) # draw the player on the screen.
    # player1X -= 0.1 # move the player to the right by particular amount of pixels.(+ for right,- for left)
    # player1Y -= 0.1 #move the player to the TOP AND + FOR BOTTOM
    # player1 disappears from the screen when player1 crosses beyond the screen boundaries.(No runtime error is detected)
    #player1x position is x coordinate where player1 image starts.It is not the center of the player1 image.
    
    





    show_score(textX,textY)
    pygame.draw.line(screen, (255, 0, 0), (0, 480), (800, 480), 3)  # Red boundary line
    pygame.display.update() # update the screen after adding anything to screen