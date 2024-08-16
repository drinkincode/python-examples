import random



def basics1():
    print('Hello World')


    my_int = 13

    my_float = 10.22

    my_str = 'Take a sip'

    my_var = 'hello there ;)'

    my_list = [my_int, my_float, my_str]

    print(my_list)

    my_list.append(my_var)

    print(my_list)
def basics2(my_characters):
    for i in range(len(my_characters)):
        if my_characters[i] == 'John':
            my_characters[i] = my_characters[i] + ' is human'
        else:
            my_characters[i] = my_characters[i] + ' is not human'

character_1 = 'John'
character_2 = 'Gustavo Fring'
character_3 = 'R2D2'

my_characters = [character_1, character_2, character_3]

my_characters_dict = {
    'droid': character_3,
    'human': character_1,
    'bandit': character_2
}


def get_random_age():
    age = random.randint(1, 100)
    return age
    


class Character():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def print_character(self):
        print(f'Name: {self.name}, Age: {self.age}')

class Droid(Character):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_noise(self):
        print(f'{self.name} makes noise __.__._...')
        
class Wizard(Character):
    def __init__(self, name, age):
        super().__init__(name, age)

    def throw_fire_ball(self):
        print(f'{self.name} throws a fire ball >>>(*)')
        
class MasterWizard(Wizard):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.special_hat_color = 'purple'
        
    def print_hat(self):
        print(f'{self.name} says: I have a {self.special_hat_color} frickin hat, suck it losers!')



wizard_name = 'Harry Potter'
wizard_age = get_random_age()
wizard_obj = Wizard(wizard_name, wizard_age)

wizard_obj.print_character()
wizard_obj.throw_fire_ball()

print()

droid_name = 'R2D2'
droid_age = get_random_age()
droid_obj = Droid(droid_name, droid_age)

droid_obj.print_character()
droid_obj.make_noise()

print()

master_wizard_name = 'Dumbledore'
master_wizard_age = get_random_age()
master_wizard_obj = MasterWizard(wizard_name, wizard_age)

master_wizard_obj.print_character()
master_wizard_obj.throw_fire_ball()
master_wizard_obj.print_hat()
