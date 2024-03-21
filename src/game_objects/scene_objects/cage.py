import pygame

from src.game_objects.scene_objects.scene_object import SceneObject
from src.components.interactive_component import InteractiveComponent
import src.utilities as utilities

HAPPY_COCO_PATH = 'resources/coconut_cages/happy_coco.png'
CAGE = 'cage'
RELIEVED = 'relieved'

class CoconutCage(SceneObject, InteractiveComponent):
    def __init__(self, num, position, size):
        super().__init__(size)
        self.import_character_assets()
        InteractiveComponent.__init__(self)
        self.status = 'cage'

    def import_character_assets(self) ->None:
        character_path = 'resources/coconut_cages/'
        animations = {'cage':[],'relieved':[]}

        for animation in animations.keys():
            full_path = character_path + animation
            animations[animation] = utilities.import_folder(full_path, self.image_size)

        self.image = animations['cage'][0]
        self.rect = self.image.get_rect()

        self.animations = animations
        self.frame_index = 0
        self.animation_speed = 1

    def update(self):
        self.animate()

    def animate(self) -> None:
        if len(self.animations.keys()) < 1:
            return
        animation = self.animations[self.status]

		# loop over frame index 
        self.frame_index += utilities.TIME_COUNTING_SPEED * len(animation) *  self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        self.image = image

    def use(self):
        super().use()
        self.image = pygame.image.load(HAPPY_COCO_PATH)
        self.image = pygame.transform.scale(self.image, self.image_size)
        self.status = "relieved"
        
