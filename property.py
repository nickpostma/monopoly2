import unittest 
import player


class test(unittest.TestCase): 
    def test_property_class_callable(self):
        self.assertIsNotNone(Property(1,''))
    def test_property_should_have_id(self):
        id = 5
        self.assertEqual(Property(id,'').Id,id)
    def test_property_should_have_Name(self):
        name = 'Boardwalk'
        self.assertEqual(Property(1, name).Name, name)
    def test_player_should_have_money(self):
        cost = 500
        self.assertEqual(Property(1,'',cost).Cost, cost)
    def test_player_with_funds_should_purchase(self):
        p = player.Player()
        prop = Property(1,'Boardwalk',200)
        self.assertEqual(prop.Purchase(p), True)
    def test_player_without_funds_cannot_purchase(self):
        p = player.Player()
        prop = Property(1,'Boardwalk',70000)
        self.assertEqual(prop.Purchase(p), False)
    pass 
    
    
class Property():
    def __init__(self, id, name, cost = 0): 
        self.Id = id
        self.Name = name
        self.Cost = cost
        self.Players = {}
        self.Owner = {}
    def Purchase(self, p):
        if p.Money > self.Cost:
            p.Money = p.Money - self.Cost
            self.Owner = p
            return True
        return False
    pass
    
if __name__ == '__main__': 
    unittest.main()
    