import unittest
from unittest import TestCase
from src.zoo import ZooKeeper, Animal, Fence#, Zoo


class TestZoo(TestCase):


    '''def setUp(self) -> None:

        self.zoo_1: Zoo = Zoo()
        self.zookeeper_1: ZooKeeper = ZooKeeper(name='Mario',surname='Rossi',id='5213')
        self.fence_1: Fence = Fence(area=100,temperature=25.0,habitat='Savana')
        self.animal_1: Animal = Animal(name="Toledo", species="Fox", age=16, height=0.5, width=1.25, preferred_habitat="Savana")'''

    def test_animal_dimensioni(self):

        #Questo test controlla che gli animali più grandi della dimensione della fence non venganno inseriti
        zookeeper_1: ZooKeeper = ZooKeeper(name='Mario',surname='Rossi',id='5213')
        animal_1: Animal = Animal(name="Dumbo", species="Elephantidae", age=16, height=3.2, width=2.4, preferred_habitat="Savana")
        fence_1: Fence = Fence(area=5,temperature=25.0,habitat='Savana')
        zookeeper_1.add_animal(animal_1, fence_1)
        result: int = len(fence_1.animals)
        message: str = f'Error: the function add_animal should not add self.animal_1 into self.fence_1'

        self.assertEqual(result, 0, message)

    def test_animal_habitat(self):

        #Questo test controlla che dentro fence non vengano messi animal con un habitat diverso da quello della fence

        zookeeper_1: ZooKeeper = ZooKeeper(name='Mario',surname='Rossi',id='5213')
        animal_1: Animal = Animal(name='Pluto', species='Canide', age=5, height=5.0, width=1.0, preferred_habitat='Città')
        fence_1: Fence = Fence(area=100,temperature=25.0,habitat='Savana')
        zookeeper_1.add_animal(animal_1, fence_1)

        result: int = len(fence_1.animals)
        message: str = f'Error: the function add_animal should not add self.animal_1 into self.fence_1'

        self.assertEqual(result, 0, message)

    def test_animal_add_animal(self):

        #Questo test controlla che gli animali che possono essere inseriti nella fence, vengano poi effettivamente inseriti
        zookeeper_1: ZooKeeper = ZooKeeper(name='Mario',surname='Rossi',id='5213')
        animal_1: Animal = Animal(name="Toledo", species="volpe", age=16, height=0.5, width=1.25, preferred_habitat="Savana")
        fence_1: Fence = Fence(area=100,temperature=25.0,habitat='Savana')
        zookeeper_1.add_animal(animal_1, fence_1)

        result: int = len(fence_1.animals)
        message: str = f'Error: the function add_animal should add self.animal_1 into self.fence_1'

        self.assertEqual(result, 1, message)

    def test_dimensione_fence_add(self):

        #Questo test controlla che la fence una volta inseriti gli animali la dimensione della fence venga diminuita
        zookeeper_1: ZooKeeper = ZooKeeper(name='Mario',surname='Rossi',id='5213')
        animal_1: Animal = Animal(name="Toledo", species="volpe", age=16, height=0.5, width=1.25, preferred_habitat="Savana")
        fence_1: Fence = Fence(area=100,temperature=25.0,habitat='Savana')

        controllo: float = fence_1.area - (animal_1.height * animal_1.width)

        zookeeper_1.add_animal(animal_1, fence_1)

        result: float = fence_1.remaining_area
        message: str = f'Taccini)Error: the function add_animal should modify the value of the remaning area'

        self.assertEqual(result, controllo, message)


    def test_dimensione_fence_remove(self):

        #Questo test controlla che la fence una volta inseriti gli animali la dimensione della fence venga diminuita
        zookeeper_1: ZooKeeper = ZooKeeper(name='Mario',surname='Rossi',id='5213')
        animal_1: Animal = Animal(name="Toledo", species="volpe", age=16, height=0.5, width=1.25, preferred_habitat="Savana")
        fence_1: Fence = Fence(area=100,temperature=25.0,habitat='Savana')
        zookeeper_1.add_animal(animal_1, fence_1)
        zookeeper_1.remove_animal(animal_1, fence_1)

        message: str = f'Taccini)Error: the function add_animal should modify the value of the remaning area'
        result: float = fence_1.remaining_area

        self.assertEqual(result, fence_1.area, message)




if __name__ == "__main__":

    unittest.main()


'''test_result: bool = False

try:

    zookeeper.remove_animal(animal_1, fence_1)

except Exception:

    test_result = True

self.assertEqual(test_result, True, message)'''



    
        