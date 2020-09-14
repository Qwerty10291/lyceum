class LittleBell:
    def __init__(self):
        self.bell = 'ding'

    def sound(self):
        print(self.bell)


class BigBell:
    def __init__(self):
        self.bell = ['ding', 'dong']
        self.flag = False

    def sound(self):
        print(self.bell[int(self.flag)])
        self.flag = ~self.flag


class BellTower:
    def __init__(self, *bells):
        self.arrays = [i for i in bells]

    def sound(self):
        for i in self.arrays:
            i.sound()
        print('...')

    def append(self, item):
        self.arrays.append(item)

