import test
import dice
import game

d = dice.Dice()
g = game.Game()
print('Welcome to Monopoly')
numPlayers = input('How many folk are playing?')
g.start(int(numPlayers))
print('Let us begin!')
while(True):
    for p in g.players:
        player, index = g.board.get_player_by_id(p.id)
        print('hi player '+str(p.id)+', you are at space: '+str(index))
        print('you have $'+str(player.Money)+' in your pocket')
        input('press Enter to roll the die')
        roll1 = d.roll()
        roll2 = d.roll()
        fullroll = roll1+roll2
        print('you rolled: '+str(roll1)+' and '+str(roll2))
        print('you moved '+ str(fullroll)+' spaces')
        g.board.move_player_by_player_id(p.id, fullroll)
        print('')
