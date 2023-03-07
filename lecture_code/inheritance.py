class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>

class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>


class Pet(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)

class Dog(Pet):

    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats

class Cat(Pet):

    def __init__(self, name, hates_dogs):
        #Pet.__init__(self, name, "Cat")
        super(Cat, self).__init__()
        self.hates_dogs = hates_dogs

    def hatesDogs(self):
        return self.hates_dogs


class Reader(object):
    def __init__(self):
        self._size = 0
    @property
    def size(self):
        return self._size
    def read(self):
        data = 'data read'
        return data

class Writer(object):
    def __init__(self):
        self._size = 0
    @property
    def size(self):
        return self._size
    def write(self, data):
        # write data somewhere
        pass

class ReaderWriter(Reader,Writer):
    def __init__(self):
        super(ReaderWriter, self).__init__()
    
        
    
