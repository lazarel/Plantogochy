from abc import abstractmethod, ABC


class Plantae(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def water_level(self):
        pass

    @abstractmethod
    def photosynthesis(self):
        pass

    @abstractmethod
    def stress(self):
        pass

    @abstractmethod
    def hormones(self):
        pass


class C3EmbryoPlant(Plantae): #TODO
    pass


class C3JuvenalPlant(Plantae):
    def __init__(self):
        self.health = 100
        self.water = 70  # Имеем в виду 70%, пусть будет такое стартовое значение
        self.sun = 70  # уровень освещенности, нужен для фотосинтеза
        self.stress = 0
        self.auxin = 10
        self.cytokinin = 10
        self.aba = 0

    def water_level(self):
        self.water += 15

    def photosynthesis(self):
        pass

    def stress(self):
        pass

    def hormones(self):
        pass

class C3MaturePlant(Plantae): #TODO
    pass


class CAMEmbryoPlant(Plantae): #TODO
    def __init__(self):
        self.health = 100

class CAMMaturePlant(Plantae): #TODO
    pass


def increase_water_level(obj):
    obj.water_level()

