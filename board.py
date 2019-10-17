import unittest 

class test(unittest.TestCase):     

    def test_that_board_has_40_properties(self): 
        self.assertEqual( len(Board().property_dictionary), 40) 

    pass 
    
    
class Board(): 
    def __init__(self): 
        self.property_dictionary = {} 
        self._assemble_property_dictionary()
        
    def _assemble_property_dictionary(self): 
        for i in range(40): 
            self.property_dictionary[i] = None
        
        
    pass 
    
    
if __name__ == '__main__': 
    import os
    os.system('cls') 
    unittest.main()
