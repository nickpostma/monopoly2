import unittest 

import board 
import player

class test(unittest.TestCase): 

    def test_initialization_for_4_players(self): 
    
        game = Game()
        players_count = 4
        
        game.start(players = players_count)
        
        self.assertEqual(len(game.board.property_dictionary[0].players)
                            , players_count)
                            
        
    #def test_show_player_info(self): 
    
        pass  
        
        

    
class Game(): 

    def __init__(self): 
        pass 
        
    def start(self, players): 
        self.players = [player.Player(i) for i in range(players)]
    
        self.board = board.Board()
        starting_index = 0
        self.board.set_all_players_starting_position(self.players, starting_index)
        
        
        
        
if __name__ == '__main__': 
    import os
    os.system('cls') 
    unittest.main(verbosity = 2)