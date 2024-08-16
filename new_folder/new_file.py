def turn_list_to_zeros(any_list):
    for i in range(len(any_list)):
        any_list[i] = 0
        
    return any_list


class Person():
    def __init__(self, age, name='no name'):
        self.age = age
        self.name = name
        
    def print_name(self):
        print(self.name)