import pygame
pygame.mixer.pre_init(22050, -16, 1, 512)

DAMAGE_SOUND = 'damage'
WARNING_SOUND = 'warning'
SPINNING_SOUND = 'spinnging'
ROTATING_SOUND = 'rotating'
CAGE_SOUND = 'cage'

class SoundMixer():
    def __init__(self, game):
        self.playlist = {
                'main': 'resources/music/main_menu.wav', 
                'playing':'resources/music/gameplay.wav', 
                'dead':'resources/music/dead.wav', 
                'win':'resources/music/winner.wav'
        }
        self.sounds= {
                'damage': 'resources/sounds/damage.mp3', 
                'warning': 'resources/sounds/warning.wav', 
                'spinnging': 'resources/sounds/spinning.wav', 
                'rotating': 'resources/sounds/rotating.wav', 
                'cage': 'resources/sounds/cage.wav'
        }
        #channel(0) for player
        #channel(1) for enemy
        #channel(2) for cage
        self.previous_game_state = game.state
        self.channels = [pygame.mixer.Channel(n) for n in range(0, 3)]
        self.play_background(game)

    def play_background(self,game):
        if game.state == game.mode.main_menu:
            pygame.mixer.music.load(self.playlist['main'])
            pygame.mixer.music.play(-1)
        if game.state == game.mode.playing or game.state == game.mode.paused:
            pygame.mixer.music.load(self.playlist['playing'])
            pygame.mixer.music.play(-1)
        if game.state == game.mode.dead:
            pygame.mixer.music.load(self.playlist['dead'])
            pygame.mixer.music.play(-1)
        if game.state == game.mode.win:
            pygame.mixer.music.load(self.playlist['win'])
            pygame.mixer.music.play(-1)

    def play_sound(self, sound_name: str) -> None:
        if sound_name not in self.sounds.keys():
            return
        sound = pygame.mixer.Sound(self.sounds[sound_name])
        sound.play()
        
