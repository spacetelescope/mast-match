class Card:
    def __init__(self, card_type, name, wave=None, obj_type=None, dtype=None, reqs=None):
        # type is one of: astronomical observation, science goal, telescope, chaos
        self.card_type = card_type
        self.name = name

        if self.card_type == 'obs':
            self.obj_type = obj_type
            self.dtype = dtype
        
        elif self.card_type == 'goal':
            self.reqs = reqs
        
        elif self.card_type == 'telescope':
            self.wave = wave

        # complex. implement later
        elif self.card_type == 'chaos':
            return
        
        else:
            print(f"{self.name} is an invalid card type.")