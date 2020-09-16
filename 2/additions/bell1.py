class Bell:
    def __init__(self, *args, **kwargs):
        self.dict = kwargs
        self.sorted = sorted([i for i in kwargs.keys()])
        self.args = list(args)

    def print_info(self):
        output = ''
        if len(self.sorted) > 0:
            output += ', '.join([f'{i}: {self.dict[i]}' for i in self.sorted])
            if len(self.args) > 0:
                output += '; '
        if len(self.args) > 0:
            output += ', '.join(self.args)
        if len(self.sorted) == 0 and len(self.args) == 0:
            print('-')
            return None
        print(output)


class LittleBell(Bell):
    bell = 'ding'

    def sound(self):
        print(self.bell)


class BigBell(Bell):
    bell = ['ding', 'dong']
    flag = False

    def sound(self):
        print(self.bell[int(self.flag)])
        self.flag = ~self.flag
