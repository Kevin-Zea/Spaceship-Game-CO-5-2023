from game.components.powers.power import Power
from game.utils.constants import SHOOT_POWER, SHOOT_TYPE

class TreeShoot(Power):
    
    def __init__(self):
        super().__init__(SHOOT_POWER, SHOOT_TYPE)