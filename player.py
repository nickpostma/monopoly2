import unittest 


class test(unittest.TestCase): 
    def test_player_class_callable(self):
        self.assertIsNotNone(Player(id = 0)) 
    def test_player_should_have_id(self):
        self.assertIsNotNone(Player(id = 0).id)
    def test_player_should_have_money(self):
        self.assertIsNotNone(Player(id = 0).Money)
    
    pass 
    
    
class Player():
    def __init__(self, id, money = 0): 
        self.id = 'Nickypoo'
        self.Money = money
    pass
    
if __name__ == '__main__': 
    unittest.main(verbosity = 2)
    