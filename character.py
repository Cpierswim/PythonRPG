class Character:

    actions_since_last_stab = 0
    actions_since_last_explode = 0
    can_stab_after_actions_constat = 3
    can_stab_after_explode_constant = 10

    attack_types = {
            "slap": 1,
            "punch": 3, 
            "stab" : 10, 
            "explode": 20
        }

    def __init__(self, name, HP):
        self.name = name
        self.HP = HP

    def perform_attack(self, attack_name):
        self.HP -= self.attack_types[attack_name]

    def is_alive(self):
        return self.HP > 0

    def perform_attack(self, attack_damage):
        self.HP -= attack_damage
        