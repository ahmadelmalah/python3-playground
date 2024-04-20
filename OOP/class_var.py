class MyClass:
    count = 0  # Class variable (acts like a static variable)

    def __init__(self, value):
        self.data = value
        MyClass.count += 1  # Increment count for each instance creation

    # Instance method that uses self var
    def get_count_via_instance_via_self(self):
        return self.count

    # Instance method that calls class var
    def get_count_via_instance_via_class_var(self):
        return MyClass.count

    @classmethod
    def get_count_via_param(cls):
        return cls.count

    @classmethod
    def get_count_via_class(cls):
        return MyClass.count


# Create instances
obj1 = MyClass(10)
obj2 = MyClass(20)

# Accessing using instance functions
print(obj1.get_count_via_instance_via_self())
print(obj2.get_count_via_instance_via_self())
print(obj2.get_count_via_instance_via_class_var())
print(obj2.get_count_via_instance_via_class_var())

# Accessing without an instance, talking directly to the class
# Via classmethod
print(MyClass.get_count_via_param())
print(MyClass.get_count_via_class())

# Via classvariable
print(MyClass.count)
