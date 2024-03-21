from components.interact_component import InteractComponent
from components.interactive_component import InteractiveComponent

class InteractionDetectionHandler:
	#Level class should init it and provide player and tiles
	def __init__(self, cages):
		self.cages = cages

	def update(self, character: InteractComponent) -> None:
		if not isinstance(character, InteractComponent):
			raise ValueError
		for sprite in self.cages.sprites():
			if sprite.rect.colliderect(character.rect) and sprite is not character.interact_target and isinstance(sprite, InteractiveComponent):
				character.interact_target = sprite

		if character.interact_target and not character.interact_target.rect.colliderect(character.rect):
			character.interact_target = None