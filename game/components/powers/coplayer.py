from game.components.powers.power import Power
from game.utils.constants import SPACESHIP, COPLAYER_TYPE

class Coplayer(Power):

    def __init__(self):
        super().__init__(SPACESHIP, COPLAYER_TYPE)