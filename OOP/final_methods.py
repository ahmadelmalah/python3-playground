class FinalMethodMeta(type):
    def __new__(cls, name, bases, attrs):
        if name != "BaseClass" and "final_method" in attrs:
            raise TypeError("Don't do that please!")
        return super().__new__(cls, name, bases, attrs)


class BaseClass(metaclass=FinalMethodMeta):
    def final_method(self):
        print("I will be sad if you override me")


class SubClass(BaseClass):
    def final_method(self):
        print("I don't care, I will override you")
