from os import walk
import pygame
from collections import namedtuple

pygame.font.init()

game_state = namedtuple('game_state', ['main_menu', 'playing', 'paused', 'dead', 'win'])
directions = namedtuple('direction_states', ['STILL','RIGHT', 'LEFT'])
level_objects = namedtuple("level_objects", ['tiles','player_list','cages','enemies','enemy_borders'])

tile_info = namedtuple('tile_info',['spawn','num'])
enemy_info = namedtuple('enemy_info',['spawn','num'])
TEXT_FONT = pygame.font.Font("resources/font/dynamo.otf", 60)

TIME_COUNTING_SPEED = 0.1

def import_folder(path, size: tuple):
	surface_list = []
	for _,__,img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			image_surf = pygame.transform.scale(image_surf, size)
			surface_list.append(image_surf)

	return surface_list

