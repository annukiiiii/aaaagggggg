class akeraios:
    __count = 0

    def __init__(self, value=0):
        self.value = value
        akeraios.__count += 1
        print("A new object was created.")

    def __del__(self):
        akeraios.__count -= 1

    def set_value(self, v):
        self.value = v

    def get_value(self):
        return self.value

    def print_value(self):
        print(self.value)

    @classmethod
    def get_count(cls):
        return cls.__count

    def power(self, exp):
        return self.value ** exp



a1 = akeraios(5)
a1.print_value()
print(a1.power(3))
print("Objects:", akeraios.get_count())

a2 = akeraios(10)
print("Objects:", akeraios.get_count())
