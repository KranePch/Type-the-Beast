from Character_class import *
import pygame
import random
import time
from os import path

display_width = 1024
display_height = 768
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Initial pygame
pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Type the Beast")
clock = pygame.time.Clock()
pygame.mixer.music.play(-1)

#Draw player text
globals()["font_name_player"] = pygame.font.match_font('Arial')
def draw_text_player(surf, text, size, x, y, color):
    font = pygame.font.Font(font_name_player,size)
    text_surface = font.render(text,True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface,text_rect)

#Beast process
    
def run_Beast_process(beast_variable) :
    #Initial Sprites
    Alien = Main_char()
    sprites_alien = pygame.sprite.Group()
    sprites_alien.add(Alien)
    sprites_beast = pygame.sprite.Group()
    sprites_beast.add(beast_variable)
    player_text = ""
    beast_word = beast_variable.get_text()

    while (1) :
        clock.tick(FPS)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP : #Receive input
                if not ( keys[pygame.K_BACKSPACE] or keys[pygame.K_RETURN]
                         or keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT] or keys[pygame.K_LCTRL]) :
                    player_text += chr(event.key).upper()
                    sound_effects["key_board"][ random.randint(0,1) ].play()
                    
                elif keys[pygame.K_BACKSPACE] : #Delete Text
                    player_text = player_text[:(len(player_text)-1)]
                    
                elif keys[pygame.K_RETURN] : #Check input
                    print(str(player_text) + " and " + str(beast_word))
                    temp_var = str(player_text)
                    player_text = ""
                    
                    if (str(temp_var) == str(beast_word)) : #Collect words!
                        sound_effects["beast_death"][ random.randint(0, 4) ].play()
                        Alien.frame = 0
                        Alien.animated = "shoot"
                        beast_variable.animated = "death"
                        beast_variable.frame = 0

        if (beast_variable.animated == "attack" and beast_variable.frame == 7):
            beast_shoot_sound.play()
            Alien.animated = "lose"
            sound_effects["beast_death"][ random.randint(0, 4) ].play()       
        if (Alien.animated == "lose" and Alien.frame == 9) :
            main() # If lose, back to main
                                                            
        background_in_game.update()
        sprites_alien.update()
        sprites_beast.update()
    
        #Draw 
        screen.fill(BLACK)
        background_in_game.draw(screen)
        draw_text_player(screen,player_text, 30, 510 ,680,WHITE) #Player real-time text
        sprites_alien.draw(screen)
        sprites_beast.draw(screen)
        if beast_variable.animated == "walk" : #While beast alive, keeps text
            beast_variable.draw_text(screen,beast_word,21,
                                     (beast_variable.xPos - beast_variable.xMove) + 45,beast_variable.yPos + 165,WHITE)
            beast_variable.draw_text(screen,beast_word,21,
                                     510, 20,WHITE) 
        elif beast_variable.animated == "death" and beast_variable.frame == 9 :
            return # If beast death, spawn the next one
                   
        pygame.display.flip()
    
#Create Menu
def start_bg_menu(animated) :
    waitKey = True
    stage.animated = animated
    background_in_game.add(stage)
    while waitKey :
        background_in_game.draw(screen)
        if animated == "start": # Instruction
            globals()["font_name_player"] = pygame.font.match_font('Northingtown')
            draw_text_player(screen, "HOW TO PLAY", 30, 170, 600, WHITE)
            draw_text_player(screen, "TEXT THE WORD SHOWN ON SCREEN", 25, 170, 650, WHITE)
            draw_text_player(screen, "PRESS ENTER ", 25, 90, 680, WHITE)
        pygame.display.flip()
        clock.tick(FPS)
        background_in_game.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()               
            if event.type == pygame.KEYUP:
                accept.play()
                globals()["font_name_player"] = pygame.font.match_font('Arial')
                time.sleep(0.07)
                waitKey = False
                if stage.animated == "victory":
                    main()
                else :
                    stage.animated = "hamburger"
    
#mainloop
def main() :
    menu = True
    running = True
    
    #Initalize Background picture
    globals()["stage"] = Background()
    globals()["background_in_game"] = pygame.sprite.Group()
    
    #Initial Beast as variable beast_NO_#   
    for beastUpload in range (1, 2): #Beast1
        globals()['beast_NO_%s' % beastUpload] = Enemy(3, "3-letter")
        
    for beastUpload in range (2, 4): #Beast1.5
        globals()['beast_NO_%s' % beastUpload] = Enemy(5, "3-letter")
        
    for beastUpload in range (20, 22): #Beast2
        globals()['beast_NO_%s' % beastUpload] = Enemy(3, "6-letter")
        
    for beastUpload in range (23, 25): #Beast2.5
        globals()['beast_NO_%s' % beastUpload] = Enemy(4, "6-letter")
        
    for beastUpload in range (30, 33): #Beast3
        globals()['beast_NO_%s' % beastUpload] = Enemy(2, "8-letter")
        
    for beastUpload in range (33, 35): #Beast3.5
        globals()['beast_NO_%s' % beastUpload] = Enemy(3, "8-letter")

    for beastUpload in range (35, 37): #Beast3.75
        globals()['beast_NO_%s' % beastUpload] = Enemy(5, "8-letter")

    for beastUpload in range (41, 46): #Beast4
        globals()['beast_NO_%s' % beastUpload] = Enemy(5, "unknown")
  
    while running :       
        if menu:
            start_bg_menu("start")
            menu = False
            
        #STAGE 1
        stage.animated = "hamburger"
        run_Beast_process(beast_NO_1)
        run_Beast_process(beast_NO_2)
        run_Beast_process(beast_NO_41)
        run_Beast_process(beast_NO_3)
        
        #STAGE 2   
        stage.animated = "sushi"
        run_Beast_process(beast_NO_20)
        run_Beast_process(beast_NO_42)
        run_Beast_process(beast_NO_21)
        run_Beast_process(beast_NO_43)
        run_Beast_process(beast_NO_23)
        run_Beast_process(beast_NO_24)
        
        #STAGE 3
        stage.animated = "cookie"
        run_Beast_process(beast_NO_30)
        run_Beast_process(beast_NO_31)
        run_Beast_process(beast_NO_44)
        run_Beast_process(beast_NO_32)
        run_Beast_process(beast_NO_45)
        run_Beast_process(beast_NO_33)
        run_Beast_process(beast_NO_34)
        run_Beast_process(beast_NO_35)
        run_Beast_process(beast_NO_36)
        
        #END GAME
        victory.play()
        stage.animated = "victory"
        start_bg_menu(stage.animated)

        
    pygame.quit()
    quit()
    
#Run Program
main()

        
