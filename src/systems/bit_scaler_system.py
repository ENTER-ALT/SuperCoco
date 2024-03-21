import utilities

TOLERANCE = 0.20

class BitScalerSystem():
    def __init__(self, created_objects: utilities.level_objects):
        self.scaling_objects = []
        enemies, cages, player = created_objects.enemies, created_objects.cages, created_objects.player_list.sprite
        for enemy in enemies:
            self.scaling_objects.append(enemy)
        for cage in cages:
            self.scaling_objects.append(cage)
        self.scaling_objects.append(player)

        self.timer = 0
        self.considered_time = 1
        self.scaled = False

    def update(self, delta_time):
        # for obj in self.scaling_objects:
        #     if self.timer>=1.0:
        #         self.timer = 0 
        #         if self.scaled:
        #             print("scaled")
        #             obj.image = pygame.transform.scale(obj.image, (obj.image.get_height()-200, obj.image.get_width()-200))
        #             self.scaled = False
        #         else:
        #             print("unscaled")
        #             obj.image = pygame.transform.scale(obj.image, (obj.image.get_height()+200, obj.image.get_width()+200))
        #             self.scaled = True

        # self.timer += delta_time / 10
        pass
        

        #channel(0) for player
        #channel(1) for enemy
        #channel(2) for cage
        
