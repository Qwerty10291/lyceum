class Note:
    def __init__(self, note, flag=False):
        self.notes = {'до': 'о', "ре": "э", 'ми': 'и',
                      'фа': 'а', 'соль': 'оль', 'ля': 'а', 'си': 'и'}
        self.note = note
        self.flag = flag

    def play(self):
        if self.flag:
            if self.note == 'соль':
                print('со-оль')
                return None
            print(self.note + '-' + self.notes[self.note])
            return None
        if self.note == 'соль':
            print('со-оль')
            return None
        print(self.note)

    def __str__(self):
        if self.flag:
            if self.note == 'соль':
                return 'со-оль'
            return self.note + '-' + self.notes[self.note]
        return self.note
