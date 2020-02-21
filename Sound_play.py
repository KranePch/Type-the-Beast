import pygame
from os import path

snd_dir = path.join(path.dirname(__file__), 'Sounds')

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

sound_effects = {}
sound_effects["beast_death"] = []
sound_effects["key_board"] = []
sound_effects["other"] = []

try :
    
    pygame.mixer.music.load(path.join(snd_dir, 'little_town_orchestral.ogg'))
    beast_shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'beast_shoot.wav'))
    menu_pass = pygame.mixer.Sound(path.join(snd_dir, 'deal_key.ogg'))
    accept = pygame.mixer.Sound(path.join(snd_dir, 'Accept.ogg'))
    victory = pygame.mixer.Sound(path.join(snd_dir, 'winner.wav'))

    for i in range(2) : #Typing Sound     
        file_sound = pygame.mixer.Sound(path.join(snd_dir, 'cached_type{}.wav'.format(i + 2)) )
        sound_effects["key_board"].append(file_sound)
        
    for i in range(5):
        file_sound = pygame.mixer.Sound(path.join(snd_dir, 'death_{}.ogg'.format(i + 1)) )
        sound_effects["beast_death"].append(file_sound)
        
    print("Loading music done.")
except :
    print("Error Occured")
    running = False


