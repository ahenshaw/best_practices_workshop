
class Animal:
    '''
    Base class of our zoo.
    '''
    description = "animal"
    def __init__(self, weight):
        self.weight = weight

    def __str__(self):
        return f"Description: {self.description}\nWeight: {self.weight}"

    def update_weight(self, new_weight):
        self.weight = new_weight

    

class Elephant(Animal):
    '''
    A specific animal.
    '''
    description = "elephant"


e = Elephant(1000)
print(e)
e.update_weight(1110)
print(e)
