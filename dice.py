import unittest 
import random 

class test(unittest.TestCase):    

    def test_dice_roll_result_is_integer(self): 
        self.assertIsInstance(Dice().roll(), int)
 
    def test_dice_roll_result_is_between_1_and_6(self):
        for i in range(30):
            self.assertTrue( (Dice().roll() >= 1) and (Dice().roll() <= 6))

class Dice(): 

    def roll(self):
        result = random.randint(1, 6)
        return  result 

    
if __name__ == '__main__': 
    unittest.main(verbosity = 2)
    