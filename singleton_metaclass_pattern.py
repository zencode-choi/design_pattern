# ref : https://jroomstudio.tistory.com/41

class MetaclassSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaclassSingleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class ConcreteSingletonA(metaclass=MetaclassSingleton):
    pass

class ConcreteSingletonB(metaclass=MetaclassSingleton):
    pass


t = ConcreteSingletonA()
t2 = ConcreteSingletonB()
