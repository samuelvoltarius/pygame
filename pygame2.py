#Dino Bilder by Arks
#https://arks.itch.io/dino-characters
#https://twitter.com/ScissorMarks



import pygame
import engine


def drawText(t, x, y):
            #score
        text = font.render(t,True, Mustard, dunkelgrau)
        text_rectangle = text.get_rect()
        text_rectangle.topleft = (x,y)
        screen.blit(text, text_rectangle)
        
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

#Game status (Playing; tot, win)
game_state = "playing"

#player


hp_image = pygame.image.load("images/heart.png")

coin_animation = engine.Animation(
    pygame.image.load("images/coin_0.png"),
    pygame.image.load("images/coin_1.png"),
    pygame.image.load("images/coin_2.png"),
    pygame.image.load("images/coin_3.png"), 
    pygame.image.load("images/coin_4.png"), 
    pygame.image.load("images/coin_5.png")
)


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

player_directions = "right"

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
    
    if game_state == "playing":

        new_player_x = player_x
        new_player_y = player_y


        #player input
        #links und rechts
        keys = pygame.key.get_pressed()
        # a links
        # d rechts
        if keys[pygame.K_a]:
            new_player_x -= 2
            player_directions = "left"
        if keys[pygame.K_d]:
            new_player_x += 2
            player_directions = "right"     	
    ## JUmp

        if keys[pygame.K_w] and player_on_grunde:
            player_speed = -5

    if game_state == "playing":
        coin_animation.update()
        new_player_rect = pygame.Rect(new_player_x,new_player_y,player_w,player_h)

        x_collision = False

        for p in platform:
            if p.colliderect(new_player_rect):
                x_collision = True
            break

        if x_collision == False:
            player_x = new_player_x
        #vertrical (jump)

        player_speed += player_acceleration
        new_player_y += player_speed

        # überprüfen glayer_y
        new_player_rect = pygame.Rect(new_player_x,new_player_y,player_w,player_h)

        y_collision = False
        player_on_grunde = False
        for p in platform:
            if p.colliderect(new_player_rect):
                y_collision = True
                player_speed = 0
                # wenn die Platform unter ihm ist
                if p[1]> new_player_y:
                    #player festkleben
                    player_y = p[1] - player_h
                    player_on_grunde = True
                break

        if y_collision == False:
            player_y = new_player_y



        # überprüfen Player_x
    # Gegner


        player_rect = pygame.Rect(new_player_x,new_player_y,player_w,player_h)
        for c in coins:
            if c.colliderect(player_rect):
                coins.remove(c)
                score += 1
                if score >=3:
                    game_state = "gewonnen"



    #Münzen sammel
        for m in monster:
            if m.colliderect(player_rect):
                lives -= 1
                # reset spieler
                player_x = 300
                player_y = 0
                player_speed = 0
                #gamge status
                if lives <= 0:
                    game_state = "verloren"
        print(lives)


    # update

    # ausgabe

    #hintergrund
    screen.fill(dunkelgrau)

    


        #Platform
    for p in platform:
        pygame.draw.rect(screen, Mustard, p)
        

        #münzen

    for c in coins:
        #screen.blit(coin_image, (c.x,c.y))
        coin_animation.draw(screen, c.x, c.y)


        #monster
    for m in monster:
        screen.blit(monster_image, (m.x,m.y))
            
        #spieler
        if player_directions == "right":
            screen.blit(player_image, (player_x,player_y))
        elif player_directions == "left":
            screen.blit(pygame.transform.flip(player_image, True, False), (player_x, player_y))

        #Gui

        #score
        screen.blit(coin_image, (10,10))
        drawText(str(score), 50, 10)
        #score_text = font.render("Punkte: " + str(score), True, Mustard, dunkelgrau)
        #score_text_rectangle = score_text.get_rect()
        #score_text_rectangle.topleft = (10,19)
        #screen.blit(score_text, score_text_rectangle)
        

        #hp
    for l in range(lives):
        screen.blit(hp_image, (200 + (l*50),10))

    if game_state == "gewonnen":
        drawText("Gewonnen", 50,50)

    if game_state == "verloren":
        drawText("verloren", 50,50)
    #screen
    pygame.display.flip()
    clock.tick(100)


# quit


pygame.quit()