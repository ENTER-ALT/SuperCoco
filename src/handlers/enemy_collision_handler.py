TOLERANCE = 20

class EnemyCollisionHandler:
	#Level class should init it and provide player and tiles
	def __init__(self, borders):
		self.borders = borders

		#shit calculations - TODO
		self.current_x = 0.0
		# self.player_on_ground = False
		
	def horizontal_movement_collision(self, enemy) -> None:
		for sprite in self.borders.sprites():
			if enemy.rect.colliderect(sprite.rect):
				if enemy.direction_x < 0 and abs(enemy.rect.left - sprite.rect.centerx) <= TOLERANCE:
					enemy.on_left = True
					enemy.direction_x = enemy.runs.RIGHT
					self.current_x = enemy.rect.left
				elif enemy.direction_x > 0 and abs(enemy.rect.right - sprite.rect.centerx) <= TOLERANCE:
					enemy.on_right = True
					enemy.direction_x = enemy.runs.LEFT
					self.current_x = enemy.rect.right

		if enemy.on_left and (enemy.rect.left+2 < self.current_x or enemy.direction_x >= 0):
			enemy.on_left = False
		if enemy.on_right and (enemy.rect.right-2 > self.current_x or enemy.direction_x <= 0):
			enemy.on_right = False