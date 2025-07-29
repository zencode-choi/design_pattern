from abc import ABC, abstractmethod

class MediatorInterface(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass
    
class ConcreteMediator(MediatorInterface):
    def __init__(self, comp1, comp2):
        # super().__init__()
        self.comp1: BaseComponent = comp1
        self.comp1.set_mediator(self)
        self.comp2: BaseComponent = comp2
        self.comp2.set_mediator(self)
        
    def notify(self, sender, event):
        if event == 'A':
            print("mediator react on A event --> trigger comp2 C action")
            self.comp2.do_c()
        elif event == 'D':
            print("mediator react on D event --> trigger comp1 B action")
            self.comp1.do_b()
    
class BaseComponent:
    def __init__(self):
        self.mediator = None
        
    def set_mediator(self, mediator):
        self.mediator = mediator

        
class Component1(BaseComponent):
    def do_a(self):
        """trigger action"""
        print("component1 act A")
        self.mediator.notify(self, "A")
        
    def do_b(self):
        """reciever action"""
        self.mediator.notify(self, "B")

class Component2(BaseComponent):
    def do_c(self):
        """reciever action"""
        self.mediator.notify(self, "C")
        
    def do_d(self):
        """trigger action"""
        print("component2 act D")
        self.mediator.notify(self, "D")
            

component1 = Component1()
component2 = Component2()
mediator = ConcreteMediator(comp1=component1, comp2=component2)

component1.do_a()  # trigger action
component2.do_d()  # trigger action
            