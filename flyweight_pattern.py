class Flyweight:
    def __init__(self, intrinsic_state):
        self._intrinsic_state = intrinsic_state
        
    def operate(self, extrinsic_state):
        print(f"Intrinsic state {self._intrinsic_state}, Extrinsic state: {extrinsic_state}")
        
class FlyweightFactory:
    _flyweight = {}
    
    @staticmethod
    def get_flyweight(key):
        if key not in FlyweightFactory._flyweight:
            FlyweightFactory._flyweight[key] = Flyweight(key)
        return FlyweightFactory._flyweight[key]
    

flyweight1 = FlyweightFactory.get_flyweight("internal state A")
flyweight1.operate("external state 1")

flyweight2 = FlyweightFactory.get_flyweight("internal state A")
flyweight2.operate("external state 2")

print(flyweight1 is flyweight2)