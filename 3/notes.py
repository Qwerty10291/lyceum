class Note:
    def __init__(self, note, is_long=False):
        self.note = note
        self.dict = {"до": 'до-о', "ре": 'ре-э', "ми": 'ми-и',
                     "фа": 'фа-а', "соль": 'со-оль', "ля": "ля-а", "си": 'си-и'}
        self.long = is_long
        self.notes = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
        self.intervals = ["прима", "секунда", "терция",
                          "кварта", "квинта", "секста", "септима"]

    def __str__(self):
        if self.long:
            return self.dict[self.note]
        else:
            return self.note

    def __eq__(self, other):
        return self.note == other.note

    def __ne__(self, other):
        return self.note != other.note

    def __lt__(self, other):
        return self.notes.index(self.note) < other.notes.index(other.note)

    def __gt__(self, other):
        return self.notes.index(self.note) > other.notes.index(other.note)

    def __le__(self, other):
        return self.notes.index(self.note) <= other.notes.index(other.note)

    def __ge__(self, other):
        return self.notes.index(self.note) >= other.notes.index(other.note)

    def __lshift__(self, other):
        index = self.notes.index(self.note)
        for _ in range(other):
            if index == 0:
                index = len(self.notes) - 1
            else:
                index -= 1
        if self.long:
            return self.dict[self.notes[index]]
        else:
            return self.notes[index]

    def __rshift__(self, other):
        index = self.notes.index(self.note)
        for _ in range(other):
            if index == len(self.notes) - 1:
                index = 0
            else:
                index += 1
        if self.long:
            return self.dict[self.notes[index]]
        else:
            return self.notes[index]

    def get_interval(self, other):
        return self.intervals[abs(self.notes.index(self.note) - other.notes.index(other.note))]


class LoudNote(Note):
    def __init__(self, note, is_long=False):
        super().__init__(note, is_long=is_long)

    def __str__(self):
        return super().__str__().upper()


class DefaultNote(Note):
    def __init__(self, note='до', is_long=False):
        super().__init__(note, is_long=is_long)


class NoteWithOctave(Note):
    def __init__(self, note, octave, is_long=False):
        self.octave = octave
        super().__init__(note, is_long=is_long)

    def __str__(self):
        return f'{super().__str__()} ({self.octave})'


N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция",
             "кварта", "квинта", "секста", "септима"]