import unittest 


class test(unittest.TestCase):     
    

    def test_that_board_has_40_properties(self): 
        self.assertEqual( len(Board().property_dictionary), 40) 
    
    def test_that_property_object_can_be_assigned_to_property_dict(self): 
        property = Property_test(index = 0)
        board = Board()
        board.assign_property_to_dictionary(property)
        self.assertEqual(board.property_dictionary[0] , property)
        
    def test_set_player_position(self): 
        
        player = Player_test(1) 
        property = Property_test(index = 0)
        board = Board() 
        index = 0 
        
        board.assign_property_to_dictionary(property)
        board.set_player_position(player, index) 
        self.assertEqual(board.property_dictionary[0].players[0], player)
        
    def test_set_all_players_starting_position(self): 
        
        player_set = [Player_test(i) for i in range(5)]
        property = Property_test(index = 0)
        board = Board() 
        index = 0       
        board.assign_property_to_dictionary(property)

        board.set_all_players_starting_position(player_set, index)
        
        self.assertEqual(board.property_dictionary[0].players, player_set)
    
    def test_find_players_at_index(self):
        player_set = [Player_test(i) for i in range(5)]
        property = Property_test(index = 0)
        board = Board() 
        index = 0       
        board.assign_property_to_dictionary(property)

        board.set_all_players_starting_position(player_set, index)
        
        self.assertEqual(board.get_players_at_index(index), player_set)
    
    def test_get_player_by_id(self): 
        player_set = [Player_test(i) for i in range(5)]
        property = Property_test(index = 0)
        board = Board() 
        index = 0       
        board.assign_property_to_dictionary(property)

        board.set_all_players_starting_position(player_set, index)
        specific_player_id = 1 
        
        self.assertEqual(board.get_player_by_id(specific_player_id)
                        , (player_set[1], index))
        
    
    def test_remove_player_from_property(self): 
    
        player_set = [Player_test(i) for i in range(5)]
        property = Property_test(index = 0)
        board = Board() 
        index = 0       
        board.assign_property_to_dictionary(property)
        board.set_all_players_starting_position(player_set, index)
        specific_player_id = 1 
        
        expected_players_at_property = [player for player in player_set if player.id != specific_player_id]
        
        #returns same as get player 
        self.assertEqual(board.get_player_by_id(specific_player_id, remove = True), (player_set[1], index))
        
        #property at index no longer contains that player
        self.assertEqual(board.property_dictionary[index].players, expected_players_at_property)
        
        
    
    def test_move_specific_player_1_space(self): 
        
        player_set = [Player_test(i) for i in range(5)]
        
        property = Property_test(index = 0)
        destination_property = Property_test(index = 1)
        
        board = Board() 
        index = 0     
        specific_player_id = 2 
        move_spaces = 1 
        
        board.assign_property_to_dictionary(property)
        board.assign_property_to_dictionary(destination_property)
        
        
        board.set_all_players_starting_position(player_set, index)
        
        board.move_player_by_player_id(specific_player_id, move_spaces) 
        
        self.assertEqual(len([player for player in board.property_dictionary[index].players 
                        if player.id == specific_player_id]), 0)
        
        self.assertEqual(board.get_player_by_id(specific_player_id)
                            , (player_set[2], destination_property.index))
        
    def test_move_specific_player_past_index_39(self): 
        
        player_set = [Player_test(i) for i in range(5)]
        
        property = Property_test(index = 0)
        destination_property = Property_test(index = 1)
        
        board = Board() 
        index = 39     
        specific_player_id = 2 
        move_spaces = 2
        
        board.assign_property_to_dictionary(property)
        board.assign_property_to_dictionary(destination_property)
        
        
        board.set_all_players_starting_position(player_set, index)
        
        board.move_player_by_player_id(specific_player_id, move_spaces) 
        
        self.assertEqual(len([player for player in board.property_dictionary[index].players 
                        if player.id == specific_player_id]), 0)
        
        self.assertEqual(board.get_player_by_id(specific_player_id)
                            , (player_set[2], destination_property.index))
    pass 
    
    
class Property_test(): 
    def __init__(self, index): 
        self.index = index 
        self.players = [] 
        
class Player_test(): 
    def __init__(self, id): 
        self.id = id 
        
        
    
    
class Board(): 
    def __init__(self): 
        self.property_dictionary = {} 
        self._assemble_property_dictionary()
        
    def _assemble_property_dictionary(self): 
        for i in range(40): 
            self.property_dictionary[i] = None
        
        for i in range(40):
            self.assign_property_to_dictionary(Property_test(index = i))
        
    def assign_property_to_dictionary(self, property):
        self.property_dictionary[property.index] = property
        
    def set_player_position(self, player, index): 
        self.property_dictionary[index].players.append(player) 
        
    def set_all_players_starting_position(self, players, index): 
        for player in players: 
            self.set_player_position(player, index) 
    
    def get_players_at_index(self, index): 
        return self.property_dictionary[index].players 
    
    def get_player_by_id(self, player_id, remove = False): 
        for index, property in self.property_dictionary.items(): 

            for player in property.players:
                if player.id == player_id:
                    if not remove: 
                        return (player, index)
                    else: 
                        p = property.players.remove(player)
                        return (player, index) 
            
        assert 1 == 0, 'Player Not Found in Any Property on Board'
            
    
    def move_player_by_player_id(self, player_id, move_amount): 
        
        player, player_index = self.get_player_by_id(player_id, remove = True)
        
        new_index = player_index + move_amount
        if new_index >= 40:
            new_index -= 40 
            
        self.set_player_position(player, new_index)
    
        return 
    
    pass 
    
    
if __name__ == '__main__': 
    import os
    os.system('cls') 
    unittest.main(verbosity = 2)
