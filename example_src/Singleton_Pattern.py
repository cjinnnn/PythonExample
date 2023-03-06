class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance

class LazyInstantiation:
    _instance = None
    def __init__(self):
        if not self._instance:
            print("instance None")
        else:
            print(f"instance {self.getInstance()}")
 
    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = LazyInstantiation()
        return cls._instance

class SingletonInstance:
  __instance = None

  @classmethod
  def __getInstance(cls):
    return cls.__instance

  @classmethod
  def instance(cls, *args, **kargs):
    cls.__instance = cls(*args, **kargs)
    cls.instance = cls.__getInstance
    return cls.__instance


class Person(SingletonInstance):
    Name = ""
    Age = 0
    def __init__(self):
       pass

if __name__ == '__main__':
    print("==== __new___ ====")
    singleton1 = SingletonClass()
    singleton1.my_variable = "my variable"
    print(singleton1, singleton1.my_variable)
    singleton2 = SingletonClass()
    print(singleton2, singleton2.my_variable)

    print("==== LazyInstantiation ====")
    s1 = LazyInstantiation.getInstance()
    s1.test = "test data"
    print(s1, s1.test)
    s2 = LazyInstantiation.getInstance()
    print(s2, s2.test)

    print("==== Method type ====")
    p1 = Person.instance()
    p1.Name = "Hong Gil Dong"
    print(p1, p1.Name)
    p2 = Person.instance()
    print(p2, p2.Name)

    
    

