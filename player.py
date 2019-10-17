import unittest 


class test(unittest.TestCase): 
    def test_player_class_callable(self):
        self.assertIsNotNone(Player()) 
    def test_player_should_have_id(self):
        self.assertIsNotNone(Player().id)
    def test_player_should_have_money(self):
        self.assertIsNotNone(Player().money)
    
    pass 
    
    
class Player():
    def __init__(self): 
        self.id = 'Nickypoo'
        self.money = 300
    pass
    
if __name__ == '__main__': 
    unittest.main()
    