class Army:
    def __init__(self):
        self.name = 'Lt'

    def get_lt(self):
        print(self.name)

    class Navy:
        def __init__(self):
            self.ship = 10
            self.captain = 15
            self.guns = 2500

        def navy_muscles(self):
            print("Ship in navy",self.ship)
            print("Captain in navy",self.captain)
            print("Guns in navy",self.guns)


soldier = Army()
soldier.get_lt()

soldier2 = soldier.Navy()
soldier2.navy_muscles()