#controlla se ciò che è stato passato possa diventare float
from typing import Any
def is_float(num: Any):

    try:
        float(num)
        return True
    
    except ValueError:

        risposta: bool = False

        if num.isdigit():

            risposta = True

        return risposta
    

class Fence:

    def __init__(self, 
                 area: float,
                 temperature: float,
                 habitat: str,
                 animals: list[Any] = []) -> None:
        
        if (not(is_float(area)))or(area <= 0):

            return

        else:
            self.area: float = float(area)

        while not(is_float(temperature)):

            return

        else:
            self.temperature: float = float(temperature)

        self.habitat: str = habitat
        self.remaining_area: float = area
        self.animals: list[Any] = animals.copy()

    def __str__(self) -> str:

        message: str = ''
    
        if (len(self.animals) > 0):    

            message = f'\nFence:\n'\
                f'\nFence(area={round(self.area, 3)},temperature: {round(self.temperature, 3)},habitat={self.habitat})\n'\
                    f'\nwith animals:'
            
            for animal in self.animals:

                message += f'\n{animal}'

            message += f'\n\n******************************'
        
        return message

class Animal:

    def __init__(self,
                 name: str,
                 species: str,
                 age: int,
                 height: float,
                 width: float,
                 preferred_habitat: str) -> None:
        
        self.name: str = name
        self.species: str = species

        while (type(age) != int)or(age <= 0):
            
            return
        else:
            self.age: int = age

        while (not(is_float(height)))or(height <= 0):

            return

        else:
            self.height: float = float(height)


        while (not(is_float(width)))or(width <= 0):

            return

        else:
            self.width: float = float(width)
            
        self.preferred_habitat: str = preferred_habitat

        self.health: float = round(100*(1/self.age), 3)

        self.fence: Fence = Fence(0, 0, 'a', [])

    def __str__(self) -> str:
        
        return f'\nAnimal(name={self.name},species:{self.species},età:{self.age})'


class ZooKeeper:

    def __init__(self,
                 name: str,
                 surname: str,
                 id: str) -> None:
        
        self.name: str = name
        self.surname: str = surname
        self.id: str = id


    def add_animal(self, 
                   animal: Animal, 
                   fence: Fence):
        
        occupied_space: float = animal.height * animal.width

        if (occupied_space <= fence.remaining_area)and(animal.preferred_habitat == fence.habitat):
            
            fence.animals.append(animal)

            fence.remaining_area -= occupied_space

            animal.fence = fence

        return


    def remove_animal(self, 
                      animal: Animal, 
                      fence: Fence):
        
        if animal in fence.animals:

            occupied_space: float = animal.height * animal.width

            fence.remaining_area += occupied_space
            fence.animals.remove(animal)


    def feed(self, 
             animal: Animal):
        
        if animal in animal.fence.animals:
            increased_height: float = animal.height + ((animal.height/100)*2)
            increased_width: float = animal.width + ((animal.width/100)*2)

            dim_re: float = animal.fence.remaining_area + (animal.height * animal.width)

            increased_animal: float = increased_height * increased_width

            if dim_re >= increased_animal:

                animal.fence.remaining_area += (animal.height * animal.width)
                animal.height = increased_height
                animal.width = increased_width
                animal.fence.remaining_area -= (animal.height * animal.width)
                
                animal.health = animal.health + (animal.health/100)
                
                


    def clean(self, 
              fence: Fence)->float:
        
        time: float = 0.0

        area_occupata: float = fence.area - fence.remaining_area

        if fence.remaining_area > 0.0:

            time = area_occupata / fence.remaining_area

            return round(time, 3)
        
        else:

            return area_occupata
    
    def __str__(self) -> str:
        
        messaggio: str = f'\nZookeeper(name={self.name},surname={self.surname},id={self.id})'
        
        return messaggio

class Zoo:
    
    def __init__(self,
                 fence: list[Fence] = [],
                 zookeeper: list[ZooKeeper] = []) -> None:
        
        self.fence: list[Fence] = fence
        self.zookeeper: list[ZooKeeper] = zookeeper

    def describe_zoo(self):
        
        messaggio: str = f'Guardians:'

        for i in self.zookeeper:

            messaggio += f'\n{i}'

        for j in self.fence:

            messaggio += f'\n{j}'

        return messaggio




a1: Animal = Animal(name='a',species='a',age=1,height=12,width=32,preferred_habitat='a')
a2: Animal = Animal(name="Toledo", species="Fox", age=16, height=0.5, width=1.25, preferred_habitat="a")

f1: Fence = Fence(area=10000,temperature=12,habitat='a')

zk1: ZooKeeper = ZooKeeper(name='a',surname='a',id='5213')

zk1.add_animal(a1,f1)
zk1.add_animal(a2, f1)

recinti: list[Fence] = [f1]
guardiani: list[ZooKeeper] = [zk1]

z1: Zoo = Zoo(recinti, guardiani)

print(f1.remaining_area)

zk1.feed(a1)
    
print(f1.remaining_area)

zk1.feed(a2)

print(f1.remaining_area)

print(z1.describe_zoo())

print(a2.height)
print(a2.width)