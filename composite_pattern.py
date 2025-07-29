from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operate(self):
        pass
        
        
        
class Leaf(Component):
    def __init__(self, name):
        super().__init__()
        self._name = name
    
    def operate(self):
        print(f"I am a leaf: {self._name}", flush=True)
    
    
class Composite(Component):
    def __init__(self, name):
        super().__init__()
        self._name = name
        self._children = []
        
    def add(self, component):
        self._children.append(component)
        
    def remove(self, component):
        self._children.remove(component)
        
    def operate(self):
        print(f"I am composite: {self._name}", flush=True)
        for child in self._children:
            child.operate()            
        
        
grandparents = Composite('Grand Parents')

grandparents.add(Leaf('Son Tom'))

parents = Composite('Son John')
parents.add(Leaf('Grand Daughter Michelle'))
parents.add(Leaf('Grand Son Nick'))
grandparents.add(parents)

grandparents.add(Leaf('Daughter Jane'))

grandparents.operate()
    