import unittest 


class test(unittest.TestCase): 
    def test_player_class_callable(self):
        self.assertIsNotNone(Player(id = 0)) 
    def test_player_should_have_id(self):
        self.assertIsNotNone(Player(id = 0).id)
    def test_player_should_have_money(self):
        self.assertIsNotNone(Player(id = 0).Money)
    def test_when_given_money_increase_money(self):
        p = Player()
        originalMoney = p.Money
        p.GiveMoney(200)
        self.assertTrue(p.Money > originalMoney)
        
    pass 
    
    
class Player():
    def __init__(self, id, money = 0): 
        self.id = 'Nickypoo'
        self.Money = money
    def GiveMoney(self, money):
        self.Money += money
    pass
    
if __name__ == '__main__': 
    unittest.main(verbosity = 2)
    