# Single inheritance = Father and Son
# multi-level inheritance = Father and Son and GrandSon
# hierarchical inheritance = Father and Daughter and Son
# multiple inheritance = Father, Mother and their son
 
class Father:
    money = 1000

    def __init__(self,fa):
        self.what = fa
        print(self.what,"constructor")

    @classmethod
    def show(cls):
        print(cls.money)

    @staticmethod
    def show2():
        a = 50
        print("This is static method from parent class",a)

class Son(Father):
    def __init__(self,fa,sa):
        super().__init__(fa)                     # To call parent class constructor
        
        self.what = sa
        print(self.what,"Constructor")

    def display():
        print("This is a regular method from son class")

class GrandSon(Son):
    def __init__(self,fa,sa):
        super().__init__(fa,sa)
        print("Grand son constructor")

# mike = Son('father','son')

gs = GrandSon('father','son')