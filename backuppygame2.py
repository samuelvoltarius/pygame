#Dino Bilder by Arks
#https://arks.itch.io/dino-characters
#https://twitter.com/ScissorMarks



import pygame

#eingaben

screen_size = (700,500)
dunkelgrau = (50,50,50)
Mustard = (209,206,25)

# init

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Alfis erstes Spiel")
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 24)


#player


hp_image = pygame.image.load("images/heart.png")

coin_image = pygame.image.load("images/coin_0.png")
coin_w = 20
coin_h = 20

coins = [pygame.Rect(100,200,24,24),pygame.Rect(250,250,coin_h,coin_w),pygame.Rect(350,250,coin_h,coin_w)]

score = 0

player_image = pygame.image.load("images/vita00.png")
player_w = 60
player_h = 69

player_x = 300
player_y = 0

player_speed = 0
player_acceleration = 0.2



#Gegner

monster_image = pygame.image.load("images/monster.png")
monster = [pygame.Rect(150,274,29,19)]

lives = 3

#platform

platform = [pygame.Rect(100,300,400,50),pygame.Rect(100,250,50,50),pygame.Rect(450,250,50,50)]

#mitte
#mitte_platform = pygame.Rect(100,300,400,50)
#links 
#links_platform = pygame.Rect(100,250,50,50)

#rechts
#rechts_platform = pygame.Rect(450,250,50,50)

new_player_x = player_x
new_player_y = player_y

running = True
while running:



# game loop

    #-------
    # imput (palyer input)
    #------


    # check for quit
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
    


    #player input
    #links und rechts
    keys = pygame.key.get_pressed()
    # a links
    # d rechts
    if keys[pygame.K_a]:
        new_player_x -=1
    if keys[pygame.K_d]:
        new_player_x += 1
## JUmp
    if keys[pygame.K_w] and player_on_grounde:
        player_speed = -5
 


    #vertrical (jump)

    player_speed += player_acceleration
    new_player_y += player_speed
  


    # überprüfen Player_x
# Gegner


    player_rect = pygame.Rect(new_player_x,new_player_y,player_w,player_h)
    for c in coins:
        if c.colliderect(player_rect):
            coins.remove(c)
            score += 1



 #Münzen sammel
    for m in monster:
        if m.colliderect(player_rect):
            lives -= 1
            # reset spieler
            player_x = 300
            player_y = 0
            player_speed = 0
        
    print(lives)

# überprüfen Player_x

    new_player_rect = pygame.Rect(new_player_x,new_player_y,player_w,player_h)

    x_collision = False

    for p in platform:
        if p.colliderect(new_player_rect):
            x_collision = True
        break

    if x_collision == False:
        player_x = new_player_x



    # überprüfen glayer_y
    new_player_rect = pygame.Rect(new_player_x,new_player_y,player_w,player_h)

    y_collision = False
    player_on_grounde = False
    for p in platform:
        if p.colliderect(new_player_rect):
            y_collision = True
            player_speed = 0
            # wenn die Platform unter ihm ist
            if p[1]> new_player_y:
                #player festkleben
                player_y = p[1] - player_h
                player_on_grunde = True
            

    if x_collision == False:
        player_y = new_player_y


    # update

    # ausgabe

    #hintergrund
    screen.fill(dunkelgrau)

    


    #Platform
    for p in platform:
        pygame.draw.rect(screen, Mustard, p)
    #pygame.draw.rect(screen, Mustard, mitte_platform)
    #pygame.draw.rect(screen, Mustard, links_platform)
    #pygame.draw.rect(screen, Mustard, rechts_platform)

    #münzen

    for c in coins:
        screen.blit(coin_image, (c.x,c.y))


    #monster
    for m in monster:
        screen.blit(monster_image, (m.x,m.y))
        
    #spieler
    screen.blit(player_image, (player_x,player_y))

    #Gui

    #score
    score_text = font.render("Punkte: " + str(score), True, Mustard, dunkelgrau)
    score_text_rectangle = score_text.get_rect()
    score_text_rectangle.x = 50
    score_text_rectangle.y = 50
    screen.blit(score_text, score_text_rectangle)
    
    #hp
    for l in range(lives):
        screen.blit(hp_image, (200 + (l*50),0))

#screen
    pygame.display.flip()
    clock.tick(100)


# quit


pygame.quit()