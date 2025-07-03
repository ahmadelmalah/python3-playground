class A:
    _instance = None

    def __new__(cls, data):
        # First time only, create a new instance
        if not cls._instance:
            cls._instance = super(A, cls).__new__(cls)

        return cls._instance

    def __init__(self, data):
        self.data = data


obj1 = A(10)
obj2 = A(15)
print(obj1.data)
print(obj2.data)
