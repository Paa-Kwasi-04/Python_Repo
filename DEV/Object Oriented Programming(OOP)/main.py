class Character:
    def __init__(self, name: str, attack_power: int, life: int):
        self.name = name
        self.attack_power = attack_power
        self.life = life

    def __repr__(self):
        return f'<Class \'Character\'>'


villain = Character('Thanos', 400, 1500)
