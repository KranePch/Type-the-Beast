from Vocabualary import *
from Sound_play import *
import pygame
import random
from os import path

#Define
img_dir = path.join(path.dirname(__file__), 'Images')

font_name = pygame.font.match_font('Arial')

BLACK = (0, 0, 0)

#Load sprites
background_img_ani = {}
background_img_ani["start"] = []
background_img_ani["hamburger"] = []
background_img_ani["sushi"] = []
background_img_ani["cookie"] = []
background_img_ani["victory"] = []

beast_img_ani = {}
beast_img_ani["walk"] = []
beast_img_ani["death"] = []
beast_img_ani["attack"] = []

alien_img_ani = {}
alien_img_ani["stand"] = []
alien_img_ani["lose"] = []
alien_img_ani["shoot"] = []

try :
        
    for i in range (10): #Alien standing animation upload.
        filename = 'alienstand_{}.png'.format(i + 1)    
        alien_img = pygame.image.load(path.join(img_dir, filename))
        alien_img.set_colorkey(BLACK)
        alien_img_ani["stand"].append(alien_img)
    print("Loading " + str(filename) + " done.")

    for i in range (10): #Alien death animation upload.
        filename = 'alienlose_{}.png'.format(i + 1)    
        alien_img = pygame.image.load(path.join(img_dir, filename))
        alien_img.set_colorkey(BLACK)
        alien_img_ani["lose"].append(alien_img)
    print("Loading " + str(filename) + " done.")

    for i in range (5): #Alien shoot animation upload.
        filename = 'alienshoot_{}.png'.format(i + 1)    
        alien_img = pygame.image.load(path.join(img_dir, filename))
        alien_img.set_colorkey(BLACK)
        alien_img_ani["shoot"].append(alien_img)
    print("Loading " + str(filename) + " done.")
    
    for i in range (8): #Beast walking animation upload
        filebeast = 'Predatorwalk_{}.png'.format(i + 1)
        beast_img = pygame.image.load(path.join(img_dir, filebeast))
        beast_img.set_colorkey(BLACK)
        beast_img_ani["walk"].append(beast_img)
    print("Loading " + str(filebeast) + " done. ")
        
    for i in range (10): #Beast death animation upload
        filebeast = 'Predatordeath_{}.png'.format(i + 1)
        beast_img = pygame.image.load(path.join(img_dir, filebeast))
        beast_img.set_colorkey(BLACK)
        beast_img_ani["death"].append(beast_img)
    print("Loading " + str(filebeast) + " done. ")

    for i in range (8): #Beast attack animation upload
        filebeast = 'predatorattack_{}.png'.format(i + 1)
        beast_img = pygame.image.load(path.join(img_dir, filebeast))
        beast_img.set_colorkey(BLACK)
        beast_img_ani["attack"].append(beast_img)
    print("Loading " + str(filebeast) + " done. ")
    
    for i in range (10): #Sushi background upload
        fileSpace = 'Sushi_{}.png'.format(i + 1)
        background_img = pygame.image.load(path.join(img_dir, fileSpace))
        background_img.set_colorkey(BLACK)
        background_img_ani["sushi"].append(background_img)
    print("Loading " + str(fileSpace) + " done. ")

    for i in range (10): #Hamburger background upload
        fileSpace = 'Background_{}.png'.format(i + 1)
        background_img = pygame.image.load(path.join(img_dir, fileSpace))
        background_img.set_colorkey(BLACK)
        background_img_ani["hamburger"].append(background_img)
    print("Loading " + str(fileSpace) + " done. ")

    for i in range (12): #Cookie background upload
        fileSpace = 'Cookie_{}.png'.format(i + 1)
        background_img = pygame.image.load(path.join(img_dir, fileSpace))
        background_img.set_colorkey(BLACK)
        background_img_ani["cookie"].append(background_img)
    print("Loading " + str(fileSpace) + " done. ")

    for i in range (10): #Start background upload
        fileSpace = 'Start_{}.png'.format(i + 1)
        background_img = pygame.image.load(path.join(img_dir, fileSpace))
        background_img.set_colorkey(BLACK)
        background_img_ani["start"].append(background_img)
    print("Loading " + str(fileSpace) + " done. ")

    for i in range (8): #Victory background upload
        fileSpace = 'Victory_{}.png'.format(i + 1)
        background_img = pygame.image.load(path.join(img_dir, fileSpace))
        background_img.set_colorkey(BLACK)
        background_img_ani["victory"].append(background_img)
    print("Loading " + str(fileSpace) + " done. ")
        
except :
    print("Error Occured")
    running = False


#Background
class Background(pygame.sprite.Sprite):
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.animated = "start"
        self.image = background_img_ani[self.animated][0]
        self.rect = self.image.get_rect()
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
        self.rewind = 1

    def update(self) :
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate :
            self.last_update = now
            self.frame += 1
            if self.frame < len(background_img_ani[self.animated]) : #Frame First - Last
                self.image = background_img_ani[self.animated][self.frame]
                self.rect = self.image.get_rect()                
            elif self.frame > len(background_img_ani[self.animated]) : #Frame Last - First
                self.image = background_img_ani[self.animated][ (len(background_img_ani[self.animated])) - self.rewind]
                self.rect = self.image.get_rect()
                self.rewind += 1
                if self.rewind == (len(background_img_ani[self.animated])) :
                    self.frame = -1
                    self.rewind = 1

#Alien
class Main_char(pygame.sprite.Sprite):
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.animated = "stand"
        self.image = alien_img_ani[self.animated][0]
        self.rect = self.image.get_rect()
        self.rect.move_ip(50, 290)
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
        self.death = False

    def update(self) :
        now = pygame.time.get_ticks()            
        if now - self.last_update > self.frame_rate :
            self.last_update = now
            self.frame += 1
            if self.frame == len(alien_img_ani[self.animated]) :
                self.frame = -1
                if self.death :
                    self.animated = "lose"
                    self.frame = 0
        
            else :
                self.image = alien_img_ani[self.animated][self.frame]
                self.rect = self.image.get_rect()
                self.rect.move_ip(50, 290)


#Beast
class Enemy(pygame.sprite.Sprite) :
    def __init__(self, speed, letter) :
        pygame.sprite.Sprite.__init__(self)

        self.xPos = 900 #Fixed start point (x)
        self.yPos = random.randint (10, 550) #Random y position
        self.animated = "walk"
        self.image = beast_img_ani[self.animated][0]
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.xPos, self.yPos)
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
        self.xMove = 0
        self.randomWord = str( vocab_set[letter][ random.randint(0, len( vocab_set[letter] ) -1) ] )
        self.speed = speed


    def update(self) : #Change frame and animation
        now = pygame.time.get_ticks()
        self.xMove += self.speed        #Walking Speed (1-10)
        if now - self.last_update > self.frame_rate :
            self.last_update = now
            self.frame += 1
            if self.animated == "death" :
                self.speed = 0
            if self.frame == len(beast_img_ani[self.animated]) :
                self.frame = -1
                if self.animated == "death" :
                    self.kill()

            else : #Keep the frame change
                self.image = beast_img_ani[self.animated][self.frame]
                self.rect = (self.xPos - self.xMove, self.yPos)

        if (self.xPos - self.xMove <= 200) :
            self.xMove -= self.speed
            self.animated = "attack"

    def draw_text(self, surf, text, size, x, y, color):
        font = pygame.font.Font(font_name,size)
        text_surface = font.render(text,True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        surf.blit(text_surface,text_rect)

    def get_text(self) :
        return self.randomWord




