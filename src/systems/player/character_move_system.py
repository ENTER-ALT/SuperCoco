class CharacterMoveSystem:
	def horizontal_movement(self, character, delta_time: float) -> None:
		character.rect.x += character.direction_x * character.speed * delta_time

	def vertical_movement(self, character, delta_time: float) -> None:
		character.rect.y += character.velocity_y * delta_time