class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a > 3:
            raise StopIteration

        x = self.a
        self.a += 1
        return x


obj1 = MyNumbers()
for n in obj1:
    print(n)

obj2 = MyNumbers()
i = iter(obj2)
print(next(i))
print(next(i))
print(next(i))
