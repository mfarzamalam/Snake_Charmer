# Method Resolution Order (MRO), When a father is polygamous

class Father:
    def __init__(self):
        super().__init__()
        print("Father constructor")

class Mother:
    def __init__(self):
        super().__init__()
        print("Mother constructor")

class Mother2:
    def __init__(self):
        super().__init__()
        print("Mother2 constructor")

class Mother3:
    def __init__(self):
        super().__init__()
        print("Mother3 constructor")

class Mother4:
    def __init__(self):
        super().__init__()
        print("Mother4 constructor")

class Son(Mother, Mother2, Mother3, Mother4, Father):
    def __init__(self):
        super().__init__()
        print("Son constructor")

s = Son()