
class CollisionHandler:
	#Level class should init it and provide player and tiles
	def __init__(self, tiles):
		self.tiles = tiles

		#shit calculations - TODO
		self.current_x = 0.0
		# self.player_on_ground = False
		
	def horizontal_movement_collision(self, character) -> None:
		for sprite in self.tiles.sprites():
			if character.rect.colliderect(sprite.rect):
				if sprite.rect.top >= character.rect.bottom or sprite.rect.bottom <= character.rect.top:
					continue
				if character.direction_x < 0:
					character.rect.left = sprite.rect.right
					character.on_left = True
					self.current_x = character.rect.left
				elif character.direction_x > 0:
					character.rect.right = sprite.rect.left
					character.on_right = True
					self.current_x = character.rect.right

		if character.on_left and (character.rect.left < self.current_x or character.direction_x >= 0):
			character.on_left = False
		if character.on_right and (character.rect.right > self.current_x or character.direction_x <= 0):
			character.on_right = False

	def vertical_movement_collision(self, character) -> None:
		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(character.rect):
				if character.velocity_y > 0:
					character.rect.bottom = sprite.rect.top
					character.velocity_y = 0
					character.on_ground = True
				elif character.velocity_y < 0:
					character.rect.top = sprite.rect.bottom
					character.velocity_y = 0
					character.on_ceiling = True

		if character.on_ground and character.velocity_y < 0 or character.velocity_y > 1:
			character.on_ground = False
		if character.on_ceiling and character.direction_x > 0.1:
			character.on_ceiling = False