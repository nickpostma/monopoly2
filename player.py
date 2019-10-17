import unittest 


class test(unittest.TestCase): 
    def test_player_class_callable(self):
        self.assertIsNotNone(Player()) 
    
    pass 
    
    
    
if __name__ == '__main__': 
    unittest.main()
    