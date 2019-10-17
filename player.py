import unittest 


class test(unittest.TestCase): 
    def test_player_class_callable(self):
        self.assertIsNotNone(Player()) 
    def test_player_should_have_id(self):
        self.assertIsNotNone(Player().id)
    def test_player_should_have_money(self):
        self.assertIsNotNone(Player().Money)
    def test_when_given_money_increase_money(self):
        p = Player()
        originalMoney = p.Money
        p.GiveMoney(200)
        self.assertTrue(p.Money > originalMoney)
    pass 
    
    
class Player():
    def __init__(self, id): 
        self.id = id
        self.Money = 300
    def GiveMoney(self, money):
        self.Money += money
    pass
    
if __name__ == '__main__': 
    unittest.main()
    