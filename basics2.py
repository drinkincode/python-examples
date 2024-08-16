from new_folder.new_file import turn_list_to_zeros, Person

print('Hello World')

x = 10

my_float = 343.343

my_str = 'take a sip'

my_list = [x, my_float, my_str, 'hello', 30]

my_list[2] = 'new stuff'

print(my_list[2])

my_list.append('add to the end')

print(my_list)


    
all_zeros_list = turn_list_to_zeros(my_list)

print(all_zeros_list)


class Person():
    def __init__(self, age, name='no name'):
        self.age = age
        self.name = name
        
    def print_name(self):
        print(self.name)
        
        
        
class Wizard(Person):
    def __init__(self, age, name='no name'):
        super().__init__(age, name)
        self.hat = 'red'
    
    def cast_fireball(self):
        print(f'{self.name}: Uses Fireball... With a {self.hat} hat')
        
john = Person(67, 'John')
john.print_name()

sarah = Person(34, 'Sarah')
sarah.print_name()

harry = Wizard(122, 'Harry')
harry.print_name()
harry.hat = 'green'
harry.cast_fireball()